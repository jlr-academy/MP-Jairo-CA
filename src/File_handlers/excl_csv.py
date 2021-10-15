import csv
import os

def write(tocsv, path, file_name):
    if len(tocsv)>0:
        os.chdir(path)
        keys = tocsv[0].contents.keys()
        with open(file_name, 'w', newline='')  as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            for item in tocsv:
                dict_writer.writerow(item.contents)
        os.chdir("..\\")
    
def read(path, file_name):
    l = list()
    if os.path.exists(os.path.join(path, file_name)):
        with open(os.path.join(path, file_name), 'r') as f:
            l = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
        
        for i in range(0,len(l)):
            if "courier" in l[i].keys():
                l[i]["courier"] = int(l[i]["courier"])
            if "product" in l[i].keys():
                l[i]["product"] = l[i]["product"].split(",")
                l[i]["product"][0] = l[i]["product"][0][1:]
                l[i]["product"][-1] = l[i]["product"][-1][:-1]
                l[i]["product"] = list(map(int, l[i]["product"]))
                
    return l
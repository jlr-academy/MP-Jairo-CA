import os
from Items import Courier, Product

def write(x, path, file_name):
    with open(os.path.join(path, file_name), 'w') as f:
        for item in x:
            f.write(f"{item.namae}" + "\n")
        
def read(path, file_name):
    L = list()
    if os.path.exists(os.path.join(path, file_name)):
        with open(os.path.join(path, file_name), 'r') as f:
            f = f.readlines()
            for item in f:
                if file_name == "Product_list.txt":
                    L.append(Product(item.strip()))
                elif file_name == "Courier_list.txt":
                    L.append(Courier(item.strip()))

    return L

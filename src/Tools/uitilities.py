import os
from Items import Product, Courier, Order
from colorama import Fore, Back, Style
import tabulate
from colorama import init
init(autoreset=True)

def clear():
    # Clearing screen is different depending on whether windows or unix-like
    os.system('cls' if os.name == 'nt' else 'clear')
    
def create_dict(d = dict(), keys = [], list_d = list()):
    for i in range(0,len(keys)):
        user_input = cap(input('\n {:<50}'.format(Fore.CYAN + f'Enter the {keys[i]}. > ' + Style.RESET_ALL)))
        
            
        if not user_input and keys[i] in d:
            print('\n {:<50}'.format(Fore.WHITE + Back.LIGHTRED_EX + "You enter Blank and the value was not updated"))
        elif keys[i] == "name":
            if list_d and (((isinstance(list_d[0], Product) or isinstance(list_d[0], Courier)) and user_input in [obj.contents["name"] for obj in list_d]) or (isinstance(list_d[0], dict) and user_input in [obj["name"] for obj in list_d])):
                print('\n {:<50}'.format(Fore.WHITE + Back.LIGHTRED_EX + 'ID or Name already on database. Duplicate not permited...'))
                return {}
            elif not user_input:
                print('\n {:<50}'.format(Fore.WHITE + Back.LIGHTRED_EX + "You enter a Blank 'name' and the item was not created"))
                return {}
            elif keys[i] in d:
                print('\n {:<50}'.format(Fore.CYAN + f"{d[keys[i]]} changed to " + Fore.WHITE + f"{user_input}"))
                d[keys[i]] = user_input
            else:
                d[keys[i]] = user_input
                
        elif keys[i] == "price" or keys[i] == "quantity":
            try:
                if keys[i] in d:
                    print('\n {:<50}'.format(Fore.CYAN + f"{d[keys[i]]} changed to " + Fore.WHITE +  f"{user_input}"))
                    d[keys[i]] = float(user_input)
                else:
                    d[keys[i]] = float(user_input)
            except:
                if not user_input:
                    return d
                else:
                    print('\n {:<50}'.format(Back.RED + Fore.WHITE + '"price" should be interger or float...Enter "blank" if not known. item was not created'))
                    return {}
                
        elif keys[i] == "phone":
            try:
                if keys[i] in d:
                    print('\n {:<50}'.format(Fore.CYAN + f"{d[keys[i]]} changed to " + Fore.WHITE + f"{user_input}"))
                    d[keys[i]] = int(user_input)
                else:
                    d[keys[i]] = int(user_input)
            except:
                if not user_input:
                    return d
                else:
                    print('\n {:<50}'.format(Back.RED + Fore.WHITE + '"phone" should be interger...Enter "blank" if not known. item was not created'))
                    return {}
                
        elif keys[i] in d:
            print('\n {:<50}'.format(Fore.CYAN + f"{d[keys[i]]} changed to " + Fore.WHITE + f"{user_input}"))
            d[keys[i]] = user_input
            
        else:
            d[keys[i]] = user_input
            
    return d

def create_dict_with_list(d = dict(), L = list(), key = str, multiple = True):   
    check = True
    products_dummy = []
    while check == True:
        print('\n {:<35}'.format(Fore.CYAN + f'{key} Data:' + Style.RESET_ALL))
        print_list(L)
        if multiple == False:
            user_input = input('\n {:<35}'.format(Fore.CYAN + f'Select the {key} ID . > ' + Style.RESET_ALL))
            
            
            if user_input.isnumeric() and ((not key == "product" and not key == "courier" and len(L)>=int(user_input)>0) or ((key == "product" or key == "courier") and int(user_input) in [obj.contents["id"] for obj in L])):
                if key in d:
                    if key == "status":
                        d[key] = L[int(user_input)-1]
                        print('\n {:<35}'.format(Fore.CYAN + "Parameter changed"))
                    else:
                        d[key] = int(user_input)
                        print('\n {:<35}'.format(Fore.CYAN + "Parameter changed"))
                else:
                    d[key] = int(user_input)
                check = False
                
            else:
                input('\n {:<35}'.format(Fore.WHITE + Back.RED + 'Select Only from the list..  Press any key and try again..'  + Style.RESET_ALL))
                
                
        else:
            user_input = input('\n {:<35}'.format(Fore.CYAN + f'Select the {key} ID and the quantity. Use comma-separated values > ' + Style.RESET_ALL)).split(",")
            
            
            if user_input[0].isnumeric() and int(user_input[0]) in [obj.contents["id"] for obj in L]:
                
                for i in range(0, len(L)):
                    if L[i].contents["id"] == int(user_input[0]): dummy_id = i
                
                if len(user_input)>1 and user_input[1].isnumeric() and 0 < int(user_input[1]) <= L[dummy_id].contents["quantity"]:
                    products_dummy.append(int(user_input[0]))
                    products_dummy.append(float(user_input[1]))
                    L[dummy_id].contents["quantity"] = L[dummy_id].contents["quantity"] - float(user_input[1])
                else:
                    input('\n {:<35}'.format(Fore.WHITE + Back.RED + 'Quantity parameter not correct . Please try again..' + Style.RESET_ALL))
                    
                    continue
                
                if  like_to_continue('Would you like to add another Product? - "Y" for yes and "N" for no.'):
                    continue
                else:
                    if key in d:
                        print('\n {:<35}'.format(Fore.CYAN + "Parameter changed"))
                        
                        
                    d[key] = products_dummy
                    check = False 
            
            else:
                input('\n {:<35}'.format(Fore.WHITE + Back.RED + 'Select Only from the list..  Press any key and try again..' + Style.RESET_ALL))
                
            
    return d
    
# Prints index and list items
def print_dict(list):
    idx = 0
    for item in list:
        print('\n {:<35}'.format(Fore.CYAN + f"ID-{idx+1}: {item.contents}"))
        idx += 1
        
def print_dict_k(d = dict()):
    idx = 0
    l = []
    print(Fore.CYAN + '\n {:-^100}'.format(""))
    for key in d:
        if not key == "id":
            print('\n {:^100}'.format(Fore.CYAN + f"ID-{idx+1}:  " + Fore.WHITE + f"{key}"))
            l.append(key)
            idx += 1
    return l

def print_list(list):
    x = []
    if isinstance(list[0], Product) or isinstance(list[0], Courier):
        for item in list: x.append(item.contents)
        header = x[0].keys()
        rows =  [y.values() for y in x]
        print(Style.BRIGHT + tabulate.tabulate(rows, header, tablefmt="grid"))
        
    elif isinstance(list[0], dict):
        header = list[0].keys()
        rows =  [y.values() for y in list]
        print(Style.BRIGHT + tabulate.tabulate(rows, header, tablefmt="grid"))
        
    else:
        for count, value in enumerate(list):
            print('\n {:<35}'.format(Fore.CYAN + f"ID-{count+1}:" + Fore.WHITE + f"{value}"))

#Print a standard menu based on input and asks for user input
def create_menu(list = ["Main Menu", "Add New Product", "Edit an Product",  "Delete an Product", "Show Products", "Exit"]):
    clear()
    
    print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'{list[0]}'), "\n")
    
    
    for i in range(1,len(list)):
        print('{:>35}'.format(Fore.CYAN + f'{i}.') + '{:^35}'.format(Fore.WHITE + f'     {list[i]}'), "\n")
    
    user_choice = input('\n {:<35}'.format(Fore.CYAN + "Select from the Menu: > " + Style.RESET_ALL))
    
    
    # we will return the user choice.
    return user_choice

# Check if there is no orders
def no_orders(log, string = str):
    if not log:
        input('\n {:<35}'.format(Fore.LIGHTRED_EX + f'Nothing in the {string} database. Press any key to Continue..' + Style.RESET_ALL))
        
        return False
    else:
        return True

# Yes or No question with infinite loop  
def like_to_continue(text = "     You select Wrong value'. Would you like to continue in 'Edit a Product'? - 'Y' for yes and 'N' for no."):
    check = True
    while check == True:
        answer = input('\n {:<50}'.format(Back.LIGHTBLACK_EX + Fore.WHITE + text + Style.RESET_ALL))
        

        if answer.upper() == "Y":
            check = False
            return True
        elif answer.upper() != "N":
            pass
        else:
            check = False
            return False

#Check if user wnats to exit
def exit(x, y="     You select to Exit or not entered any commands from 'Editing an Product'.. Press any key to Exit. > "):
    if x.upper()=="E" or x ==' ' or x == '':
        input('\n {:<35}'.format(Back.LIGHTBLACK_EX + Fore.WHITE + y + Style.RESET_ALL))
        

        return True
    else:
        return False

#Capitalize the first letter of each word
def cap(edit_id):
    return " ".join([word.capitalize() for word in edit_id.split(" ")]) 
import os
from Items import Product, Courier, Order

def create_dict(d = dict(), keys = [], list_d = list()):
    for i in range(0,len(keys)):
        user_input = cap(input(f'   Enter the {keys[i]}. > '))
        if not user_input and keys[i] in d:
            print("You enter Blank and the value was not updated")
        elif keys[i] == "name":
            if user_input in [obj.contents["name"] for obj in list_d]:
                print('ID or Name already on database. Duplicate not permited...')
                return d
            elif not user_input:
                print("You enter a Blank 'name' and the value was not created")
                return d
            elif keys[i] in d:
                print(f"{d[keys[i]]} changed to {user_input}")
                d[keys[i]] = user_input
            else:
                d[keys[i]] = user_input
        elif keys[i] in d:
            print(f"{d[keys[i]]} changed to {user_input}")
            d[keys[i]] = user_input
        else:
            d[keys[i]] = user_input
            
    return d

def create_dict_with_list(d = dict(), L = list(), key = str, multiple = True):
    check = True
    while check == True:
        os.system('cls')
        print_list(L, key)
        if multiple == False:
            user_input = input(f'     Select the {key} ID . > ')
            if user_input.isnumeric() and len(L)>=int(user_input)>0:
                if key in d:
                    if key == "status":
                        print(f"{d[key]} changed to {L[int(user_input)-1]}")
                        d[key] = L[int(user_input)-1]
                    else:
                        print(f"{d[key]} changed to {user_input}")
                        d[key] = int(user_input)
                else:
                    d[key] = int(user_input)
                check = False
            else:
                input('   Select Only from the list..  Press any key and try again..')
        else:
            user_input = input(f'     Select the {key} ID . Use comma-separated ID values for multiple slection  > ').split(",")
            for i in range(0, len(user_input)):
                if user_input[i].isnumeric() and len(L)>=int(user_input[i])>0:
                    if i == len(user_input)-1:
                        if key in d:
                            print(f"{d[key]} changed to {list(map(int, user_input))}")
                        d[key] = list(map(int, user_input))
                        check = False     
                else:
                    input('   Select Only from the list..  Press any key and try again..')
                    break
            
    return d
    
# Prints index and list items
def print_dict(list):
    idx = 0
    for item in list:
        print(f"ID-{idx+1}: {item.contents}")
        idx += 1
        
def print_dict_k(d = dict()):
    idx = 0
    l = []
    for key in d:
        print(f"ID-{idx+1}: {key}")
        l.append(key)
        idx += 1
    return l

def print_list(list, string="Products"):
    x = []
    if isinstance(list[0], Product) or isinstance(list[0], Courier) or isinstance(list[0], Order):
        for count, value in enumerate(list):
            print(f"ID-{count+1}: {value.contents}")
    else:
        for count, value in enumerate(list):
            print(f"ID-{count+1}: {value}")

#Print a standard menu based on input and asks for user input
def create_menu(list = ["Main Menu", "Add New Product", "Edit an Product",  "Delete an Product", "Show Products", "Exit"]):
    os.system('cls')
    print(f'==========[ {list[0]} ]==========')
    for i in range(1,len(list)):
        print(f'     {i}. {list[i]}')
    
    user_choice = input("      Select from the Menu: > ") 
    
    # we will return the user choice.
    return user_choice

# Check if there is no orders
def no_orders(log, string = str):
    if not log:
        input(f'Nothing in the {string} database. Press any key to Continue..')
        return False
    else:
        return True

# Yes or No question with infinite loop  
def like_to_continue(text = "     You select Wrong value'. Would you like to continue in 'Edit a Product'? - 'Y' for yes and 'N' for no."):
    check = True
    while check == True:
        answer = input(text)
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
        input(y)
        return True
    else:
        return False

#Capitalize the first letter of each word
def cap(edit_id):
    return " ".join([word.capitalize() for word in edit_id.split(" ")]) 
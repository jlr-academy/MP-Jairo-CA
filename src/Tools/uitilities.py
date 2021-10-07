import os

# Prints index and list items
def print_dict(list, string="Order"):
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
    for count, value in enumerate(list):
        x.append(f"ID-{count+1}: {value.name}")
    return print(string + " List =", x)

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
def no_orders(log):
    if not log:
        input(f'Nothing in the database. Press any key to Continue..')
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
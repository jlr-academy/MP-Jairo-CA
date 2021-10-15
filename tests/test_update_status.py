import os
import sys
sys.path.append('C:/Users/jcanoalo\Desktop/IW/cafe_app/src')
from unittest.mock import Mock, patch

from Items import Order
from Tools.uitilities import no_orders, exit

def edit_order_status(like_to_continue, input, log=list(), string = "Order Status"):
    check_1 = True  
    while check_1 == True:
        os.system('cls')
        print(f"==========[ Edit a Status ]========== \n")
        #check if list is empty
        if not no_orders(log):
            return
        #ask for an item to edit
        edit_id = input(f'\n     Enter the {string} ID to Edit . [E to Exit]. > ')
        #check if user wants to exit
        if exit(edit_id, f"     You select to Exit or not entered any commands from 'Editing an {string}'.. Press any key to Exit. > "):
            return log
    
        if edit_id.isnumeric() and len(log)>=int(edit_id)>0:
            edit_id=int(edit_id)-1
        
            #ask for the key to edit
            while True:
                os.system('cls')
                print(f'\n     You Select to Change the Status of "{log[edit_id].contents}".')
                options = ["Preparing", "On its Way", "Delivered", "Cancelled"]
                for count, value in enumerate(options):
                    print(f"ID-{count+1}: {value}")
                status = input('     Select the new Status ID . > ')
                if status.isnumeric() and len(options)>=int(status)>0:
                    status = int(status)-1
                    break
                else:
                    input('   Select Only from the list..  Press any key and try again..')
            new_edit = options[status]
            
            print(f"{log[edit_id].contents['status']} changed to {new_edit}")
            log[edit_id].contents['status'] = new_edit
            if like_to_continue(f'Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                continue
            else:
                input(f"     You select Exit from 'Editing an {string}'.. Press any key to Exit. > ")
                check_1 = False
                return log
        else:
            #ID or name not in the databse and ask if user want to continue
            if not like_to_continue(f'     You Select an ID that is NOT Available in the Data-Base. Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                check_1 = False
                return log
        
def test_edit_order_status(expected, L, string, status):

    enter = "1"
    exit ="e"

    def mock_input(prompt):
        if "enter" in prompt.lower():
            return enter
        if "status" in prompt.lower():
            return status
        if "exit" in prompt.lower():
            return exit
    
    def mock_like_to_continue(prompt):
        return False

    actual = edit_order_status(mock_like_to_continue, mock_input, L, string)[int(enter)-1].contents
    print(actual)
    assert actual == expected

list_1 = {"customer_name" : "Jairo", "customer_address" : "Flat 6", "customer_phone" : "07", "courier" : 1, "status" : "Preparing"}example = {"customer_name" : "Jairo", "customer_address" : "Flat 6", "customer_phone" : "07", "courier" : 1, "status" : "On its Way"}test_edit_order_status(Order(example).contents, [Order(list_1)], "Order", "2")  list_1 = {"customer_name" : "Jairo", "customer_address" : "Flat 6", "customer_phone" : "07", "courier" : 1, "status" : "Preparing"}example = {"customer_name" : "Jairo", "customer_address" : "Flat 6", "customer_phone" : "07", "courier" : 1, "status" : "On its Way"}test_edit_order_status(Order(example).contents, [Order(list_1)], "Order", "0") 

def create_menu(list = ["Main Menu", "Add New Product", "Edit an Product",  "Delete an Product", "Show Products", "Exit"]):
    while True:
        os.system('cls')
        print(f'==========[ {list[0]} ]==========')
        for i in range(1,len(list)):
            print(f'     {i}. {list[i]}')

        user_choice = input("      Select from the Menu: > ") 
        
        if  user_choice.isnumeric() and len(list)>int(user_choice)>0:
            print(user_choice)
            return user_choice
        else:
            print("invalid argument")


@patch("builtins.input")
def test_create_menu(mock_input: Mock, ):
    
    mock_input.side_effect = ["99","1","1", "1"]

    #assemble
    expected__print_response = "invalid argument"
    expected = "1"
    #act
    print("3")
    actual = create_menu(list = ["Main Menu", "Add New Car", "Edit an Product",  "Delete an Product", "Show Products", "Exit"])
    print(actual)
    #assert actual == expected

    #mock_print.assert_called_with(expected__print_response)
    
test_create_menu()
    

import os
import sys
sys.path.append('C:/Users/jcanoalo/Desktop/IW/cafe_app/src')
from unittest.mock import Mock, patch
from src import __App__, Items


list_1 = {"customer_name" : "Jairo", "customer_address" : "Flat 6", "customer_phone" : "07", "courier" : 1, "status" : "Preparing"}
example = {"customer_name" : "Jairo", "customer_address" : "Flat 6", "customer_phone" : "07", "courier" : 1, "status" : "On its Way"}

@patch("src.Tools.uitilities.like_to_continue") 
@patch("builtins.input")
def test_edit_order_status(mock_input, mock_like_to_continue):
    
    #assemble
    expected = Items.Order(example).contents
    L = [Items.Order(list_1)]
    string = "Order"
    status = "2"
    print(L)
    mock_input.side_effect = ["1", status, "n", "n"]
    mock_like_to_continue.side_effect = [False]

    actual = __App__.Shop("1").edit_order_status(L, string)[int("1")-1].contents
    print(actual)
    assert actual == expected

test_edit_order_status()  


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
    

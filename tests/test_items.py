import sys
from unittest.mock import patch
sys.path.append('C:/Users/jcanoalo/Desktop/IW/Mini_project_1/src')
import Tools
from  __App__ import Shop
import Items


@patch("Tools.uitilities.like_to_continue") 
@patch("builtins.input")
@patch("__App__.fetch_orders")
def test_edit_order_status(mock_fetch_orders, mock_input, mock_like_to_continue):
    
    #assemble
    list_1 = {"customer_name" : "Jairo", "customer_address" : "Flat 6", "customer_phone" : "07", "courier" : 1, "status" : "Preparing"}
    example = {"customer_name" : "Jairo", "customer_address" : "Flat 6", "customer_phone" : "07", "courier" : 1, "status" : "On its Way"}
    expected = Items.Order(example).contents
    L = [Items.Order(list_1)]
    string = "Order"
    status = "2"
    
    mock_input.side_effect = ["1", status, "n", "n"]
    mock_like_to_continue.side_effect = [False]
    mock_fetch_orders.side_effect = ['fish']

    actual = Shop("1").edit_order_status(string)[int("1")-1]
    assert actual == expected
    
@patch('Tools.uitilities.like_to_continue') 
@patch("builtins.input")
def test_edit_order(mock_input, mock_like_to_continue):
    
    #assemble
    list_1 = {"id": "1", "customer_name" : "Jairo", "customer_address" : "Flat 6", "customer_phone" : "07", "courier" : 1, "status" : "Preparing"}
    example = {"id": "1", "customer_name" : "Pepe", "customer_address" : "Flat 6", "customer_phone" : "07", "courier" : 1, "status" : "Preparing"}
    expected = Items.Order(example).contents
    L = [Items.Order(list_1)]
    string = "Order"

    mock_input.side_effect = ["1", "1", "pepe", "n",""]
    mock_like_to_continue.side_effect = [False]

    actual = Shop("1").edit_order(L, string)[int("1")-1].contents
    print(actual)
    assert actual == expected
    
# @patch('Tools.uitilities.like_to_continue') 
# @patch("builtins.input")
# @patch('Tools.sql_utilities.edit_item_table')
# def test_edit_order_product(mock_edit_item_table, mock_input, mock_like_to_continue):
    
#     #assemble
#     list_1 = {"id": 5, "customer_name" : "Jairo", "customer_address" : "Flat 6", "customer_phone" : "07", "courier" : 1, "status" : "Preparing"}
#     example = {"id": 5, "customer_name" : "Pepe", "customer_address" : "Flat 6", "customer_phone" : "07", "courier" : 1, "status" : "Preparing"}
#     expected = Items.Product(example).contents
#     L = [Items.Product(list_1)]
#     string = "Product"

#     mock_edit_item_table.side_effect = [True]
#     mock_input.side_effect = ["5", "1", "pepe"]
#     mock_like_to_continue.side_effect = [False]

#     actual = __App__.Shop("1").edit_order(L, string)[int("1")-1].contents
    
#     assert actual == expected
        

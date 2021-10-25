from unittest.mock import Mock, call, patch
import sys
sys.path.append('C:/Users/jcanoalo/Desktop/IW/Mini_project_1/src')
from Tools.uitilities import create_dict, create_dict_with_list, print_dict, print_dict_k, print_list, create_menu, no_orders, like_to_continue, exit, cap
import __App__, Items

@patch("builtins.input")
def test_create_dict(mock_input):
    #asssemble
    d = {}
    keys = ["name", "adress"]
    list_d = []
    expected = {"name": "Jairo", "adress": "Flat"}
    mock_input.side_effect = ['Jairo', 'Flat']
    #act
    actual = create_dict(d, keys, list_d)
    
    assert actual == expected
    
@patch("builtins.input")
def test_create_dict_with_list(mock_input):
    #asssemble
    d = {}
    L = ["Jairo", "Kevin"]
    key = "name"
    multiple = False
    expected = {"name": 2}
    mock_input.side_effect = ['2']
    #act
    actual = create_dict_with_list(d, L, key, multiple)
    
    assert actual == expected

@patch("builtins.print")
def test_print_dict(mock_print):
    #assemble
    l = [{"name": "jairo", "age": "30"}]
    actual = []
    for item in l:
        actual.append(Items.Product(item))
    print_dict(actual)
    mock_print.assert_called_with("ID-1: {'name': 'jairo', 'age': '30'}")
    assert mock_print.call_count == 1
    
@patch("builtins.print")
def test_print_dict_k(mock_print):
    #assemble
    d = {"name": "jairo", "age": "30"}
    expected = [call("ID-1: name"), call("ID-2: age")]
    
    print_dict_k(d)
    
    mock_print.assert_has_calls(expected, any_order=False)
    assert mock_print.call_count == 2

@patch("builtins.print")
def test_print_list(mock_print):
    #assemble
    l = [{"name": "jairo", "age": "30"}]
    expected = [call("ID-1: {'name': 'jairo', 'age': '30'}")]
    
    actual = []
    for item in l:
        actual.append((item))
        
    actual = print_list(actual)
    
    mock_print.assert_has_calls(expected, any_order=False)
    assert mock_print.call_count == 1
    
@patch("builtins.print")
@patch("builtins.input")
def test_create_menu(mock_input, mock_print):
    #assemble
    mock_input.side_effect = ['1']
    l = ["name", "jairo", "age", "30"]
    expected = [call('     1. jairo'), call('     2. age')]
    
    actual = []
    for item in l:
        actual.append((item))
        
    actual = create_menu(actual)
    
    mock_print.assert_has_calls(expected, any_order=True)
    assert actual == "1"
    
@patch("builtins.input")
def test_create_menu_input(mock_input ):
    
    mock_input.side_effect = ["99","1","1", "1"]

    #assemble
    expected__print_response = "invalid argument"
    expected = "99"
    #act
    print("3")
    actual = create_menu(list = ["Main Menu", "Add New Car", "Edit an Product",  "Delete an Product", "Show Products", "Exit"])
    
    assert actual == expected
    
@patch("builtins.input")
def test_no_orders(mock_input):
    #assemble
    mock_input.side_effect = ['1']
    l = []
    string = "jairo"
    expected = False
    
    actual = no_orders(l, string)
    
    assert actual == expected

@patch("builtins.input")
def test_like_to_continue(mock_input):
    #assemble
    mock_input.side_effect = ['n']
    string = "jairo"
    expected = False
    
    actual = like_to_continue(string)
    
    assert actual == expected
    
@patch("builtins.input")
def test_exit(mock_input):
    #assemble
    mock_input.side_effect = ['']
    
    string = ""
    expected = True
    
    actual = exit(string, string)
    
    assert actual == expected
    
def test_cap():
    #assemble
    string = 'coke MAX'
    
    expected = "Coke Max"
    
    actual = cap(string)
    
    assert actual == expected
    
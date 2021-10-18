from unittest.mock import Mock, patch
import sys
sys.path.append('C:/Users/jcanoalo/Desktop/IW/cafe_app/src')
from src.Tools.uitilities import create_dict, create_dict_with_list

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
def test_print_dict(mock_print, mock_input):
    #assemble
    mock_input.side_effect = ['Jairo', '30']
    get_user_details()
    mock_print.assert_called_with("Thank you, your name is Jairo and your age is 30")
    assert mock_input.call_count == 2
    assert mock_print.call_count == 1
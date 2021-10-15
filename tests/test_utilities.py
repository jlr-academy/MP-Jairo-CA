import os
import sys

from src.Tools.uitilities import create_dict
sys.path.append('C:/Users/jcanoalo\Desktop/IW/cafe_app/src')
from unittest.mock import Mock, patch

from Items import Order
from Tools.uitilities import no_orders, exit

@patch("builtins.input")
def test_create_dict(mock_input, d, keys, list_d, expected):
    #asssemble
    mock_input.side_effect = ['Jairo', 'Flat']
    #act
    actual = create_dict(d, keys, list_d)
    
    assert actual == expected
    
d = {}
keys = ["name", "adress"]
#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple

def index_range(page:int, page_size:int)-> Tuple:
    """this function will return a tuple"""
    start_index = (page -1 ) * page_size
    end_index = page * page_size
    my_tuple = (start_index, end_index)
    return my_tuple


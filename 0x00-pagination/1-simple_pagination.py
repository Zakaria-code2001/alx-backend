#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple:
    """this function will return a tuple"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    my_tuple = (start_index, end_index)
    return my_tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        try:
            if page not in range(1, 11) or page_size not in range(1, 11):
                return []
            assert type(page) == int and type(page_size) == int, "Both page and page_size must be integers."
            start_index, end_index = index_range(page, page_size)
            page_data = self.__dataset[start_index:end_index]
            return page_data

        except AssertionError as e:
            print(e)

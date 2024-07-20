#!/usr/bin/env python3
"""
This module contains a helper function index_range and a class Server

index_range that takes two integer arguments page and page_size
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    compute start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters

    Arguments:
    page (integer), numbers are 1 indexed
    page_size (integer)

    Returns:
    tuple(start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server with the dataset.
        """
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
        """
        Get a specific page of the dataset.

        Arguments:
        page (int): Page number, default is 1
        page_size (int): Number of records per page, default is 10
        Returns:
        List[List]: A list of records for the requested page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Get a specific page of the dataset with hypermedia information.

        Arguments:
        page (int): Page number, default is 1
        page_size (int): Number of records per page, default is 10
        Returns:
        dict: A dictionary containing the requested page, total pages, and total records
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        total_records = len(self.dataset())
        total_pages = math.ceil(total_records / page_size)
        data = self.get_page(page, page_size)
        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'prev_page': page - 1 if page > 1 else None,
            'next_page': page + 1 if page < total_pages else None,
            'total_pages': total_pages
        }

# Question 1: Given two list, find the missing and additional values in both the list
from loguru import logger


def find_missing_additional(list1, list2):
    """
    This function takes in two lists and returns the missind and additiional values in both the lists.
    """
    set1 = set(list1)
    set2 = set(list2)

    missing_in_list1 = list(set2.difference(set1))
    additional_in_list1 = list(set1.difference(set2))
    return missing_in_list1, additional_in_list1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]
missing, additional = find_missing_additional(list1, list2)
logger.info(f"Missing in list1: {missing}")         # Output: [10, 11, 12, 13]
logger.info(f"Additional in list1: {additional}")   # Output: [1, 2, 3, 4]
logger.info(f"Missing in list2: {additional}")      # Output: [1, 2, 3, 4]
logger.info(f"Additional in list2: {missing}")      # Output: [10, 11, 12, 13]

# Question 3: Given three arrays, we have to find the common elements in all three sorted arrays using sets
def find_common_elements(arr1, arr2, arr3):
    """
    This function takes in three arrays and returns the common elements in all three arrays.
    """
    set1 = set(arr1)
    set2 = set(arr2)
    set3 = set(arr3)

    common_elements = list(set1.intersection(set2).intersection(set3))
    return common_elements

arr1 = [1, 2, 7, 11, 19, 21]
arr2 = [6, 7, 8, 19, 20]
arr3 = [3, 4, 7, 19, 23, 27, 28, 35]
common_elements = find_common_elements(arr1, arr2, arr3)
logger.info(f"Common elements in all three arrays: {common_elements}")  # Output: [7, 19]
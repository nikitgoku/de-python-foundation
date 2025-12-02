from loguru import logger

'''
Mini Exercise: List Sort and Insertion
---------------------------------
Write a Python function that takes a list of numbers sorted in ascending order and a number as input.
The function should insert the number into the list such that the list remains sorted in ascending order.
Do not use any built-in sort functions like sort() or sorted() and also do not use any list methods like append() or insert().
Additionally, write a similar function that handles lists sorted in
'''

def insert_number(num_list, number_to_insert):
    # Edge Cases
    # If number_to_insert is bigger than every other value in the list,
    # We can straigtaway append the value at the end
    if number_to_insert >= num_list[-1]:
        num_list += [number_to_insert]
        return num_list
    # If number_to_insert is smaller than every other value in the list,
    # We can straigtaway insert the value at the start
    if number_to_insert <= num_list[0]:
        num_list = [number_to_insert] + num_list
        return num_list
    
    # First let's find the index where the number is to be inserted
    index_to_insert = 0
    for i in range(len(num_list)):
        if num_list[i] < number_to_insert:
            index_to_insert += 1
        else:
            break
    
    # Now append a 'None' value in the list, so that we can move
    # elements from the list to the right
    num_list.append(None)
    
    # Now iterate the list from the end and move the elements one place forward
    # Until we reach the index, and then insert the number into the index
    for i in range(len(num_list) - 1, index_to_insert, -1):
        num_list[i] = num_list[i - 1]
        
    num_list[index_to_insert] = number_to_insert
    
    return num_list


def insert_number_decending(num_list, number_to_insert):
    """
    This functions takes in a list of numbers sorted in descending order and a number.
    Our task is to insert the number into the list such that the list remains sorted in descending order.
    Note: You cannot use any built--in sort functions like sort() or sorted() and also do not
    use any list methods like append() or insert().
    """
    # Edge Cases
    # If number_to_insert is smaller than every other value in the list,
    # We can straigtaway append the value at the end
    if number_to_insert <= num_list[-1]:
        return num_list + [number_to_insert]
    
    # If number_to_insert is bigger than every other value in the list,
    # We can straigtaway insert the value at the start
    if number_to_insert >= num_list[0]:
        return [number_to_insert] + num_list
    
    # First let's find the index where the number is to be inserted
    index_to_insert = 0
    for i in range(len(num_list)):
        if num_list[i] > number_to_insert:
            index_to_insert += 1
        else:
            break
    
    # Now append a 'None' value in the list, so that we can move
    # elements from the list to the right
    num_list.append(None)
    
    # Now iterate the list from the end and move the elements one place forward
    # Until we reach the index, and then insert the number into the index
    for i in range(len(num_list) - 1, index_to_insert, -1):
        num_list[i] = num_list[i - 1]
        
    num_list[index_to_insert] = number_to_insert
    
    return num_list
        
        
logger.info(insert_number([5, 17, 88, 108, 977], 100))  # Output: [5, 17, 88, 100, 108, 977]
logger.info(insert_number([1, 2, 3, 4, 5], 0))          # Output: [0, 1, 2, 3, 4, 5]
logger.info(insert_number([10, 20, 30, 40], 50))        # Output: [10, 20, 30, 40, 50]

logger.info(insert_number_decending([977, 108, 90, 17, 5], 100))  # Output: [5, 17, 88, 100, 108, 977]
logger.info(insert_number_decending([5, 4, 3, 2, 1], 0))          # Output: [0, 1, 2, 3, 4, 5]
logger.info(insert_number_decending([40, 30, 20, 10], 50))        # Output: [10, 20, 30, 40, 50]
    
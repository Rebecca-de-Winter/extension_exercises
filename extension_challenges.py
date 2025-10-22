def is_palindrome(phrase: str) -> bool:
    """
    Figures out whether a phrase is a palindrome. A palindrome is a word or phrase that reads the same forwards and
    backwards, ignoring any spaces or punctuation and treating all letters as lowercase.

    Examples:
        Input: "racecar"
        Output: True

        Input: "Australovenator"
        Output: False

        Input: "Taco cat"
        Output: True

        Input: "Taco truck"
        Output: False

        Input: "A man, a plan, a canal - Panama"
        Output: True

        Input: "Panama is a country"
        Output: False

    Args:
        phrase (str): The phrase to check.

    Returns:
        booL: True if the phrase is a palindrome, False otherwise.
    """
    # Convert the entire string to lowercase
    s = phrase.lower()
    
    # Clean the string: remove any characters that are not alphabets
    cleaned_str = ""
    for char in s:
        if char.isalpha():
            cleaned_str += char
            
    # Check for palindrome
    return cleaned_str == cleaned_str[::-1]


def string_to_nested_list(input_string: str) -> list:
    """
    Given some multi-line string with comma-separated values, output a list of lists of the values like rows and columns
    of a spreadsheet.

    Examples:
         Input: "1,2,3\n4,5,6\n7,8,9"
         Output: [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

         Input: "Australovenator,Australia\nAnkylosaurus,North America"
         Output: [["Australovenator", "Australia"], ["Ankylosaurus", "North America"]]

         Input: "Hello,Greeting"
         Output: [["Hello", "Greeting"]]

    Args:
        input_string (str): Some string we want to parse

    Returns:
        The list of lists of the values in that string
    """
    sublist_strings = input_string.split("\n")
    nested_list = []
    for s in sublist_strings:
        nested_list.append(s.split(","))
    return nested_list


def binary_search(list_to_search: list, value_to_find: int) -> int:
    """
    Implement a binary search algorithm. You can assume list_to_search is sorted.

    Examples:
        Input: [1, 2, 3, 4, 5], 3
        Output: 2

        Input: [2, 3, 5, 7, 11, 13], 13
        Output: 5

        Input: [2, 4, 6, 8, 10], 15
        Output: -1

    Args:
        list_to_search (list): the sorted list to search.
        value_to_find (int): the value to search for.

    Returns:
        int: the index of the element in list_to_search, or -1 if the element can't be found.
    """
    low = 0
    high = len(list_to_search) - 1
    while low <= high:
        mid = low + (high - low) // 2  # Calculate the middle index

        # If the target is found at the middle
        if list_to_search[mid] == value_to_find:
            return mid
        # If the target is greater than the middle element, search the right half
        elif list_to_search[mid] < value_to_find:
            low = mid + 1
        # If the target is smaller than the middle element, search the left half
        else:
            high = mid - 1

    # Target not found in the list/array
    return -1

def bubble_sort(list_to_sort: list) -> list:
    """
    An implementation of the bubble sort algorithm.

    Args:
        list_to_sort (list): the list to sort

    Returns:
        list: the sorted list
    """
    # Outer loop to iterate through the list n times
    for n in range(len(list_to_sort) - 1, 0, -1):
        
        # Initialize swapped to track if any swaps occur
        swapped = False  

        # Inner loop to compare adjacent elements
        for i in range(n):
            if list_to_sort[i] > list_to_sort[i + 1]:
              
                # Swap elements if they are in the wrong order
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                
                # Mark that a swap has occurred
                swapped = True
        
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break
    return list_to_sort

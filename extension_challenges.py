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
    pass


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
    pass


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
    pass

def bubble_sort(list_to_sort: list) -> list:
    """
    An implementation of the bubble sort algorithm.

    Args:
        list_to_sort (list): the list to sort

    Returns:
        list: the sorted list
    """
    pass


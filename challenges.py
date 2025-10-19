def fibonacci(n: int) -> int:
    """
    Returns the nth element of the Fibonacci sequence.

    The Fibonacci sequence is a series of numbers where each number is the sum of the two before it. The 0th element is
    0, the 1st element is 1, the 2nd element is 1, the 3rd element is 2, and so on.

    Args:
        n (int): The number of the element that must be returned.

    Returns:
        int: The nth element of the Fibonacci sequence.
    """
    pass
    a = 0
    b = 1

    # Check if n is less than 0
    if n < 0:
        print("incorrect input")

    # check if n = 0
    elif n == 0:
        return 0
    
    elif n ==1: 
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(9))


def flatten_list(input_list: list) -> list:
    """
    Takes a nested list and returns a single list of all the elements in the lists inside the nested list.

    Examples:
        Input: [[1, 2], [3, 4]]
        Output: [1, 2, 3, 4]

        Input: [[2, 3, 5, 7], [11, 13, 17, 19, 23]]
        Output: [2, 3, 5, 7, 11, 13, 17, 19, 23]

    Args:
        input_list (list): A list of lists to flatten.

    Returns:
        list: the flattened list
    """
    flat_list = []
    for row in input_list:
        flat_list.extend(row)
    return flat_list
# extend == += aka concatenation



def print_dict(dictionary: dict) -> None:
    """
    Given a dictionary, print the output in a nice way, with each key-item pair on a new line and the key and value
    separated by a colon.

    Examples:
        Input: {"German": "Guten Tag", "English": "Hello", "Spanish": "Hola"}
        Output:
            German: Guten Tag
            English: Hello
            Spanish: Hola

        Input: {"Spinach": 4.95, "Milk": 6.5, "Chicken": 10.0}
        Output:
            Spinach: 4.95
            Milk: 6.5
            Chicken: 10.0

    Args:
        dictionary (dict): Some dictionary we want to print in a nice way.
    """
    pass

def do_math(math: str) -> float:
    """
    Do the math described by the input string. Assume they'll always be in the format "<number> <operator> <number>",
    and the only operators we'll give you are "+", "-", "*", and "/"

    Examples:
        Input: "3 * 3"
        Output: 9.0

        Input: "5 / 2"
        Output: 2.5

        Input: "30 + 70"
        Output: 100.0

        Input: "50.5 - 20":
        Output: 30.5

    Args:
        math (str): The string that contains an operation to perform

    Returns:
        float: The result of the math
    """
    pass
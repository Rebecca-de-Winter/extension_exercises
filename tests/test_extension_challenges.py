import unittest

from extension_challenges import is_palindrome, string_to_nested_list, binary_search, bubble_sort


class TestCase(unittest.TestCase):
    def test_is_palindrome(self):
        test_cases = [
            ("racecar", True),
            ("Taco cat", True),
            ("A man, a plan, a canal - Panama", True),
            ("Australovenator", False)
        ]

        for function_input, expected in test_cases:
            actual = is_palindrome(function_input)

            if not isinstance(actual, bool):
                self.fail(
                    f"is_palindrome(\"{function_input}\") was supposed to return a bool, but it returned {type(actual)}")

            self.assertEqual(expected, actual, msg=f"\nInput: {function_input}\nExpected: {expected}\nActual: {actual}")

    def test_string_to_nested_list(self):
        test_cases = [
            ("1,2,3\n4,5,6\n7,8,9", [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]),
            ("Australovenator,Australia\nAnkylosaurus,North America",
             [["Australovenator", "Australia"], ["Ankylosaurus", "North America"]]),
            ("Hello,Greeting", [["Hello", "Greeting"]])
        ]

        for function_input, expected in test_cases:
            actual = string_to_nested_list(function_input)

            if not isinstance(actual, list):
                self.fail(
                    f"string_to_nested_list(\"{function_input}\") was supposed to return a list, but it returned {type(actual)}")

            self.assertEqual(expected, actual, msg=f"\nInput: {function_input}\nExpected: {expected}\nActual: {actual}")

    def test_binary_search(self):
        test_cases = [
            (([1, 2, 3, 4, 5], 3), 2),
            (([2, 3, 5, 7, 11, 13], 13), 5),
            (([2, 4, 6, 8, 10], 15), -1)
        ]

        for function_input, expected in test_cases:
            actual = binary_search(*function_input)

            if not isinstance(actual, int):
                self.fail(
                    f"binary_search({function_input[0]}, {function_input[1]}) was supposed to return an int, but it returned {type(actual)}")

            self.assertEqual(expected, actual, msg=f"\nInput: {function_input[0]}, {function_input[1]}\nExpected: {expected}\nActual: {actual}")

    def test_bubble_sort(self):
        test_cases = [
            ([1, 5, 2, 4, 3], [1, 2, 3, 4, 5]),
            ([1.1, 1.5, 1.2, 3.5, 2.2], [1.1, 1.2, 1.5, 2.2, 3.5]),
            (["test", "tester", "tested", "tea"], ["tea", "test", "tested", "tester"])
        ]

        for function_input, expected in test_cases:
            actual = bubble_sort(function_input)

            if not isinstance(actual, list):
                self.fail(
                    f"bubble_sort({function_input}) was supposed to return a list, but it returned {type(actual)}")

            self.assertEqual(expected, actual,
                             msg=f"\nInput: {function_input}\nExpected: {expected}\nActual: {actual}")

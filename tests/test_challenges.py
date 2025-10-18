import unittest
import io
import sys

from challenges import fibonacci, flatten_list, print_dict, do_math


class TestCase(unittest.TestCase):
    def test_fibonacci(self):
        test_cases = [
            (0, 0),
            (1, 1),
            (10, 55)
        ]

        for function_input, expected in test_cases:
            actual = fibonacci(function_input)

            if not isinstance(actual, int):
                self.fail(f"fibonacci({function_input}) was supposed to return an int, but it returned {type(actual)}")

            self.assertEqual(expected, actual, msg=f"\nInput: {function_input}\nExpected: {expected}\nActual: {actual}")

    def test_flatten_list(self):
        test_cases = [
            ([[1, 2], [3, 4]], [1, 2, 3, 4]),
            ([[2, 3, 5, 7], [11, 13, 17, 19, 23]], [2, 3, 5, 7, 11, 13, 17, 19, 23])
        ]

        for function_input, expected in test_cases:
            actual = flatten_list(function_input)

            if not isinstance(actual, list):
                self.fail(
                    f"flatten_list({function_input}) was supposed to return a list, but it returned {type(actual)}")

            self.assertEqual(expected, actual,
                             msg=f"\nInput: {function_input}\nExpected: {expected}\nActual: {actual}")

    def test_print_dict(self):
        test_cases = [
            ({"German": "Guten Tag", "English": "Hello", "Spanish": "Hola"}, "German: Guten Tag\nEnglish: Hello\nSpanish: Hola\n"),
            ({"Spinach": 4.95, "Milk": 6.5, "Chicken": 10.0}, "Spinach: 4.95\nMilk: 6.5\nChicken: 10.0\n")
        ]

        for function_input, expected in test_cases:
            captured_output = io.StringIO()
            sys.stdout = captured_output
            out = print_dict(function_input)
            sys.stdout = sys.__stdout__
            actual = captured_output.getvalue()

            if out is not None:
                self.fail(
                    f"print_dict({function_input}) was supposed to return None, but it returned {type(out)}")

            self.assertEqual(expected, actual,
                             msg=f"\nInput: {function_input}\nExpected: {expected}\nActual: {actual}")

    def test_do_math(self):
        test_cases = [
            ("3 * 3", 9.0),
            ("5 / 2", 2.5),
            ("30 + 70", 100.0),
            ("50.5 - 20", 30.5)
        ]

        for function_input, expected in test_cases:
            actual = do_math(function_input)

            if not isinstance(actual, float):
                self.fail(
                    f"do_math(\"{function_input}\") was supposed to return a float, but it returned {type(actual)}")

            self.assertEqual(expected, actual,
                             msg=f"\nInput: {function_input}\nExpected: {expected}\nActual: {actual}")

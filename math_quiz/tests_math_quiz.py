import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_expression

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if the operator generated is one of the valid options: '+', '-', '*'
        valid_operators = ['+', '-', '*']
        for _ in range(100):  # Test multiple times to ensure randomness
            operator = generate_random_operator()
            self.assertIn(operator, valid_operators)

    def test_calculate_expression(self):
        # Test different expressions for correctness
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (9, 4, '-', '9 - 4', 5),
            (3, 3, '*', '3 * 3', 9),
            (10, 5, '-', '10 - 5', 5),
            (7, 2, '+', '7 + 2', 9)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, result = calculate_expression(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(result, expected_answer)

if __name__ == "__main__":
    unittest.main()
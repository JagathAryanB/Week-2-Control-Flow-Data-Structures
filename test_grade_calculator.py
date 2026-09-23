import unittest
from unittest import mock

import grade_calculator


class GradeCalculatorTests(unittest.TestCase):
    def test_calculate_grade_for_high_average(self):
        grade, comment = grade_calculator.calculate_grade(95)
        self.assertEqual(grade, 'A')
        self.assertIn('Excellent', comment)

    def test_calculate_grade_for_borderline_average(self):
        grade, comment = grade_calculator.calculate_grade(75)
        self.assertEqual(grade, 'C')
        self.assertIn('Good', comment)

    def test_get_valid_number_accepts_valid_value(self):
        with mock.patch('builtins.input', side_effect=['5']):
            value = grade_calculator.get_valid_number('Enter number', min_val=1, max_val=10)
        self.assertEqual(value, 5.0)


if __name__ == '__main__':
    unittest.main()

import unittest
from is_leap_year import is_leap_year
class TestIsLeapYear(unittest.TestCase):
    def test_leap_year(self):
        self.assertEqual(is_leap_year(2024), True)
        self.assertEqual(is_leap_year(2000), True)
        self.assertEqual(is_leap_year(2020), True)

    def test_non_leap_year(self):
        self.assertEqual(is_leap_year(2023), False)
        self.assertEqual(is_leap_year(2001), False)
        self.assertEqual(is_leap_year(1900), False)

if __name__ == '__main__':
    unittest.main()

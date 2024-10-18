"""
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE

This module contains unit tests for the Flatmate Bill Sharing project.
"""

import unittest
from flatmate_bill.bill import Bill
from flatmate_bill.flatmate import Flatmate


class TestFlatmateBill(unittest.TestCase):
    """
    Unit tests for the Flatmate and Bill classes.
    """

    def setUp(self):
        """Setting up test data."""
        self.bill = Bill(amount=120, period="March 2024")
        self.flatmate1 = Flatmate(name="Alice", days_in_house=20)
        self.flatmate2 = Flatmate(name="Bob", days_in_house=10)

    def test_flatmate_pays(self):
        """Test if the flatmates pay the correct amount."""
        self.assertAlmostEqual(self.flatmate1.pays(self.bill, self.flatmate2), 80)
        self.assertAlmostEqual(self.flatmate2.pays(self.bill, self.flatmate1), 40)

    def test_flatmate_zero_days(self):
        """Test if a flatmate with 0 days pays 0."""
        self.flatmate2.days_in_house = 0
        self.assertAlmostEqual(self.flatmate2.pays(self.bill, self.flatmate1), 0)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover

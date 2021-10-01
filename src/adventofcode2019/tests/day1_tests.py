import unittest

import day1


class Day1Test(unittest.TestCase):

    def test_fuel_calculation(self):
        self.assertEqual(2, day1.calc_fuel(12))
        self.assertEqual(654, day1.calc_fuel(1969))
        self.assertEqual(33583, day1.calc_fuel(100756))

    def test_fuel_calculation_recursive(self):
        self.assertEqual(2, day1.part_two(14))
        self.assertEqual(966, day1.part_two(1969))
        self.assertEqual(50346, day1.part_two(100756))

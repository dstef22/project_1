import unittest
from calc_formulas import *
# To test calc_formulas


class TestCase(unittest.TestCase):
    delta_value = 0.000001

    def test_euler(self):
        self.assertAlmostEqual(euler(2), 7.38905609893, delta=0.001)
        self.assertAlmostEqual(euler(5), 148.413159103, delta=0.001)
        self.assertAlmostEqual(euler(6), 403.428793493, delta=0.01)
        self.assertAlmostEqual(euler(7), 1096.63315843, delta=1)

    def test_factorial(self):
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(-4), -24)
        # self.assertRaises(ValueError, factorial(0.25)) FIXME

    def test_power(self):
        self.assertEqual(power(2, 2), 4)
        self.assertEqual(power(-2, 2), 4)
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(2, 1), 2)
        self.assertEqual(power(-2, 1), -2)
        self.assertAlmostEqual(power(4, -2), 0.0625, delta=self.delta_value)
        self.assertAlmostEqual(power(3.2, 4), 104.8576, delta=self.delta_value)
        # self.assertRaises(ValueError, power(2, 0.2)) FIXME

    def test_multiply(self):
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(-3, 2), -6)
        self.assertEqual(multiply(2, -5), -10)
        self.assertEqual(multiply(-3, -5), 15)
        self.assertAlmostEqual(multiply(0.5, 2), 1, delta=self.delta_value)
        self.assertAlmostEqual(multiply(2, 0.25), 0.5, delta=self.delta_value)
        self.assertAlmostEqual(multiply(0.25, 0.25), 0.0625, delta=self.delta_value)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(15, -3), -5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(0.5, 0.25), 2)
        self.assertAlmostEqual(divide(2, 4), 0.5, delta=self.delta_value)
        self.assertAlmostEqual(divide(0.25, 0.5), 0.5, delta=self.delta_value)

    def test_add(self):
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(2, -2), 0)
        self.assertEqual(add(-2, 2), 0)
        self.assertAlmostEqual(add(0.25, 0.5), 0.75, delta=self.delta_value)
        self.assertAlmostEqual(add(0.25, 2), 2.25, delta=self.delta_value)
        self.assertAlmostEqual(add(2, 0.5), 2.5, delta=self.delta_value)

    def test_subtract(self):
        self.assertEqual(subtract(2, 2), 0)
        self.assertEqual(subtract(2, 4), -2)
        self.assertEqual(subtract(-2, 2), -4)
        self.assertEqual(subtract(2, -2), 4)
        self.assertEqual(subtract(-2, -2), 0)
        self.assertAlmostEqual(subtract(0.5, 0.25), 0.25, delta=self.delta_value)
        self.assertAlmostEqual(subtract(2, 0.5), 1.5, delta=self.delta_value)
        self.assertAlmostEqual(subtract(0.5, 1), -0.5, delta=self.delta_value)

import unittest
from calc_formulas import *
"""
    Final Project 1: Calculator.
        From lab 03 I am creating a gui to use the basic formulas.
        I am adding the new formulas power, percentage, plus/minus, and factorial.
        I am adding formulas to approximate for sin, cos, and e.
        I am adding a function to backspace, one to go back to the previous number, and one to clear.

    Project author:
    Dallin Stefanidis
    dstefanidis@unomaha.edu
    https://github.com/dstef22

    Credit and disclaimer:
    Gui design inspiration came from John Elder in this video: 
    https://www.youtube.com/watch?v=H1FpwbavWIk&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=8
    
    Icons used were created by Yusuke Kamiyamane and taken from https://p.yusukekamiyamane.com/.
    These icons are available under a Creative Commons Attribution 3.0 License
    https://creativecommons.org/licenses/by/3.0/.
    Yusuke Kamiyamane had no part in creating this project.
"""


# To test calc_formulas.py
class TestCase(unittest.TestCase):
    delta_value = 0.000001

    def test_euler(self):
        self.assertAlmostEqual(euler(-2), 0.13533528323, delta=0.001)
        self.assertAlmostEqual(euler(2), 7.38905609893, delta=0.001)
        self.assertAlmostEqual(euler(2.5), 12.1824939607, delta=0.001)
        self.assertAlmostEqual(euler(5), 148.413159103, delta=0.001)
        self.assertAlmostEqual(euler(6), 403.428793493, delta=0.01)
        self.assertAlmostEqual(euler(7), 1096.63315843, delta=1)

    def test_sin(self):
        self.assertAlmostEqual(sin(-2), -0.90929742682, delta=0.000001)
        self.assertAlmostEqual(sin(2), 0.90929742682, delta=0.000001)
        self.assertAlmostEqual(sin(2.5), 0.5984721441, delta=0.000001)
        self.assertAlmostEqual(sin(4), -0.7568024953, delta=0.000001)
        self.assertAlmostEqual(sin(7), 0.65698659871, delta=0.000001)
        self.assertAlmostEqual(sin(12), -0.536572918, delta=0.0001)
        self.assertAlmostEqual(sin(13), 0.42016703682, delta=0.01)
        self.assertAlmostEqual(sin(14), 0.99060735569, delta=0.1)
        self.assertAlmostEqual(sin(15), 0.65028784015, delta=1)

    def test_cos(self):
        self.assertAlmostEqual(cos(-3), -0.9899924966, delta=0.000001)
        self.assertAlmostEqual(cos(-2), -0.41614683654, delta=0.000001)
        self.assertAlmostEqual(cos(2), -0.41614683654, delta=0.000001)
        self.assertAlmostEqual(cos(2.5), -0.80114361554, delta=0.000001)
        self.assertAlmostEqual(cos(4), -0.65364362086, delta=0.000001)
        self.assertAlmostEqual(cos(7), 0.75390225434, delta=0.000001)
        self.assertAlmostEqual(cos(12), 0.84385395873, delta=0.001)
        self.assertAlmostEqual(cos(13), 0.90744678145, delta=0.01)
        self.assertAlmostEqual(cos(14), 0.1367372182, delta=0.1)
        self.assertAlmostEqual(cos(15), -0.75968791285, delta=1)

    def test_factorial(self):
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(-4), -24)
        # self.assertRaises(ValueError, factorial(0.25)) test doesn't work

    def test_power(self):
        self.assertEqual(power(2, 2), 4)
        self.assertEqual(power(-2, 2), 4)
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(2, 1), 2)
        self.assertEqual(power(-2, 1), -2)
        self.assertAlmostEqual(power(4, -2), 0.0625, delta=self.delta_value)
        self.assertAlmostEqual(power(3.2, 4), 104.8576, delta=self.delta_value)

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

    def test_percent(self):
        self.assertEqual(percent(20), 0.2)
        self.assertEqual(percent(100), 1)
        self.assertEqual(percent(-50), -0.5)
        self.assertEqual(percent(2.25), 0.0225)

    def test_plusminus(self):
        self.assertEqual(plusminus(25), -25)
        self.assertEqual(plusminus(-25), 25)

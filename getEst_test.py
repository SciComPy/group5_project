#Unit testing for getEst function

from PiSimulation import PiSimulation
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test_negative_large_both(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(-213123, -232323))

    def test_negative_large_first(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(-213123, 232323))

    def test_negative_large_second(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(213123, -232323))

    def test_negative_small_both(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(-2, -3))

    def test_negative_small_first(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(-2, 3))

    def test_negative_small_second(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(2, -3))

    def test_negative_one_both(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(-1, -1))

    def test_negative_one_first(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(-1, 2))

    def test_negative_one_second(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(2, -1))

    def test_zero_both(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(0,0))

    def test_zero_first(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(0,2))

    def test_zero_second(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(12,0))

    def test_negative_decimal_both(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(-5.12323, -2.34345))

    def test_negative_decimal_first(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(-5.12323, 2.34345))

    def test_negative_decimal_second(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(5.12323, -2.34345))

    def test_positve_decimal_both(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(5.12323, 2.34345))

    def test_positive_decimal_first(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(5.12323, -2.34345))

    def test_positive_decimal_second(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.getEst(-5.12323, 2.34345))

if __name__ == '__main__':
   unittest.main()

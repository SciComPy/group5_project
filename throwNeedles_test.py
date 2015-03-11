#Unit testing for throwNeedles function

from PiSimulation import PiSimulation
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test_negative_large(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.throwNeedles(-245345))

    def test_negative_small(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.throwNeedles(-6))

    def test_negative_one(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.throwNeedles(-1))

    def test_zero(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.throwNeedles(0))

    def test_positive_one(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.throwNeedles(1))

    def test_negative_decimal(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.throwNeedles(-4.545))

    def test_positive_decimal(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.throwNeedles(6.3434))

if __name__ == '__main__':
    unittest.main()

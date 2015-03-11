#Unit testing for estPi function

from PiSimulation import PiSimulation
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test_small_negative_whole_number(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.estPi(-12345,-98765))

    def test_small_negative_decimal_number(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.estPi(-0.12345,-0.98765))
                          
    def test_big_negative_whole_number(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.estPi(-12345947685738456374564564,-98765468449456984576456))

    def test_big_negative_decimal_number(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.estPi(-0.1234557867876867834522345,-0.987657567876898904))

    def test_zero_number(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.estPi(0,0))

    def test_decimal(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.estPi(1234, 0.456))

if __name__ == '__main__':
    unittest.main()

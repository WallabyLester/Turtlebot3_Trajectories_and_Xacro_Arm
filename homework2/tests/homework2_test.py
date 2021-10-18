"""
Tests the python package homework2 calculations 

"""

import unittest
from numpy.testing._private.utils import assert_almost_equal
from homework2.comp_traj import FigureEight
from math import pi, sqrt

class Test_calc(unittest.TestCase):
    """ Runs series of tests on python package calculations
    """
    def __init__(self, *args):
        super(Test_calc, self).__init__(*args)
        W = 4
        H = 2
        self.T = 6
        self.figure_eight = FigureEight(W, H, self.T)

    def test_time_at_zero(self):
        """ Function to check the calculations at time t = 0

        Checks the x, y, xdot, ydot, xddot, yddot, v, and omega calculated values 

        Args: 
            t (time) : 0 

        Returns: 
            Calculated values and test results 
        """
        assert_almost_equal(self.figure_eight.test(0), (0, 0, 2*pi/3, 2*pi/3, 0, 0, 2*sqrt(2)*pi/3, 0), decimal = 2)
        

    def test_time_at_half(self):
        """ Function to check the calculations at half the cycle

        Checks the x, y, xdot, ydot, xddot, yddot, v, and omega calculated values 

        Args: 
            t (time) : T/2 = 3

        Returns: 
            Calculated values and test results 
        """
        assert_almost_equal(self.figure_eight.test(self.T/2), (0, 0, -2*pi/3, 2*pi/3, 0, 0, 2*sqrt(2)*pi/3, 0), decimal = 2)

if __name__ == "__main__":
    import rosunit
    rosunit.unitrun(homework2, 'test_calc', Test_calc)

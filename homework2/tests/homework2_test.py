import unittest
import homework2.comp_traj

class Test_values(unittest.TestCase):
    """ Runs series of tests on python package calculations
    """
    def __init__(self, *args):
        super(Test_values, self).__init__(*args)
        W = 4
        H = 2
        self.T = 6

    def test_1(self):
        self.assertEquals(2,2)


if __name__ == "__main__":
    import rosunit
    rosunit.unitrun(homework2, 'test_1', Test_values)

import unittest

from Stopper import Stopper


class StopperTest(unittest.TestCase):

    def test_stopper_base(self):
        stopper = Stopper()
        stopper.start()
        stopper.stop()
        elapsed_time = stopper.get_elapsed_time()

    def test_elapsed_time_is_integer(self):
        stopper = Stopper()
        elapsed_time = stopper.get_elapsed_time()
        self.assertTrue( isinstance(elapsed_time, int) )
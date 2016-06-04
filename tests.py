import unittest

from Stopper import Stopper


class StopperTest(unittest.TestCase):

    def test_stopper_base(self):
        stopper = Stopper()
        stopper.start()
        stopper.stop()
        elapsed_time = stopper.get_elapsed_time()

import unittest

import time

from Stopper import Stopper


class StopperTest(unittest.TestCase):

    def test_stopper_base(self):
        stopper = Stopper()
        stopper.start()
        stopper.stop()
        elapsed_time = stopper.get_elapsed_sec()

    def test_elapsed_time_is_integer(self):
        stopper = Stopper()
        elapsed_time = stopper.get_elapsed_sec()
        self.assertTrue( isinstance(elapsed_time, int) )

    def test__nostart_nostop__elapsed_0(self):
        stopper = Stopper()
        elapsed_time = stopper.get_elapsed_sec()
        self.assertEqual( elapsed_time, 0)

    def test__nostop__elapsed_0(self):
        stopper = Stopper()
        stopper.start()
        elapsed_time = stopper.get_elapsed_sec()
        self.assertEqual( elapsed_time, 0)

    def test_nostart__elapsed_0(self):
        stopper = Stopper()
        stopper.stop()
        elapsed_time = stopper.get_elapsed_sec()
        self.assertEqual( elapsed_time, 0)

    def test__no_time_between_startstop__elapsed_0sec(self):
        stopper = Stopper()
        stopper.stop()
        self.assertEqual(stopper.get_elapsed_sec(), 0)

    def test__0point5sec_between_startstop__elapsed_1sec(self):
        stopper = Stopper()
        stopper.start()
        time.sleep(0.5)
        stopper.stop()
        self.assertEqual(stopper.get_elapsed_sec(), 1)

    def test__1point5sec_between_startstop__elapsed_2sec(self):
        stopper = Stopper()
        stopper.start()
        time.sleep(1.5)
        stopper.stop()
        self.assertEqual(stopper.get_elapsed_sec(), 2)
import unittest


class Stopper(object):
    def start(self):
        pass

    def stop(self):
        pass

    def get_elapsed_time(self):
        pass


class StopperTest(unittest.TestCase):

    def test_stopper_base(self):
        stopper = Stopper()
        stopper.start()
        stopper.stop()
        elapsed_time = stopper.get_elapsed_time()

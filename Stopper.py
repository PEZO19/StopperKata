import datetime


class Stopper(object):

    def __init__(self):
        self.start_datetime = None
        self.end_datetime = None

    def start(self):
        self.start_datetime = datetime.datetime.now()

    def stop(self):
        self.end_datetime = datetime.datetime.now()

    def get_elapsed_sec(self):
        if self.start_datetime is None or self.end_datetime is None:
            return 0
        else:
            timedelta = self.end_datetime - self.start_datetime
            return timedelta.seconds + 1
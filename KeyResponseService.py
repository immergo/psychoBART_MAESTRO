import sys, time, copy
import psychopy.core
from psychopy.constants import NOT_STARTED
import string, numpy


class KeyResponseService:
    def __init__(self):
        self.status = NOT_STARTED
        self.keys = []  # the key(s) pressed
        self.corr = 0  # was the resp correct this trial? (0=no, 1=yes)
        self.rt = []  # response time(s)
        self.clock = psychopy.core.Clock()  # we'll use this to measure the rt

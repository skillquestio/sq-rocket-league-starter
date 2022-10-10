# This file is for strategy

from util.objects import *
from util.routines import *


class Bot(GoslingAgent):
    def run(self):
        # determines what to do
        self.push(drive(1))

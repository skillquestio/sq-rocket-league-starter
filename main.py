# This file is for strategy

from util.objects import *
from util.routines import *

# Note the line below says GoslingUtils in the videos
# DO NOT change the line below. It's no longer compatible with GoslingUtils so we renamed it.
class Bot(BotCommandAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        # set_intent tells the bot what it's trying to do
        self.set_intent(drive(500))

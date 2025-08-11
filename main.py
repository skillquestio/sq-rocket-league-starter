# This is the main file where you control your bot's strategy

from util.objects import *
from util.routines import *


class Bot(BotCommandAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        # set_intent tells the bot what it's trying to do
        self.set_intent(drive(500))

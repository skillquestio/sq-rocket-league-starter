# This is the main file where you control your bot's strategy

from util.objects import *
from util.routines import *

# Hi! Corbin here. Note the line below says GoslingUtils in the videos.
# DO NOT change the line below. It's no longer compatible with GoslingUtils so we renamed it.
# There are a few places like this where the code that you started with (the code you downloaded) might
# look different than the videos. THAT'S OK! Don't change it. We've made it better over time.
# Just follow along with the videos and it will all work the same.
class Bot(BotCommandAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        # set_intent tells the bot what it's trying to do
        self.set_intent(drive(500))

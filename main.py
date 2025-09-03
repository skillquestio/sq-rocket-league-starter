# This is the main file where you control your bot's strategy

from util.objects import *
from util.routines import *


def run(bot: BotCommandAgent):
    # set_intent tells the bot what it's trying to do
    bot.set_intent(drive(500))

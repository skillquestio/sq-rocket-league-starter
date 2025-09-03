from util.objects import BotCommandAgent
from main import run


class Bot(BotCommandAgent):
    def run(self):
        run(self)

from src.bot.Bot import Bot
from src.symbols.ObjectSymbols import ObjectSymbols

class PythonBot(Bot):

    def __init__(self):
        super().__init__()

    def get_name(self):
        return 'Python'

    def turn(self, game_state, character_state, other_bots):
        super().turn(game_state, character_state, other_bots)
        goal = (1, 5)

        return self.commands.idle()

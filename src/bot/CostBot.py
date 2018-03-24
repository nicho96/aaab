from src.bot.Bot import Bot

class GreedyBot(Bot):

    def __init__(self):
        super().__init__()

    def get_name(self):
        # Find a name for your bot
        return 'TestBot'

    def turn(self, game_state, character_state, other_bots):
        super().turn(game_state, character_state, other_bots)

        start = self.character_state['location']
        goal = self.pathfinder.get_closest_material_goal(start)

        if goal:
            direction = self.pathfinder.get_next_direction(self.character_state['location'], goal)
            if direction:
                return self.commands.move(direction)

        return self.commands.collect()

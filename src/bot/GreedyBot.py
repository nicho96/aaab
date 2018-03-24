from src.bot.Bot import Bot
class GreedyBot(Bot):

    def __init__(self):
        super().__init__()
        self.turn_num = 0

    def get_name(self):
        # Find a name for your bot
        return 'TestBot'

    def turn(self, game_state, character_state, other_bots):
        super().turn(game_state, character_state, other_bots)
        self.turn_num += 1
        distanceToHome = self.pathfinder.get_length_of_path_safe(self.character_state['location'], self.character_state['base'])
        start = self.character_state['location']
        goal = self.pathfinder.get_closest_material_goal_safe(start)

        if 1000 - self.turn_num <= distanceToHome + 1:
            if distanceToHome == 1:
                return self.commands.store()
            else:
                return self.commands.move(self.pathfinder.get_next_direction_safe(self.character_state['location'], self.character_state['base']))

        if goal:
            direction = self.pathfinder.get_next_direction_safe(self.character_state['location'], goal)
            if direction:
                return self.commands.move(direction)



        return self.commands.collect()

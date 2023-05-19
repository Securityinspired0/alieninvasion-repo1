import json

class GameStats():
    """Track Statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Start game in an inactive state
        self.game_active = False

        #High score should never be reset.
        self.high_score = self.get_saved_high_score()


    def get_saved_high_score(self):
        """Get high score from file if it exists."""
        try:
            with open('high_score.json') as f:
                self.high_score = json.load(f)
                return json.load(f)
        except FileNotFoundError:
            self.high_score = 0
            return 0


    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 0
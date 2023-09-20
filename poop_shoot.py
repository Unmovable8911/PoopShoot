import pygame, sys
from settings import Settings
from start import StartPage
from playing import PlayingPage
from pause import PausePage
from exi1 import ExitPage

class PoopShoot:
    """The overall class of the game"""
    def __init__(self):
        """Create incidences and initiallize game elements"""
        pygame.init()
        self.settings = Settings()
        self.state = self.GameStates()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height
        pygame.display.set_caption('Poop Shoot')
        self.start_page = StartPage(self)
        self.playing_page = PlayingPage(self)
        self.pause_page = PausePage(self)
        self.exit_page = ExitPage(self)

    def _check_events(self):
        """Check mouse and keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif self.state.game_state == 0:
                self.start_page.respond_events(event)
            elif self.state.game_state == 1:
                self.playing_page.respond_events(event)
            elif self.state.game_state == -1:
                self.pause_page.respond_events(event)
            elif self.state.game_state == 2:
                self.exit_page.respond_events(event)

    def run(self):
        """Run the game"""
        while True:
            self._check_events()
            if self.state.game_state == 0:
                # When the game is inactive, start page
                self.start_page.draw()
            elif self.state.game_state == 1:
                # When the game is active, playing screen
                self.playing_page.draw()
            elif self.state.game_state == -1:
                # When the user pauses the game, Pause page
                self.pause_page.draw()
            elif self.state.game_state == 2:
                self.exit_page.draw()
            pygame.display.flip()
    
    class GameStates:
        """Manipulate the scoring system"""
        def __init__(self):
            self.game_state = 0 # 0 represents inactive, 1 represents active, and -1 represents pause
            self.score = 0
            self.life = 3
        
        def add_score(self):
            self.score += 10
        
        def loose_life(self):
            self.life -= 1

if __name__ == "__main__":
    poop_shoot = PoopShoot()
    poop_shoot.run()
import pygame
from lib.button import Button

class StartPage:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.game = game
        # Load background image
        self.img = pygame.image.load('images/start_page.bmp')
        # Rescale the image
        self.img = pygame.transform.scale(self.img, self.screen_rect.size)
        self.rect = self.img.get_rect()
        # Create buttons
        self.start_button = Button('start')
        self.exit_button = Button('exit')
        # Set the position of the buttons
        self.start_button.set_rect(self.screen_rect, 0)
        self.exit_button.set_rect(self.screen_rect, 1)
    
    def respond_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.is_active:
                self.game.state.game_state = 1
            elif self.exit_button.is_active:
                self.game.state.game_state = 2

    def draw(self):
        self.screen.blit(self.img, (0, 0))
        self.start_button.draw(self.screen)
        self.exit_button.draw(self.screen)
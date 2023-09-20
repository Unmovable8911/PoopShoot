import pygame
from lib.button import Button

class PausePage:
    def __init__(self, game):
        self.game = game
        self.img = pygame.image.load('images/pause_page.bmp')
        self.img = pygame.transform.scale(self.img, self.game.screen_rect.size)
        
        self.resume_button = Button('resume')
        self.quit_button = Button('quit')
        self.resume_button.set_rect(game.screen_rect, 0)
        self.quit_button.set_rect(game.screen_rect, 1)
    
    def respond_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.state.game_state = 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.resume_button.is_active:
                self.game.state.game_state = 1
            elif self.quit_button.is_active:
                self.game.playing_page.ass.initiallize_state()
                self.game.playing_page.faces.empty()
                self.game.settings.initiallize()
                self.game.state.game_state = 0

    def draw(self):
        self.game.screen.blit(self.img, (0, 0))
        self.resume_button.draw(self.game.screen)
        self.quit_button.draw(self.game.screen)
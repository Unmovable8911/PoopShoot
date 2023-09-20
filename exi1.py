import pygame, sys
from lib.button import Button

class ExitPage:
    def __init__(self, game):
        self.game = game
        self.title = pygame.image.load('images/title.bmp')
        self.space = pygame.image.load('images/space.bmp')
        self.width = self.game.screen_width / 3
        self.title_height = self.title.get_rect().height / self.title.get_rect().width * self.width
        self.space_height = self.space.get_rect().height / self.space.get_rect().width * self.width
        self.title = pygame.transform.scale(self.title, (self.width, self.title_height))
        self.space = pygame.transform.scale(self.space, (self.width, self.space_height))
        self.title_rect = self.title.get_rect()
        self.space_rect = self.space.get_rect()
        self.title_rect.center = self.game.screen_rect.center
        self.title_rect.y -= ((self.title_height + self.space_height) / 2) - (self.title_height / 2)
        self.space_rect.midtop = self.title_rect.midbottom

        self.yes = Button('yes')
        self.no = Button('no')
        self.yes.set_rect(self.game.screen_rect, 0, 10)
        self.no.set_rect(self.game.screen_rect, 0, 10)
        self.yes.rect.center = self.no.rect.center = self.space_rect.center
        self.yes.rect.x -= self.yes.width * 0.7
        self.no.rect.x += self.no.width * 0.7
    
    def respond_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.yes.is_active:
                sys.exit()
            elif self.no.is_active:
                self.game.state.game_state = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.state.game_state = 0
    
    def draw(self):
        self.game.screen.blit(self.title, self.title_rect)
        self.game.screen.blit(self.space, self.space_rect)
        self.yes.draw(self.game.screen)
        self.no.draw(self.game.screen)
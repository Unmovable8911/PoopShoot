import pygame

class ScoreBoard:
    def __init__(self, game):
        self.game = game
        self.bg = pygame.Rect(0, 0, self.game.screen_width, self.game.screen_height / 11)

        self.ass = pygame.image.load('images/ass.bmp')
        self.ass_height = self.bg.height * 0.7
        self.ass_width = self.ass.get_rect().width / self.ass.get_rect().height * self.ass_height
        self.ass = pygame.transform.scale(self.ass, (self.ass_width, self.ass_height))
        self.ass_rect = self.ass.get_rect()
        self.ass_rect.bottomleft = self.bg.bottomleft

        self.font = pygame.font.SysFont(None, 50)
        self.update_score()
    
    def update_score(self):
        self.score = self.font.render(str(self.game.state.score), True, self.game.settings.text_color, 
                                      self.game.settings.sb_color)
        self.score_rect = self.score.get_rect()
        self.score_rect.midright = self.bg.midright
    
    def draw(self):
        self.game.screen.fill(self.game.settings.sb_color, self.bg)
        for n in range(self.game.state.life):
            ass = self.ass.copy()
            ass_rect = ass.get_rect()
            ass_rect.x += n * 1.2 * ass_rect.width
            self.game.screen.blit(ass, ass_rect)
        self.update_score()
        self.game.screen.blit(self.score, self.score_rect)
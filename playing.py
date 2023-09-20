import pygame
from lib.ass import Ass
from lib.face import Face
from lib.score_board import ScoreBoard

class PlayingPage:
    """Controls the game when it is in playing state"""
    def __init__(self, game):
        self.game = game
        self.ass = Ass(game)
        self.faces = pygame.sprite.Group()
        self.sb = ScoreBoard(game)
    
    def respond_events(self, event):
        if event.type == pygame.KEYDOWN:
            self._respond_keydown(event)
        elif event.type == pygame.KEYUP:
            self._respond_keyup(event)
    
    def _respond_keydown(self, event):
        if event.key == pygame.K_a:
            self.ass.move_left = True
        if event.key == pygame.K_d:
            self.ass.move_right = True
        if event.key == pygame.K_SPACE:
            self.ass.keep_shooting = True
        if event.key == pygame.K_ESCAPE:
            self.game.state.game_state = -1
            self.ass.set_movements_false()
    
    def _respond_keyup(self, event):
        if event.key == pygame.K_a:
            self.ass.move_left = False
        if event.key == pygame.K_d:
            self.ass.move_right = False
        if event.key == pygame.K_SPACE:
            self.ass.keep_shooting = False
    
    def _update_faces(self):
        charge = False
        try:
            previouse_face_top = self.faces.sprites()[-1].rect.top
        except IndexError:
            charge = True
        else:
            charge = previouse_face_top > self.game.settings.face_distance
        if charge:
            self.faces.add(Face(self.game))
        self.faces.update()
    
    def _check_collision(self):
        shot_face = pygame.sprite.groupcollide(self.faces, self.ass.poops, True, True)
        if shot_face:
            self.game.state.add_score()
    
    def draw(self):
        self.ass.update()
        self._update_faces()
        self._check_collision()
        self.game.screen.fill(self.game.settings.background_color)
        self.ass.draw()
        self.faces.draw(self.game.screen)
        self.sb.draw()
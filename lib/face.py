import pygame, random
from pygame.sprite import Sprite

class Face(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('images/face.bmp')
        self.rect = self.image.get_rect()
        self.width = self.game.screen_width / 15
        self.height = self.rect.height / self.rect.width * self.width
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        
        # The face will apear at a random position of the top of the screen
        self.rect.bottom = self.game.screen_rect.top
        self.random_x_position = random.randint(0, int(self.game.screen_width - self.width))
        self.rect.x = self.random_x_position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.x_direction = random.choice((1, -1)) # 1 stands for right, -1 stands for left
        self.x_speed = self.game.screen_width / self.game.settings.face_x_speed
        self.y_speed = self.game.screen_height / self.game.settings.face_y_speed
    
    def update(self) -> None:
        if self.rect.left <= 0:
            self.x_direction = 1
        elif self.rect.right >= self.game.screen_width:
            self.x_direction = -1
        self.y += self.y_speed
        self.x += self.x_speed * self.x_direction
        self.rect.x = self.x
        self.rect.y = self.y
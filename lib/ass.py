import pygame
from pygame.sprite import Sprite

class Ass:
    """Manipulate the Ass behavior"""
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.screen_width = game.screen_width # Used to calculate the size and move speed of the ass
        self.screen_height = game.screen_height # Used to calculate the move speed of the poop

        self.source_img = pygame.image.load('images/ass.bmp') # Load the image
        self.img_rect = self.source_img.get_rect()
        self.img_height = self.img_rect.height
        self.img_width = self.img_rect.width
        del self.img_rect
        self.initiallize_state()
    
    def initiallize_state(self):
        # Change the image size based on the screen size
        self.width = self.screen_width / 10
        self.height = self.img_height / self.img_width * self.width
        self.img = pygame.transform.scale(self.source_img, (self.width, self.height))
        self.rect = self.img.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom # Put the ass at the middle bottom of the screen
        self.speed = self.screen_width / self.settings.ass_speed
        self.x = float(self.rect.x)
        self.poops = pygame.sprite.Group()
        self.set_movements_false()
    
    def set_movements_false(self):
        self.move_left = False
        self.move_right = False
        self.keep_shooting = False

    def update(self):
        """Update the speed and the position of the ass and poop"""
        self.speed = self.screen_width / self.settings.ass_speed # Constantly updating the speed of the ass
        if self.move_left and self.rect.left > 0:
            self.x -= self.speed
        if self.move_right and self.rect.right < self.screen_width:
            self.x += self.speed
        self.rect.x = self.x
        self._update_poops()
    
    def _update_poops(self):
        """Shoot poop when player press SPACE
        And constantly updating the speed, distance and position of poop"""
        try:
            previouse_poop_bottom = self.poops.sprites()[-1].rect.bottom
        except IndexError: # when there's no poop on the screen
            shootable = True
        else: # when there's already some poop on the screen
            shootable = (previouse_poop_bottom + self.settings.poop_distance) < self.rect.y
        if self.keep_shooting and shootable:
            self.poops.add(self.Poop(self))
        for poop in self.poops.copy().sprites():
            if poop.rect.bottom < 0:
                self.poops.remove(poop)
        self.poops.update()

    def draw(self):
        """Draw the ass and poops onto the screen"""
        self.screen.blit(self.img, self.rect)
        self.poops.draw(self.screen)
    
    class Poop(Sprite):
        """Controls how bullets behaves"""
        def __init__(self, ass):
            super().__init__()
            self.settings = ass.settings
            self.screen_height = ass.screen_height
            self.src_img = pygame.image.load('images/poop.bmp')
            self.img_rect = self.src_img.get_rect()
            self.img_height = self.img_rect.height
            self.img_width = self.img_rect.width
            # Calculate the appropriate size of the poop image, and resize the image to fit the size of the ass
            self.width = ass.width / 4
            self.height = ass.height / ass.width * self.width
            self.image = pygame.transform.scale(self.src_img, (self.width, self.height))

            del self.src_img, self.img_rect, self.img_height, self.img_width # free up memory

            self.rect = self.image.get_rect()
            self.rect.midleft = ass.rect.midleft
            self.y = float(self.rect.y)
            self.speed = self.screen_height / self.settings.poop_speed
        
        def update(self):
            """Update the position and speed of the poop"""
            self.speed = self.screen_height / self.settings.poop_speed
            self.y -= self.speed
            self.rect.y = self.y

import pygame

class Button:
    def __init__(self, name):
        path = 'images/buttons/'
        button_path = f'{path}{name}.bmp'
        acti_button_path = f'{path}{name}_acti.bmp'
        self.img = pygame.image.load(button_path)
        self.acti_img = pygame.image.load(acti_button_path)
        self.rect = self.img.get_rect()
        self.is_active = False

    def check_mouse_over(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.is_active = True
        else:
            self.is_active = False
    
    def set_rect(self, screen_rect, number, size = 8):
        """scale the image, and set its rectangle value
        ;screen_rect: the game screen
        ;number: move the button down number of levels"""
        self.width = screen_rect.width / size
        self.height = self.rect.height / self.rect.width * self.width
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.acti_img = pygame.transform.scale(self.acti_img, (self.width, self.height))

        self.rect = self.img.get_rect()
        self.rect.center = screen_rect.center

        self.rect.y += number * 1.5 * self.height

    def draw(self, screen):
        self.check_mouse_over()
        if self.is_active:
            screen.blit(self.acti_img, self.rect)
        else:
            screen.blit(self.img, self.rect)
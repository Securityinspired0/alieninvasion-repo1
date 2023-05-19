import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the screen and set the starting point"""
        super(Ship, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        #load the ship image and get its rect
        self.image = pygame.image.load('C:/Users/USER/Documents/Python/Alien_Invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)

        #Moving to left and right
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Updating ship postion based on movement flag"""
        #Update the ship center value no rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor

        #Update rect object from self.center
        self.rect.centerx = self.centerx

    def blitme(self):
        """Draw the sip at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx
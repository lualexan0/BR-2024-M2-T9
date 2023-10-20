import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite): # herdarança sprites: metodos e atributos
    def __init__(self, image, type):
        self.type = type # tipo de imagens
        self.image = image
        self.rect = self.image[self.type].get_rect() # a dimensão da imagem e seu tipo
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))
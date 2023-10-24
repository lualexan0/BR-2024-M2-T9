import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH # importar a tela


class Obstacle(Sprite): 
    def __init__(self, image, type):
       self.image = image 
       self.type = type #é o indice das nossas imgens de cacto
       self.rect = self.image[self.type].get_rect() # dimensão da nossa imagem
       self.rect.x = SCREEN_WIDTH #aparecer os obstaculos no final da tela

    def update(self, game_speed, obstacles): # aqui vai ser quase igual ao background, movendo os objetos com a velocidade do jogo
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width: # se o obstaculo andou toda a nossa tela
            obstacles.pop()# retira a ultima unidade
    # no momemnto em que o objeto percorrer a nossa tela todo ele sera retirado
    # e a velocidade do jogo, que sera menos 20 pra locomover a os obstaculos, da direita pra esquerda
    def draw(self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))
        #o blit novamente colocando ordem no que vai ser desenhado primeiro
    
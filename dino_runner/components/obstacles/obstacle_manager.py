import pygame
import random # importei

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
#importando as duas classes

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game): # aqui a lista de obstuclos e seu tipo
        obstacle_type = [
            Cactus(),
            Bird(),
        ]

        if len(self.obstacles) == 0: # se minha lista esta vazia

         self.obstacles.append(obstacle_type[random.randint(0,1)]) # ele adiciona o tipo de obstaculo de forma randomica  

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
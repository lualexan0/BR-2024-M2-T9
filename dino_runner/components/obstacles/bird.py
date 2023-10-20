import random

from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD, 0) # herança
        self.rect.y = random.randint(200,300) #alterna entre as posiçoes, verticais
        self.step_index = 0 # mudarmos a posição de forma dinamica

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect) # divisão do step index: de 0 a 4 o retorno sera 0, e de 5 a 9 vai ser 1
        self.step_index += 1

        if self.step_index >= 9: # aqui ele nao pode chegar a 10 pq retornaria dois e so temos de 0 a 1
            self.step_index = 0 # aqui zera
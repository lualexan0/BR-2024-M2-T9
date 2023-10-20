import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS

#minha lista de cacto
CACTUS = [
   (LARGE_CACTUS, 300),# aqui mudamos a posiçaõ
   (SMALL_CACTUS, 325),
]

class Cactus(Obstacle):
    def __init__(self):
      image, cactus_pos = CACTUS[random.randint(0, 1)] # aqui temos a forma aleatoria de cacto que ira vir
      self.type = random.randint(0, 2) # aqui é o tipo do cacto pq ele tem 3
      super().__init__(image, self.type) # herança
      self.rect.y = cactus_pos #aqui fica dinamico se for o lage e posiçao e uma e se for o small e outra
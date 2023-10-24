import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS

CACTUS = [
   (LARGE_CACTUS, 300), #
   (SMALL_CACTUS, 325), # aqui é como se fosse a imagem do dino duck, pq precisamos posicionar a imagem diferente
]


class Cactus(Obstacle):# herda os componetes do obstacle
    def __init__(self):
      image, cactus_pos = CACTUS[random.randint(0, 1)]# ele pega entre o large e o smal cactos de forma aleatoria
      self.type = random.randint(0, 2) # e o tipo de cacto
      super().__init__(image, self.type)# super e como se tivessemos acessando os componetes que sao imagens e tipo do obstacle
      self.rect.y = cactus_pos # aqui fica dimanimico pra encaixar na tela

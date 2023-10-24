from dino_runner.utils.constants import FLYING, FLYING_TYPE 
from dino_runner.components.power_ups.power_up import PowerUp 


#
class Flying (PowerUp):
    def __init__(self):
        self.image = FLYING
        self.type = FLYING_TYPE 
        super().__init__(self.image, self.type)

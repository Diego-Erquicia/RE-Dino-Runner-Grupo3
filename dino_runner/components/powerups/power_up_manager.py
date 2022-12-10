import pygame
from random import randint
from dino_runner.components.obstacles.shield import Shield
from dino_runner.components.obstacles.hammer import Hammer
from dino_runner.utils.constants import HAMMER_TYPE, SHIELD_TYPE


class PowerUpManager ():
    def __init__ (self):
        self.power_ups = []
        self.when_appears = 0
        self.hammer_appears = 0
        self.increment = 0
    
    def generate_power_up (self, score):
        if len (self.power_ups) == 0 and self.when_appears + self.increment == score:
               self.power_ups.append(Shield())
        elif len (self.power_ups) == 0 and self.hammer_appears + self.increment == score:
               self.power_ups.append(Hammer())

    def update (self, game_speed, player, score):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                if power_up == SHIELD_TYPE:
                   power_up.start_time = pygame.time.get_ticks()
                   player.on_pick_power_up(power_up.start_time, power_up.duration, power_up.type)
                   self.power_ups.remove(power_up)
                   self.increment = randint(1, 500)
                elif power_up == HAMMER_TYPE:
                   power_up.start_time = pygame.time.get_ticks()
                   power_up.duration = 10
                   player.on_pick_power_up(power_up.start_time, power_up.duration, power_up.type)
                   self.power_ups.remove(power_up)
                   self.increment = randint(1, 500)
                   


    def draw (self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
        
    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = randint(200, 300)
        self.hammer_appears = randint(500, 700)
        self.increment = 0
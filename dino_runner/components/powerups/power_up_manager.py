from random import randint
import random

import pygame
from dino_runner.components.obstacles.hammer import Hammer
from dino_runner.components.obstacles.shield import Shield


class PowerUpManager ():
    def __init__ (self):
        self.power_ups = []
        self.when_appears = 0
        self.increment = 0
    
    def generate_power_up (self, score):
        if len (self.power_ups) == 0 and self.when_appears + self.increment == score:
            if random.randint(0,1)==0:
               self.power_ups.append(Shield())
            elif random.randint(0,1)==1:
               self.power_ups.append(Hammer())

    def update (self, game_speed, player, score):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.on_pick_power_up(power_up.start_time, power_up.duration, power_up.type)
                self.power_ups.remove(power_up)
                self.increment += 500
            elif not player.dino_rect.colliderect(power_up.rect):
                self.increment += 1000

    def draw (self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
        
    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = randint(200, 300)
        self.increment = 0
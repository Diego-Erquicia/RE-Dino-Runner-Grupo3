import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update (self, game):
        if len(self.obstacles) == 0:
            if random.randint(0,1) == 0:
                cactus_type = "SMALL"
            else:
                cactus_type = "LARGE"
            self.obstacles.append (Cactus(cactus_type))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                if game.on_death():
                    self.obstacles.remove(obstacle)
                else:
                #game.playing = False

                    break

    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []

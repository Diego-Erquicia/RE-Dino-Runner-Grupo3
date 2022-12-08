import pygame
from dino_runner.components.obstacles.obstacle import Obstacle

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class DeathCount:
    def __init__(self):
        self.death_count = 0

    def update (self, game):
        if game.player.dino_rect.colliderect(Obstacle.rect):
            pygame.time.delay(2000)
            death_count += 1

    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, 22)
        text_component = font.render(f"Number of deaths: {self.death_count}", True, (0,0,0))
        text_rect = text_component.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        screen.blit(text_component, text_rect)
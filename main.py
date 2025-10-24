import pygame
import sys
import time

FRAMES_PER_SECOND = 30
clock = pygame.time.Clock()

pygame.init()
window = pygame.display.set_mode((600, 600))
icon = pygame.image.load("img/icon.jpeg")
pygame.display.set_caption("Untitled")
pygame.display.set_icon(icon)

flag = True

while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        
    window.fill((0, 200, 255))

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)

pygame.quit()
sys.exit()
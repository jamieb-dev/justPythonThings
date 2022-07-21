import pygame
import os 
import random
import time
pygame.font.init()

WIDTH, HEIGHT = 1000, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load images
RED_SPACESHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
BLUE_SPACESHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SPACESHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))

# Player ship
YELLOW_SPACESHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    level = 1
    lives = 3
    mainFont = pygame.font.SysFont("comicsans", 50)

    def redrawWindow():
        WIN.blit(BG, (0,0))
        # draw text
        livesLabel = mainFont.render(f"Lives: {lives}", 1,(255, 255, 255))
        levelsLabel = mainFont.render(f"Level: {level}", 1, (255,255,255))
        pygame.display.update()
        

    while run:
        clock.tick(FPS)
        redrawWindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
main()
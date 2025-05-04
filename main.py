import pygame
from sys import exit

pygame.init()

pygame.display.set_caption("Runner")
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
screen.fill("Purple")
clock = pygame.time.Clock()


font = pygame.font.Font("assets/font/SYNNova-Normal.otf", 25)

background_rain = pygame.image.load("assets/background/background_rain.png")
background_rain = pygame.transform.scale(background_rain, (width, height))

road = pygame.image.load("assets/background/road.png")
road = pygame.transform.scale(road, (800, 80))

text = font.render("Score", 1, "Green" )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_rain, (0, 0))
    screen.blit(road,(0, 320))
    screen.blit(text, (0, 0))

    pygame.display.update()
    clock.tick(60)





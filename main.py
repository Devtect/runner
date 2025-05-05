import pygame
from sys import exit

pygame.init()

pygame.display.set_caption("Runner")
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


font = pygame.font.Font("assets/font/SYNNova-Normal.otf", 25)

background_rain = pygame.image.load("assets/background/background_rain.png").convert()
background_rain = pygame.transform.scale(background_rain, (width, height))

road = pygame.image.load("assets/background/road.png").convert()
road = pygame.transform.scale(road, (800, 80))

enemy = pygame.image.load("assets/sprites/enemy.png").convert_alpha()
enemy = pygame.transform.scale(enemy, (80, 55))
enemy_rect = enemy.get_rect(topleft = (700,320))


player = pygame.image.load("assets/sprites/player.png").convert_alpha()
player = pygame.transform.scale(player, (120, 120))
player_rect = player.get_rect(midleft=(0, 320))

text = font.render("Score", 1, "Green" )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_rain, (0, 0))
    screen.blit(road,(0, 320))
    screen.blit(text, (0, 0))
    enemy_rect.right -= 3
    if enemy_rect.right <= 0: enemy_rect.left = 800
    screen.blit(enemy, enemy_rect)
    screen.blit(player, player_rect)

    pygame.display.update()
    clock.tick(60)
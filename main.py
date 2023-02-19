import pygame
from game_object import *

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ping-pong")

def run():
    game = True
    clock = pygame.time.Clock()
    player1 = Board(15, 250, 20, 100, None, 5)


    while game:
        window.fill((0,0,0))
        pygame.draw.rect(window, (255, 0, 0), player1)
        player1.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1.MOVE["UP"] = True
                if event.key == pygame.K_s:
                    player1.MOVE["DOWN"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player1.MOVE["UP"] = False
                if event.key == pygame.K_s:
                    player1.MOVE["DOWN"] = False
        
        clock.tick(60)
        pygame.display.flip()

run()
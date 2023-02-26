import pygame
from game_object import *
from data import *


pygame.init()

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("ping-pong")

def run():
    game = True
    clock = pygame.time.Clock()
    player_left = Board(15, 250, 20, 500, None, 7)
    player_right = Board(setting_win["WIDTH"] - 20 - 15, 250, 20, 500, None, 7)
    ball = Ball(setting_win["WIDTH"] // 2, setting_win["HEIGHT"] // 2, 20, (0, 255, 0), None, 5)


    while game:
        window.fill((0,0,0))
        pygame.draw.rect(window, (255, 0, 0), player_left)
        pygame.draw.rect(window, (255, 0, 0), player_right)
        pygame.draw.circle(window, ball.COLOR, (ball.X, ball.Y), ball.RADIUS)

        if ball.DIRECTION:
            ball.move(player_left)
        else:
            ball.move(player_right)
        #sball.move(player_left, player_right)


        player_left.move()
        player_right.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player_left.MOVE["UP"] = True
                if event.key == pygame.K_s:
                    player_left.MOVE["DOWN"] = True
                if event.key == pygame.K_UP:
                    player_right.MOVE["UP"] = True
                if event.key == pygame.K_DOWN:
                    player_right.MOVE["DOWN"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player_left.MOVE["UP"] = False
                if event.key == pygame.K_s:
                    player_left.MOVE["DOWN"] = False
                if event.key == pygame.K_UP:
                    player_right.MOVE["UP"] = False
                if event.key == pygame.K_DOWN:
                    player_right.MOVE["DOWN"] = False
        
        clock.tick(60)
        pygame.display.flip()

run()
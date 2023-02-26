import pygame
from data import *
from random import choice, uniform


class Board(pygame.Rect):
    def __init__(self, x, y, width, height, image, speed):
        super().__init__(x, y, width, height)
        self.IMAGE = image
        self.SPEED = speed
        self.MOVE = {"UP": False, "DOWN": False}
    
    def move(self):
        if self.MOVE["UP"] and self.y > 0:
            self.y -= self.SPEED
        elif self.MOVE["DOWN"] and self.y < 500:
            self.y += self.SPEED

class Ball():
    def __init__(self, x, y, radius, color, image, speed):
        self.X = x
        self.Y = y
        self.RADIUS = radius
        self.COLOR = color
        self.IMAGE = image
        self.SPEED = speed
        self.ANGLE = choice([-self.SPEED, self.SPEED])
        self.VERTICAL = 0
        self.DIRECTION = True if self.ANGLE < 0 else False
    
    def move(self, board):
        
        if self.Y - self.RADIUS <= 0 or self.Y + self.RADIUS >= setting_win["HEIGHT"]:
            self.VERTICAL *= -1
        elif board.collidepoint(self.X - self.RADIUS, self.Y) or board.collidepoint(self.X + self.RADIUS, self.Y):
            if board.MOVE["UP"]:
                self.VERTICAL = - uniform(self.SPEED // 2, self.SPEED)
            elif board.MOVE["DOWN"]:
                self.VERTICAL = uniform(self.SPEED // 2, self.SPEED)
            self.ANGLE *= -1
            self.DIRECTION = not self.DIRECTION

        self.X += self.ANGLE
        self.Y += self.VERTICAL
        print((self.ANGLE ** 2 + self.VERTICAL ** 2) ** 0.5)
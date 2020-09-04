import pygame
class Player():
    def __init__(self, x, y, width, height, color, vel):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.vel = vel
        self.rect = (self.x, self.y, self.width, self.height)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y - self.vel > 0:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y + self.vel + self.height < 500:
            self.y += self.vel
        if keys[pygame.K_LEFT] and self.x - self.vel > 0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x + self.vel + self.width < 500:
            self.x += self.vel
        self.update()
    
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

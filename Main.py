import Player
import pygame
pygame.init()
screen_size = (600,600)
screen = pygame.display.set_mode(screen_size)
pl_color = (0,0,255)
pl_size = [40,40,100,60]
pygame.display.set_caption("My game")

pl = Player.Player(screen,pl_color,pl_size)
run = True
while run:
    pl.main()
    pygame.display.flip()
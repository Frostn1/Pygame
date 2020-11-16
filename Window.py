import pygame
import Player

class Window:
    def __init__(self,width,height,title):
        pygame.init()
        self.players = []
        self.setSize(width,height)
        self.setTitle(title)

    def setSize(self,width, height):
        self.size = width,height
        self.screen =  pygame.display.set_mode(self.size)

    def setTitle(self,title):
        self.title = title
        pygame.display.set_caption(self.title)


    def createPlayer(self,color,size,auto):
        self.players.append(Player.Player(self.screen,color,size,auto))

    def run(self):
        for pl in self.players:
            pl.main()
        pygame.display.flip()

        
import pygame
import random

BLACK = (0,0,0)
keys = ["RIGHTUP","RIGHTDOWN","LEFTUP","LEFTDOWN"]
COLOR_NAMES = ["RED","GREEN","BLUE","WHITE"]
COLORS = {"BLUE":(0,0,255),"RED":(255,0,0),"GREEN":(0,255,0),"WHITE":(255,255,255)}

class Player:
    def __init__(self,screen,color,size,auto):
        
        #< General >
        self.screen = screen
        self.color = color
        self.size = size
        self.font = pygame.font.SysFont('Arial', 25)

        #< Shapes >
        self.screen.blit(self.font.render('VOD', True, (255,0,0)), (200, 100))
        self.rect = pygame.draw.rect(self.screen,self.color,pygame.Rect(self.size[0],self.size[1],self.size[2],self.size[3]))


        
        #< Flags >
        self.auto = auto
        self.curr_dir = random.choice(keys)
        self.vel = 0.025

        
        
        
    

    def main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
        if not self.auto:
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_RIGHT]:
                
                self.move("RIGHT")
            if self.keys[pygame.K_LEFT]:
                
                self.move("LEFT")
            if self.keys[pygame.K_UP]:
                
                self.move("UP")
            if self.keys[pygame.K_DOWN]:
                
                self.move("DOWN")

        # { Auto Def}
        else:
            self.move(self.curr_dir)


        self.screen.fill(BLACK)
        
        
        self.rect_temp = pygame.Rect(self.size[0], self.size[1], self.size[2],self.size[3])
        
        self.circle = pygame.draw.ellipse(self.screen, self.color, self.rect_temp)
        self.screen.blit(self.font.render('VOD', True, (0,0,0)), (self.size[0]+self.size[2]/3,self.size[1]+self.size[3]/3))
    def move(self,arg):
        
        if "RIGHT" in arg and not self.size[0] + self.vel + self.size[2] > self.screen.get_size()[0]:
            self.size[0] += self.vel * random.randint(random.randint(1,4),7)
            
        if "LEFT" in arg and self.size[0] - self.vel  > 0:
            self.size[0] -= self.vel* random.randint(random.randint(1,4),7)
           
        if "UP" in arg and self.size[1] - self.vel > 0:
            self.size[1] -= self.vel* random.randint(random.randint(1,4),7)
            
        if "DOWN" in arg and not self.size[1] + self.vel + self.size[3] > self.screen.get_size()[1]:  
            self.size[1] += self.vel* random.randint(random.randint(1,4),7)
    

        if "RIGHT" in arg and self.size[0] + self.vel + self.size[2] > self.screen.get_size()[0]:
            self.color = COLORS[random.choice(COLOR_NAMES)]
            self.change_dir()
        elif "LEFT" in arg and not self.size[0] - self.vel  > 0:

            self.color = COLORS[random.choice(COLOR_NAMES)]
            self.change_dir()
        elif "UP" in arg and not self.size[1] - self.vel > 0:
            self.color = COLORS[random.choice(COLOR_NAMES)]
            self.change_dir()
        
        elif "DOWN" in arg and self.size[1] + self.vel + self.size[3] > self.screen.get_size()[1]:  
            self.color = COLORS[random.choice(COLOR_NAMES)]
            self.change_dir()

    def change_dir(self):
        if self.auto:
            self.curr_dir = random.choice(keys)
            
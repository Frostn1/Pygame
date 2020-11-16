import pygame
import random
import keyboard

keys = ["R","L","U","D"]
#,"RU","RD","LU","LD"]

keys_dict = {"R":lambda:keyboard.press("right"),"L":lambda:keyboard.press("left"),"U":lambda:keyboard.press("up"),"D":lambda:keyboard.press("down")}
#,"RU","RD","LU","LD"}
BLACK = (0,0,0)
COLOR_NAMES = ["RED","GREEN","BLUE","WHITE"]
COLORS = {"BLUE":(0,0,255),"RED":(255,0,0),"GREEN":(0,255,0),"WHITE":(255,255,255)}
class Player:
    def __init__(self,screen,color,size):
        self.screen = screen
        self.color = color
        self.size = size
        self.font = pygame.font.SysFont('Arial', 25)
        ################
        self.screen.blit(self.font.render('Hello!', True, (255,0,0)), (200, 100))
        print(self.size)
        self.rect = pygame.draw.rect(self.screen,self.color,pygame.Rect(self.size[0],self.size[1],self.size[2],self.size[3]))
        self.vel = 1
        
        ###############
        #self.keys = pygame.key.get_pressed()
        
    

    def main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_RIGHT]:
            #print("Right")
            self.move("RIGHT")
        if self.keys[pygame.K_LEFT]:
            #print("Left")
            self.move("LEFT")
        if self.keys[pygame.K_UP]:
            #print("Up")
            self.move("UP")
        if self.keys[pygame.K_DOWN]:
            #print("Down")
            self.move("DOWN")

        self.screen.fill(BLACK)
        
        #self.rect = pygame.draw.rect(self.screen,self.color,pygame.Rect(self.size[0],self.size[1],self.size[2],self.size[3]))
        self.rect_temp = pygame.Rect(self.size[0], self.size[1], self.size[2],self.size[3])
        #self.circle = pygame.draw.circle(self.screen, self.color, (self.size[0], self.size[1]), self.size[2])
        self.circle = pygame.draw.ellipse(self.screen, self.color, self.rect_temp)
        self.screen.blit(self.font.render('VOD', True, (0,0,0)), (self.size[0]+self.size[2]/3,self.size[1]+self.size[3]/3))
    def move(self,arg):
        #print(arg == "RIGHT",(self.size[0] + self.vel) > self.screen.get_size()[0],self.size[0],self.vel,self.screen.get_size()[0])
        if arg == "RIGHT" and not self.size[0] + self.vel + self.size[2] > self.screen.get_size()[0]:
            self.size[0] += self.vel 
            
        elif arg == "LEFT" and self.size[0] - self.vel  > 0:
            self.size[0] -= self.vel
            
        elif arg == "UP" and self.size[1] - self.vel > 0:
            self.size[1] -= self.vel
            
        elif arg == "DOWN" and not self.size[1] + self.vel + self.size[3] > self.screen.get_size()[1]:  
            self.size[1] += self.vel


        if arg == "RIGHT" and self.size[0] + self.vel + self.size[2] > self.screen.get_size()[0]:
            self.color = COLORS[random.choice(COLOR_NAMES)]
            self.change_dir()
        elif arg == "LEFT" and not self.size[0] - self.vel  > 0:
            self.color = COLORS[random.choice(COLOR_NAMES)]
            self.change_dir()
        elif arg == "UP" and not self.size[1] - self.vel > 0:
            self.color = COLORS[random.choice(COLOR_NAMES)]
            self.change_dir()
        
        elif arg == "DOWN" and self.size[1] + self.vel + self.size[3] > self.screen.get_size()[1]:  
            self.color = COLORS[random.choice(COLOR_NAMES)]
            self.change_dir()
    def change_dir(self):
        print("Yap")
        keyboard.unhook_all()
        #keys_dict[random.choice(keys)]()
       #print(keyboard.keys())
        keyboard.send("right arrow")
        if keyboard.is_pressed("right"):
            print("WHATTATTTTTTTTTTTTTTTTTTT")
        


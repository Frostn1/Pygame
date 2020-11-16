import pygame
pygame.init()
background_colour = (255,0,0)
size = (400,600)
screen = pygame.display.set_mode(size)#Set window
pygame.display.set_caption("Game")#Title
# screen.fill(background_colour)#Backgroung color
# pygame.display.flip()#Update screen
background_colour = (0,255,0)
# screen.fill(background_colour)
# pygame.display.flip()

rect = pygame.draw.rect(screen,background_colour,pygame.Rect(40,40,60,60))
pygame.display.flip()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            print("Right")
            rect.move_ip(1,0)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            print("Left")
        if pygame.key.get_pressed()[pygame.K_UP]:
            print("Up")
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            print("Down")
    font = pygame.font.SysFont('Arial', 25)
        ################
    screen.blit(font.render('Hello!', True, (255,0,0)), (200, 100))
    pygame.display.flip() 
    

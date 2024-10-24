import pygame
#general setup
pygame.init()

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
while running :
    #pool event
    #pygame.QUIT = when the user clicks on the X it => closes window
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running == False

    screen.fill('blue') 
    
pygame.quit()
import pygame
#general setup
pygame.init()

caption = 'Study space gamee'
pygame.display.set_caption(caption)
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

#testing place surface
surf = pygame.Surface((100,200))
surf.fill('orange')
x= 100

space_ship = pygame.image.load('images/player.png')

while running :
    #pool event
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

    screen.fill('silver')
    screen.blit(surf,(100,150))
    x+= 0.1
    screen.blit(space_ship,(100,100))
    pygame.display.update()
    
pygame.quit()
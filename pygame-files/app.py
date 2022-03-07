import pygame
from sys import exit

#this basically starts pygame - like turning the engine on in a car
pygame.init()

#creating the window that players are seeing - numbers are the widfth and height values

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('JUMPMAN 2: DOKI DOKI PANIC')
clock = pygame.time.Clock()
#the arguments for font are the type (none is default) and size in px
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#these are surfaces which you load in using the path in the folder
sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

#to create the text surface - we need 3 variables - the text you want to display, anti aliasing, and the color we want it in
text_surface = test_font.render('JUMPMAN 2: DOKI DOKI PANIC: Majoras Mask', False, 'Black')

# rectangles are being used like hitboxes - here we're setting the midbottom point of the rectangle as being on the ground in the actual game - this moves the sprite to where we want it.

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (900, 300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300))

while True:
    #the whole game goes in here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #pygame.quit is the opposite of pygame.init()
            pygame.quit()
            exit()
    #blit is block image transfer - which means to put one surface on another - the numbers are the place in the window, starting from the top left. The below puts the sky and ground together on the screen.
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(100, 50))

    snail_rectangle.x -= 4
    if snail_rectangle.right < 0:
        snail_rectangle.x = 900
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player_surface, player_rectangle)
   
    # collision detection using rectangles

    if player_rectangle.colliderect(snail_rectangle):
        print('BOOM')
    else: 
        print('Nope')


    pygame.display.update()
    #this controls how fast we're running our while loop - basically framne rate 
    clock.tick(60)
import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int((pygame.time.get_ticks()/1000)) - start_time
    score_surface = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rectangle = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rectangle)
    return current_time

def obstacle_movement(obstacle_list):


    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            elif obstacle_rect.bottom == 210:
                screen.blit(fly_surface, obstacle_rect)
            

            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []


def collision(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surface, player_index

    if player_rectangle.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index)]

#this basically starts pygame - like turning the engine on in a car
pygame.init()

#creating the window that players are seeing - numbers are the widfth and height values

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('JUMPMAN 2: DOKI DOKI PANIC')
clock = pygame.time.Clock()
#the arguments for font are the type (none is default) and size in px
test_font = pygame.font.Font('font/Pixeltype.ttf', 40)
game_active = False
start_time = 0

#these are surfaces which you load in using the path in the folder
sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

#to create the text surface - we need 3 variables - the text you want to display, anti aliasing, and the color we want it in
# score_surface = test_font.render('JUMPMAN 2', False, (64, 64, 64))
# score_rectangle = score_surface.get_rect(center = (400, 50))

# rectangles are being used like hitboxes - here we're setting the midbottom point of the rectangle as being on the ground in the actual game - this moves the sprite to where we want it.


#obstacles
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

fly_frame_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

obstacle_rectangle_list = []

player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
#we use the below to chose between the 2 choices in the player walk list
player_index = 0
player_jump = pygame.image.load('graphics/player/jump.png')


player_surface = player_walk[player_index]
player_rectangle = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0
player_score = 0

#intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rectangle = player_stand.get_rect(center = (400, 200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render('press Esc to run', False, (111, 196, 169))
game_message_rectangle = game_message.get_rect(center = (400, 320))

#Timers
obstacle_time = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_time, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fly_animation_timer, 200)


while True:
    #the whole game goes in here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #pygame.quit is the opposite of pygame.init()
            pygame.quit()
            exit()
        if game_active == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos):
                    if player_rectangle.bottom >= 300:
                        player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rectangle.bottom >= 300:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_active = True
                    start_time = int((pygame.time.get_ticks()/1000))
        if game_active:
            if event.type == obstacle_time:
                if randint(0, 2):
                    obstacle_rectangle_list.append(snail_surface.get_rect(midbottom = (randint(900, 1100), 300)))
                else:
                    obstacle_rectangle_list.append(fly_surface.get_rect(midbottom = (randint(900, 1100), 210)))

                #snail animation timer   
            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                        snail_frame_index = 1
                else:
                        snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]

                #fly animation timers
            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]


    if game_active:
        player_score = display_score()

    #blit is block image transfer - which means to put one surface on another - the numbers are the place in the window, starting from the top left. The below puts the sky and ground together on the screen.
    
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        display_score()

 # background colour
    #     pygame.draw.rect(screen, '#c0e8ec', score_rectangle)
    # margin for the background colour
        # pygame.draw.rect(screen, '#c0e8ec', score_rectangle, 10)
        # screen.blit(score_surface, score_rectangle)

    
    #player 

    #this is the code we run before drawing the player - we give them gravity and check if their position is greater than 300, if it is we put it back to 300 (this basically puts them on the floor at all times)
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300:
            player_rectangle.bottom = 300
        player_animation()

        screen.blit(player_surface, player_rectangle)

        #Obstacle movement
        obstacle_rectangle_list = obstacle_movement(obstacle_rectangle_list)

    #collision

        game_active = collision(player_rectangle, obstacle_rectangle_list)

    #game over screen:
    else:
        screen.fill((94, 129, 162))
        screen.blit(game_name, game_name_rect)
        obstacle_rectangle_list.clear()
        player_rectangle.midbottom = (80, 300)
        player_gravity = 0

        game_over_text = test_font.render(f'Game Over - You scored {player_score}', False, (111, 196, 169))
        game_over_text_rectangle = game_over_text.get_rect(center = (400, 320))

        screen.blit(player_stand, player_stand_rectangle)

        if player_score == 0:
            screen.blit(game_message, game_message_rectangle)
        else:
            screen.blit(game_over_text, game_over_text_rectangle)


    pygame.display.update()
    #this controls how fast we're running our while loop - basically framne rate 
    clock.tick(60)
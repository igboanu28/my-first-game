import pygame
from sys import exit

# it's like a rule to add this code at the begninig of your code pygame.init()
pygame.init()

# this is use to create a window for the game that is use to display the game (display surface)
screen =pygame.display.set_mode((800,400))

# this part of the code is used to change the title of the game
pygame.display.set_caption('Runner')

# this code helps with time and also helps control frame rates
clock = pygame.time.Clock()

# Note: when creating a text you will have to create an image of the text then you will now place it on the display surface
# 1. create a font (text size and style)
# 2. write text on a sky_surface
# 3. blit the text surface
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

# this is my sky backgroung note: if you want to import any new image you need to import it in a new surface
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_text_surf = test_font.render('Score',False,(64,64,64))
score_rect = score_text_surf.get_rect(center = (400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600,300))

# if you are not using a sprite you will have to create this two varaibles the surface and rectangle.
# the rectangle helps in the positioning of a surface
player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
# note: A sprite class is combianation of the surface and a rectangle and places them in one class which makes it easier to do.

player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            # the exit() function helps in completely closing your games because it the quit function doesn't
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_gravity = -20


        # while using the event for keyboard you will have to do this two things 
        #     1.)check if any button was pressed
        #     2.) work with a specific key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_rect.bottom >= 300:
                player_gravity = -20
                
                    
        
    if game_active:
        # blit stands for block image transfer this part of the code makes the surface created visible and also help fix the position of the surface.
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # screen.blit(text_surface,(300,50))
        
        # this line of the code constantly moves the snail from the right to the left by increasing it movement by 4.
        snail_rect.x -= 4

        # so in the if statement i placed the snail to the right side of the screen when it goes to far from the left side of the screen.
        if snail_rect.right < 0:
            snail_rect.left = 800
        screen.blit(snail_surface,snail_rect)
        
        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(player_surf,player_rect)




        # note: collisions return 0s and 1s
        # if player_rect.colliderect(snail_rect):
        #     print('collision') 

        # the set of code helps in pygame.mouse that is to know or get the mouse position
        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     print(pygame.mouse.get_pressed())

        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        screen.blit(score_text_surf,score_rect)

        # this is one way to use the keyboard py.game by putting it in a dictionary
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('jump')

        # collison (Game over)
        if snail_rect.colliderect(player_rect):
            game_active = False
    pygame.display.update()
    clock.tick(60)
    # clock.tick() is my frame rate (that is the game speed)
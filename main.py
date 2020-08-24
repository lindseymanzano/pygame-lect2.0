import pygame
from pygame.locals import *
import os
#https://www.pygame.org/docs/

#pygame.init() <-- sometimes needed, not required in repl.it

#determines dimensions of and builds screen object
width = 500
height = 300
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#loads an image file from its file path using os.path.join() to create the file path argument for load()
player = pygame.image.load("assets/mohan.png").convert(
)  #OR player = pygame.image.load(os.path.join("assets","mohan.png"))
player.set_colorkey(
    (255, 255, 255)
)  #along with the .convert(), allows you to make certain color in image transparent
player = pygame.transform.scale(
    player, (60, 60))  #scales image to the specified dimensions

#creates a background made up of grass image
background = pygame.image.load("assets/grass.jpg")
background = pygame.transform.scale(background, (width, height))

x = 100
y = 100
size = player.get_rect().size  #gets dimensions of player
rect1 = pygame.Rect((x, y + 10), size)
rect2 = pygame.Rect((400, 0), (10, 300))

x = 100
y = 100
color = (255, 255, 0)
FPS = 50  #speed
running = True
dx = 2  #stepsize
while running:
    clock.tick(FPS)
    eventlist = pygame.event.get()
    for event in eventlist:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                print(event)
                color = (255, 0, 0)
            if event.key == pygame.K_SPACE:
                dx = -dx
            #if event.key == pygame.K_RIGHT:
            #x = x + dx

    keys = pygame.key.get_pressed()
    #print(keys) <-- gives me a list of all keys, 0 if not pressed (false), 1 if pressed (true)
    if keys[pygame.
            K_RIGHT]:  #if the right arrow key is pressed down (true = 1)
        x = x + dx
        rect1.move_ip(dx, 0)

    #makes rect1 change direction when it collides with rect2
    if rect1.colliderect(rect2):
        dx = -dx

    #prints the index of the rectangle that rect1 collides with
    listrect = [rect2]
    index = rect1.colliderect(listrect)
    if index == -1:
        pass  #no collision
    else:
        print("collision at index: " + str(index))

    #screen.fill(color)
    screen.blit(background, (0, 0))  #displays background image
    #screen.blit(player,(x,y)) displays player on screen(top left corner matching point given)
    screen.blit(
        player,
        rect1)  #draws player at position of rectangle (sticks them together)
    #pygame.draw.rect(screen, (255, 0, 0), rect1) draws rectangle on screen
    pygame.draw.rect(screen, (0, 0, 0), rect2)

    pygame.display.update(
    )  #updates screen so we can see everything drawn, VERY IMPORTANT
    #pygame.display.quit() <-- sometimes needed, not required in repl.it
#pygame.quit() <-- sometimes needed, not required in repl.it

import pygame
from pygame.locals import *
import os

width = 500
height = 300
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

player = pygame.image.load("assets/mohan.png").convert()
player.set_colorkey((255, 255, 255))

background = pygame.image.load("assets/grass.jpg")
background = pygame.transform.scale(background, (width, height))

x = 100
y = 100
size = player.get_rect().size
rect1 = pygame.Rect((x, y + 100), size)
rect2 = pygame.Rect(400, 0, 10, 300)

color = (255, 255, 0)
FPS = 50
running = True
dx = 2
state = 0
while running:
    clock.tick(FPS)
    next_state = state
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                print(event)
                color = (255, 0, 0)
                next_state = 1
            if event.key == pygame.K_SPACE:
                dx = -dx
            #if event.key == pygame.K_RIGHT:
            #  x = x + dx

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        #x = x + dx
        rect1.move_ip(dx, 0)

    if rect1.colliderect(rect2):
        dx = -dx
    listrect = [rect2]
    index = rect1.collidelist(listrect)
    if index == -1:
        #print("no collision")
        pass
    else:
        print("collision at index " + str(index))

    #screen.fill(color)
    screen.blit(background, (0, 0))
    #screen.blit(player,(x,y))
    screen.blit(player, rect1)
    #pygame.draw.rect(screen, (255,0,0), rect1)
    pygame.draw.rect(screen, (0, 0, 0), rect2)
    pygame.display.update()
    state = next_state

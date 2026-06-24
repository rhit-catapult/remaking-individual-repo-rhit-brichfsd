# The two lines below allow you to use PyGame and System functions.
# Often programmers use code that other developers have written.
import pygame
import sys

# Let's turn pygame ON
pygame.init()

# Let's create a caption for the game window
pygame.display.set_caption("Sam Brichford")
screen = pygame.display.set_mode((1200, 600))
# TODO 05: Change the window size, make sure your circle code still works.

while True:
    # Here's another loop inside of the first loop. Notice the indentation,
    # moving one tab width into the while loop makes this statement part of the
    # loop instead of outside of it.
    for event in pygame.event.get():
        # Let's just print all the events that happen in our window, wonder
        # what those could be?
        print(event)

        # we must allow our users to quit the game right? I mean not everyone
        # wants to play forever.
        # This is a conditional statement, i.e., the line sys.exit() will ONLY
        # execute when event.type is equal to pygame.QUIT (this is what ==
        # means). 
        if event.type == pygame.QUIT:
            sys.exit()

        # Additional interactions with events

    
    screen.fill(pygame.Color("gray"))

    # Draw things on the screen


    pygame.draw.circle(screen, pygame.Color("light blue"), (230, 100),100)

    pygame.draw.circle(screen, (255,0,0), (screen.get_width()/2,screen.get_height()/2), 100)

    pygame.draw.circle(screen, (255,255,0), (0,screen.get_height()), 50)

    # This will make sure that things appear on our screen, without this
    # update, everything we do will not be visible!
    # notice how this statement is still inside of the first while loop, but
    # outside of the for loop (why? because it is at the same level of
    # indentation as the for loop statement).
    pygame.display.update()

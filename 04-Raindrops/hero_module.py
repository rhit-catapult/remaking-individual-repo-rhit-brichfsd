import pygame
import sys
import time  # Note this!
import random  # Note this!

class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        self.screen = screen
        self.x = x 
        self.y = y
        self.image_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_no_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 2
        # Done 16: Initialize this Hero, as follows:
        #     - Store the screen.
        #     - Set the initial position of this Hero to x and y.
        #     - Create an image of this Hero WITH    an umbrella to the given with_umbrella_filename.
        #     - Create an image of this Hero WITHOUT an umbrella to the given without_umbrella_filename.
        #     - Set the "last hit time" to 0.
        #   Use instance variables:
        #      screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.
        

    def draw(self):
        """ Draws this sprite onto the screen. """
        # Done 17: Draw (blit) this Hero, at this Hero's position, WITHOUT an umbrella:
        #self.screen.draw.rect()
        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_no_umbrella, (self.x,self.y))
        else:
            self.screen.blit(self.image_umbrella, (self.x, self.y))
        # Done 21: Instead draw (blit) this Hero, at this Hero's position, as follows:
        #     If the current time is greater than this Hero's last_hit_time + 1,
        #       draw this Hero WITHOUT an umbrella,
        #       otherwise draw this Hero WITH an umbrella.
    

    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        # Done 19: Return True if this Hero is currently colliding with the given Raindrop.
        hitbox = pygame.draw.rect(self.screen,'white',(self.x,self.y,self.image_umbrella.get_width(), self.image_umbrella.get_height()))
        return hitbox.colliderect(raindrop.x,raindrop.y,5,2)


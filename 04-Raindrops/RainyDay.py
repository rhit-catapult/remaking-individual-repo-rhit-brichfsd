import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x=int, y=int):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5,15)
        # Done 8: Initialize this Raindrop, as follows:
        #     - Store the screen.
        #     - Set the initial position of the Raindrop to x and y.
        #     - Set the initial speed to a random integer between 5 and 15.
        #   Use instance variables:   screen  x  y  speed.
        

    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        # TODO 11: Change the  y  position of this Raindrop by its speed.
        self.y = self.y + self.speed

    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        # Done 13: Return  True  if the  y  position of this Raindrop is greater than 800.
        if self.y > 800:
            return True
        else:
            pass

    def draw(self):
        """ Draws this sprite onto the screen. """
        # Done 9: Draw a vertical line that is 5 pixels long, 2 pixels thick,
        pygame.draw.line(self.screen,'Blue',(self.x,self.y),(self.x, self.y+5),2)
        #      from the current position of this Raindrop (use either a black or blue color).


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

class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        self.screen = screen
        self.x = x
        self.y = y
        self.image_filename = pygame.image.load(image_filename)
        self.raindrops = []
        # Done 24: Initialize this Cloud, as follows:
        #     - Store the screen.
        #     - Set the initial position of this Cloud to x and y.
        #     - Set the image of this Cloud to the given image filename.
        #     - Create a list for Raindrop objects as an empty list called raindrops.
        #   Use instance variables:
        #      screen  x  y  image   raindrops.

    def draw(self):
        """ Draws this sprite onto the screen. """
        # Done 25: Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image_filename,(self.x,self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        # TODO 28: Append a new Raindrop to this Cloud's list of raindrops,
        #for i in range(5):
        raindrop = Raindrop(self.screen,random.randint(self.x,self.x+300),self.y+100)
        self.raindrops.append(raindrop)
        #     where the new Raindrop starts at:
        #       - x is a random integer between this Cloud's x and this Cloud's x + 300.
        #       - y is this Cloud's y + 100.
        


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
   
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((1000, 600))
    
    clock = pygame.time.Clock()
   
    mike = Hero(screen,200,400,"Mike_umbrella.png","Mike.png")
    
    alyssa = Hero(screen,700,400,'Alyssa_umbrella.png',"Alyssa.png")
    # Done 23: Make a Cloud, named cloud, with appropriate images, starting at position x=300 y=50.
    cloud = Cloud(screen,300,50,'another_cloud.png')
    
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         cloud.x -= 5
            #         print(cloud.x)
            #     if event.key == pygame.K_RIGHT:
            #         cloud.x += 5
            #     if event.key == pygame.K_UP:
            #         cloud.y -= 5
            #     if event.key == pygame.K_DOWN:
            #         cloud.y += 5

        if event.type == pygame.KEYDOWN:
            pressedKey = pygame.key.get_pressed()
            if pressedKey[pygame.K_UP]:
                cloud.y -= 5
            if pressedKey[pygame.K_DOWN]:
                cloud.y += 5
            if pressedKey[pygame.K_LEFT]:
                cloud.x -= 5
            if pressedKey[pygame.K_RIGHT]:
                cloud.x += 5
        # Done 27: Inside the game loop (AFTER the events loop above), get the list of keys that are currently pressed.
        #     Arrange so that the Cloud moves:
        #       5 pixels (or 10 pixels) to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        #       5 pixels (or 10 pixels) to the left  if the Left  Arrow key (pygame.K_LEFT)  is pressed.
        #       5 pixels (or 10 pixels) up           if the Up    Arrow key (pygame.K_UP)    is pressed.
        #       5 pixels (or 10 pixels) down         if the Down  Arrow key (pygame.K_DOWN)  is pressed.
        # DISCUSS: If you want something to happen once per key press, put it in the events loop above
        #          If you want something to continually happen while holding the key, put it after the events loop.
        
       
        screen.fill((255, 255, 255))
        
        # test_drop.move()
        
        # if mike.hit_by(test_drop) == True:
        #     test_drop.x = 700
        #     test_drop.y = 10
        #     mike.last_hit_time = time.time()
        # if alyssa.hit_by(test_drop) == True:
        #     test_drop.x = 350
        #     test_drop.y = 10
        #     alyssa.last_hit_time = time.time()

        
            
    

        # Done 26: Draw the Cloud.
        cloud.draw()
        cloud.rain()
        
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)
            if mike.hit_by(raindrop) == True:
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if alyssa.hit_by(raindrop) == True:
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)   
        # TODO 29: Remove the temporary testdrop code from this function and refactor it as follows:
        # TODO: Make the Cloud "rain", then:
        # TODO    For each Raindrop in the Cloud's list of raindrops:
            #       - move the Raindrop.
            #       - draw the Raindrop.
            # TODO  30: if the Hero (Mike or Alyssa) is hit by a Raindrop, set the Hero's last_time_hit to the current time.
            # Optional  - if the Raindrop is off the screen or hitting a Hero, remove it from the Cloud's list of raindrops.

        
        
        mike.draw()
        
        alyssa.draw()
       

        pygame.display.update()
        
    


main()

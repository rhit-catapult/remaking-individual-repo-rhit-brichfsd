import pygame
import sys
import time  # Note this!
import random  # Note this!
import hero_module
import cloud_module

def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
   
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((1000, 600))
    
    clock = pygame.time.Clock()
   
    mike = hero_module.Hero(screen,200,400,"Mike_umbrella.png","Mike.png")
    
    alyssa = hero_module.Hero(screen,700,400,'Alyssa_umbrella.png',"Alyssa.png")
    # Done 23: Make a Cloud, named cloud, with appropriate images, starting at position x=300 y=50.
    cloud = cloud_module.Cloud(screen,300,50,'another_cloud.png')
    
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

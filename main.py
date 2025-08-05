import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable)

    x = SCREEN_WIDTH / 2  # Set starting position in middle of screen
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()

    dt = 0
    running = True # Initialize a flag to control the loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # Set the flag to False to exit the loop
        screen.fill("black")

        for object in updatable:
            object.update(dt)
        for object in asteroids:
            if object.collision(player):
                print("Game over!")
                sys.exit()
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()    

if __name__ == "__main__":
    main()

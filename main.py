import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        
        player.draw(screen)
        dt = clock.tick(60) / 1000
        player.update(dt)
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
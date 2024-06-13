import pygame

def basic_pygame_test():
    pygame.init()
    screen = pygame.display.set_mode((720, 720))
    pygame.display.set_caption("Basic Pygame Test")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((169, 169, 169))
        pygame.display.flip()
    pygame.quit()


import pygame
import logging

logging.basicConfig(filename='simulation_debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
WIDTH, HEIGHT = 720, 720  # Dimensions of the simulation window

def main():
    logging.info("Starting simulation")
    pygame.init()
    logging.info("Pygame initialized")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    logging.info("Display set")
    pygame.display.set_caption("Ant Colony Simulation")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((169, 169, 169))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    logging.info("Pygame quit")

if __name__ == "__main__":
    main()

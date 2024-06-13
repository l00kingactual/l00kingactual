import pygame
import logging

logging.basicConfig(filename='simulation_debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
WIDTH, HEIGHT = 720, 720  # Dimensions of the simulation window

def main():
    logging.info("Starting simulation")
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
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

if __name__ == "__main__":
    main()

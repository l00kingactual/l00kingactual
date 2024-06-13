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

if __name__ == "__main__":
    basic_pygame_test()

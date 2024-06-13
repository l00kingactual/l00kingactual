import pygame
import random

# Pygame setup
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define parameters
num_prey = 50
num_predators = 10
prey_birth_rate = 0.1
predation_rate = 0.01
predator_death_rate = 0.05
predator_reproduction_rate = 0.01

# Initialize prey and predators
prey = [pygame.Vector2(random.uniform(0, width), random.uniform(0, height)) for _ in range(num_prey)]
predators = [pygame.Vector2(random.uniform(0, width), random.uniform(0, height)) for _ in range(num_predators)]

# Simulation loop
running = True
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update prey
    new_prey = []
    for p in prey:
        if random.random() < prey_birth_rate:
            new_prey.append(pygame.Vector2(random.uniform(0, width), random.uniform(0, height)))
        new_prey.append(p)
        p += pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        if p.x > width:
            p.x = 0
        elif p.x < 0:
            p.x = width
        if p.y > height:
            p.y = 0
        elif p.y < 0:
            p.y = height

    prey = new_prey

    # Update predators
    new_predators = []
    for pred in predators:
        if random.random() < predator_death_rate:
            continue
        if random.random() < predator_reproduction_rate:
            new_predators.append(pygame.Vector2(random.uniform(0, width), random.uniform(0, height)))
        new_predators.append(pred)
        pred += pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        if pred.x > width:
            pred.x = 0
        elif pred.x < 0:
            pred.x = width
        if pred.y > height:
            pred.y = 0
        elif pred.y < 0:
            pred.y = height

    predators = new_predators

    # Predation
    new_prey = []
    for p in prey:
        eaten = False
        for pred in predators:
            if p.distance_to(pred) < 10:
                if random.random() < predation_rate:
                    eaten = True
                    break
        if not eaten:
            new_prey.append(p)

    prey = new_prey

    # Draw prey
    for p in prey:
        pygame.draw.circle(screen, (0, 255, 0), (int(p.x), int(p.y)), 3)

    # Draw predators
    for pred in predators:
        pygame.draw.circle(screen, (255, 0, 0), (int(pred.x), int(pred.y)), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

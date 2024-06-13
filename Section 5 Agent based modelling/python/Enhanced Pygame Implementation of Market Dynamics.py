import pygame
import random

# Constants
WIDTH, HEIGHT = 1280, 720
BUYER_COUNT = 50
SELLER_COUNT = 20
GOOD_COUNT = 100
PRICE_ADJUSTMENT = 0.1
MAX_PRICE = 10
MIN_PRICE = 1
BUYER_BUDGET = 20
GOOD_RADIUS = 5
MAX_SPEED = 2

# Colors
BACKGROUND_COLOR = (30, 30, 30)
BUYER_COLOR = (0, 255, 0)
SELLER_COLOR = (0, 0, 255)
GOOD_COLOR = (255, 0, 0)

class Buyer:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.budget = BUYER_BUDGET
        self.purchased_goods = 0

    def update(self, sellers):
        # Move the buyer
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += WIDTH
        elif self.x >= WIDTH: self.x -= WIDTH
        if self.y < 0: self.y += HEIGHT
        elif self.y >= HEIGHT: self.y -= HEIGHT

        for seller in sellers:
            distance = ((self.x - seller.x) ** 2 + (self.y - seller.y) ** 2) ** 0.5
            if seller.price <= self.budget and distance < GOOD_RADIUS * 2 and seller.goods > 0:
                self.budget -= seller.price
                self.purchased_goods += 1
                seller.goods -= 1
                print(f"Buyer at ({self.x}, {self.y}) bought from seller at ({seller.x}, {seller.y})")

    def draw(self, screen):
        pygame.draw.circle(screen, BUYER_COLOR, (int(self.x), int(self.y)), GOOD_RADIUS)

class Seller:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.goods = GOOD_COUNT
        self.price = random.uniform(MIN_PRICE, MAX_PRICE)

    def update(self, buyers):
        # Move the seller
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += WIDTH
        elif self.x >= WIDTH: self.x -= WIDTH
        if self.y < 0: self.y += HEIGHT
        elif self.y >= HEIGHT: self.y -= HEIGHT

        demand = sum(1 for buyer in buyers if buyer.budget >= self.price and ((self.x - buyer.x) ** 2 + (self.y - buyer.y) ** 2) ** 0.5 < GOOD_RADIUS * 2)
        if demand > self.goods:
            self.price = min(MAX_PRICE, self.price + PRICE_ADJUSTMENT)
        elif demand < self.goods:
            self.price = max(MIN_PRICE, self.price - PRICE_ADJUSTMENT)
        print(f"Seller at ({self.x}, {self.y}) adjusted price to {self.price} based on demand")

    def draw(self, screen):
        pygame.draw.circle(screen, SELLER_COLOR, (int(self.x), int(self.y)), GOOD_RADIUS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Market Dynamics Simulation")

# Main loop
def main():
    buyers = [Buyer() for _ in range(BUYER_COUNT)]
    sellers = [Seller() for _ in range(SELLER_COUNT)]
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for seller in sellers:
            seller.update(buyers)
            seller.draw(screen)

        for buyer in buyers:
            buyer.update(sellers)
            buyer.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

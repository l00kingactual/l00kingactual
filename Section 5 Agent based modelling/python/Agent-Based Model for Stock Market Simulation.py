import pygame
import random

# Constants
WIDTH, HEIGHT = 1280, 720
TRADER_COUNT = 50
INITIAL_PRICE = 100
PRICE_FLUCTUATION = 5
MAX_SPEED = 2

# Colors
BACKGROUND_COLOR = (30, 30, 30)
TRADER_COLOR = (0, 255, 0)
BUYER_COLOR = (0, 0, 255)
SELLER_COLOR = (255, 0, 0)
NEUTRAL_COLOR = (255, 255, 255)

class Trader:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.role = random.choice(['buyer', 'seller', 'neutral'])
        self.cash = random.uniform(50, 150)
        self.stocks = random.randint(0, 20)
        self.color = NEUTRAL_COLOR if self.role == 'neutral' else (BUYER_COLOR if self.role == 'buyer' else SELLER_COLOR)

    def update(self, stock_price):
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += WIDTH
        elif self.x >= WIDTH: self.x -= WIDTH
        if self.y < 0: self.y += HEIGHT
        elif self.y >= HEIGHT: self.y -= HEIGHT

        # Make trading decisions
        if self.role == 'buyer' and self.cash >= stock_price:
            if random.random() < 0.1:  # 10% chance to buy
                self.stocks += 1
                self.cash -= stock_price
        elif self.role == 'seller' and self.stocks > 0:
            if random.random() < 0.1:  # 10% chance to sell
                self.stocks -= 1
                self.cash += stock_price

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Stock Market Simulation")
    clock = pygame.time.Clock()

    traders = [Trader() for _ in range(TRADER_COUNT)]
    stock_price = INITIAL_PRICE
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        # Update stock price based on supply and demand
        buyers = sum(1 for trader in traders if trader.role == 'buyer')
        sellers = sum(1 for trader in traders if trader.role == 'seller')
        stock_price += PRICE_FLUCTUATION * (buyers - sellers) / TRADER_COUNT

        for trader in traders:
            trader.update(stock_price)
            trader.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

# Import necessary libraries
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import matplotlib.pyplot as plt

# Define the agent class
class TrafficAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.speed = 1
    
    def step(self):
        self.move()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

# Define the model class
class TrafficModel(Model):
    def __init__(self, width, height, N):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.datacollector = DataCollector({"Moving agents": lambda m: sum([1 for a in m.schedule.agents if a.speed > 0])})

        # Create agents
        for i in range(self.num_agents):
            a = TrafficAgent(i, self)
            self.schedule.add(a)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

# Set parameters
width, height = 10, 10
num_agents = 50
steps = 100

# Run the model
model = TrafficModel(width, height, num_agents)
for i in range(steps):
    model.step()

# Plot the results
moving_agents = model.datacollector.get_model_vars_dataframe()
moving_agents.plot()
plt.show()

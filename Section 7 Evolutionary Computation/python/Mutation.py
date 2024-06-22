import random

def swap_mutation(route):
    # Select two positions in the route to swap
    pos1 = random.randint(0, len(route) - 1)
    pos2 = random.randint(0, len(route) - 1)
    
    # Swap the cities at pos1 and pos2
    route[pos1], route[pos2] = route[pos2], route[pos1]
    
    return route

# Example usage
original_route = [1, 2, 3, 4, 5]
mutated_route = swap_mutation(original_route.copy())

print(f"Original Route: {original_route}")
print(f"Mutated Route: {mutated_route}")

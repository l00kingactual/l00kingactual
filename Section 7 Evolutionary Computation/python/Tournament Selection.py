# Select parents
def select_parents(population):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(population, TOURNAMENT_SIZE)
        tournament.sort(key=calculate_distance)
        selected.append(tournament[0])
    return selected

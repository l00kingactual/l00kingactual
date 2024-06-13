import itertools
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Board dimensions
board_width = 90
board_height = 60

# A4 dimensions in cm
a4_portrait = (21, 29.7)  # width x height
a4_landscape = (29.7, 21)  # width x height

def generate_configurations():
    # Generate all possible combinations of placements (within reasonable limits)
    # Using integer division to ensure the output is suitable for range()
    max_portrait = (board_width // a4_portrait[0]) * (board_height // a4_portrait[1])
    max_landscape = (board_width // a4_landscape[0]) * (board_height // a4_landscape[1])
    
    configurations = []
    for p in range(int(max_portrait + 1)):  # Ensure p is an integer
        for l in range(int(max_landscape + 1)):  # Ensure l is an integer
            configurations.append((p, l))
    return configurations

def evaluate_configurations(configurations):
    # Evaluate each configuration based on area coverage and balance of orientations
    results = []
    total_area = board_width * board_height
    for portrait_count, landscape_count in configurations:
        area_portrait = portrait_count * a4_portrait[0] * a4_portrait[1]
        area_landscape = landscape_count * a4_landscape[0] * a4_landscape[1]
        total_covered = area_portrait + area_landscape
        
        # Calculate balance ratio
        if portrait_count + landscape_count > 0:
            balance = abs(portrait_count - landscape_count) / (portrait_count + landscape_count)
        else:
            balance = 1  # worst case if no sheets are used
        
        # Calculate coverage efficiency
        coverage_efficiency = total_covered / total_area
        
        # Prefer solutions that are close to 50:50 balance and cover a large area
        score = coverage_efficiency * (1 - balance)
        results.append((portrait_count, landscape_count, coverage_efficiency, balance, score))
    
    # Sort by score
    results.sort(key=lambda x: x[4], reverse=True)
    return results

def plot_top_configurations(results, top_n=10):
    # Plot the top N configurations
    fig, axs = plt.subplots(2, 5, figsize=(20, 8))
    for idx, (ax, result) in enumerate(zip(axs.flatten(), results[:top_n])):
        portrait_count, landscape_count, _, _, _ = result
        plot_configuration(ax, portrait_count, landscape_count, idx + 1)
    plt.tight_layout()
    plt.show()

def plot_configuration(ax, num_portrait, num_landscape, plot_idx):
    ax.set_title(f'Config {plot_idx}: P={num_portrait}, L={num_landscape}')
    ax.set_xlim([0, board_width])
    ax.set_ylim([0, board_height])

    # Plot portrait
    for i in range(num_portrait):
        x = (i * a4_portrait[0]) % board_width
        y = (i * a4_portrait[1]) % board_height
        rect = patches.Rectangle((x, y), a4_portrait[0], a4_portrait[1], edgecolor='blue', facecolor='blue', alpha=0.5)
        ax.add_patch(rect)
    
    # Plot landscape
    for i in range(num_landscape):
        x = (i * a4_landscape[0]) % board_width
        y = (i * a4_landscape[1]) % board_height
        rect = patches.Rectangle((x, y), a4_landscape[0], a4_landscape[1], edgecolor='red', facecolor='red', alpha=0.5)
        ax.add_patch(rect)

# Main execution
configs = generate_configurations()
evaluated_results = evaluate_configurations(configs)
plot_top_configurations(evaluated_results, top_n=10)

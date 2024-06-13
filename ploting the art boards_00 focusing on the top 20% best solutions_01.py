import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Board dimensions
board_width = 90
board_height = 60

# A4 dimensions in cm
a4_portrait = (21, 29.7)  # width x height
a4_landscape = (29.7, 21)  # width x height

def generate_configurations():
    # Using integer division to ensure the output is suitable for range()
    max_portrait = (board_width // a4_portrait[0]) * (board_height // a4_portrait[1])
    max_landscape = (board_width // a4_landscape[0]) * (board_height // a4_landscape[1])
    
    configurations = []
    for p in range(int(max_portrait + 1)):  # Cast to int for safety
        for l in range(int(max_landscape + 1)):  # Cast to int for safety
            configurations.append((p, l))
    return configurations

def evaluate_configurations(configurations):
    total_area = board_width * board_height
    results = []
    for portrait_count, landscape_count in configurations:
        area_portrait = portrait_count * a4_portrait[0] * a4_portrait[1]
        area_landscape = landscape_count * a4_landscape[0] * a4_landscape[1]
        total_covered = area_portrait + area_landscape
        
        coverage_efficiency = total_covered / total_area
        balance = abs(portrait_count - landscape_count) / (portrait_count + landscape_count) if (portrait_count + landscape_count) > 0 else 1
        
        score = coverage_efficiency * (1 - balance)
        results.append((portrait_count, landscape_count, coverage_efficiency, balance, score))
    
    results.sort(key=lambda x: x[4], reverse=True)
    return results

def plot_top_configurations(results, top_n=10):
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

    x_offset = 0
    y_offset = 0
    # Place sheets and ensure not to overlap board dimensions
    for _ in range(num_portrait):
        if x_offset + a4_portrait[0] > board_width:
            x_offset = 0
            y_offset += a4_portrait[1]
        rect = patches.Rectangle((x_offset, y_offset), a4_portrait[0], a4_portrait[1], edgecolor='blue', facecolor='blue', alpha=0.5)
        ax.add_patch(rect)
        x_offset += a4_portrait[0]

    x_offset = 0  # Reset for landscape
    for _ in range(num_landscape):
        if x_offset + a4_landscape[0] > board_width:
            x_offset = 0
            y_offset += a4_landscape[1]
        rect = patches.Rectangle((x_offset, y_offset), a4_landscape[0], a4_landscape[1], edgecolor='red', facecolor='red', alpha=0.5)
        ax.add_patch(rect)
        x_offset += a4_landscape[0]

configs = generate_configurations()
evaluated_results = evaluate_configurations(configs)
plot_top_configurations(evaluated_results, top_n=10)

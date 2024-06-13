import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Board dimensions
board_width = 90
board_height = 60

# A4 dimensions in cm
a4_portrait = (21, 29.7)
a4_landscape = (29.7, 21)

def place_sheets(width, height, sheet_dim):
    """Place sheets based on given dimensions, return list of rectangles and leftover space dimensions."""
    num_sheets = int(width // sheet_dim[0])
    used_width = num_sheets * sheet_dim[0]
    remaining_width = width - used_width
    remaining_height = height

    # Generate list of positions for the sheets
    positions = [(i * sheet_dim[0], 0) for i in range(num_sheets)]
    return positions, (remaining_width, remaining_height), num_sheets

def plot_board():
    fig, ax = plt.subplots()
    ax.set_xlim([0, board_width])
    ax.set_ylim([0, board_height])

    # First try to place as many portrait sheets as possible
    portrait_positions, leftover, num_portrait = place_sheets(board_width, board_height, a4_portrait)
    landscape_positions, _, num_landscape = place_sheets(leftover[0], board_height, a4_landscape)

    # Add portrait rectangles
    for pos in portrait_positions:
        rect = patches.Rectangle(pos, a4_portrait[0], a4_portrait[1], edgecolor='blue', facecolor='blue', alpha=0.5, label='Portrait' if pos == portrait_positions[0] else "")
        ax.add_patch(rect)
        ax.annotate('P', (pos[0] + a4_portrait[0]/2, a4_portrait[1]/2), color='white', ha='center', va='center')

    # Add landscape rectangles
    for pos in landscape_positions:
        rect = patches.Rectangle((board_width - leftover[0] + pos[0], pos[1]), a4_landscape[0], a4_landscape[1], edgecolor='red', facecolor='red', alpha=0.5, label='Landscape' if pos == landscape_positions[0] else "")
        ax.add_patch(rect)
        ax.annotate('L', (board_width - leftover[0] + pos[0] + a4_landscape[0]/2, a4_landscape[1]/2), color='white', ha='center', va='center')

    plt.legend()
    plt.show()

    return num_portrait, num_landscape

num_portrait, num_landscape = plot_board()
print(f"Number of Portrait sheets: {num_portrait}, Number of Landscape sheets: {num_landscape}")


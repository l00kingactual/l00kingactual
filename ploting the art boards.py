import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Dimensions of the board
board_width = 90
board_height = 60

# A4 dimensions in cm
a4_width = 21
a4_height = 29.7

def calculate_sheets(board_width, board_height, sheet_width, sheet_height):
    # Calculate number of sheets that can fit in portrait and landscape orientation
    num_sheets_portrait = (board_width // sheet_width) * (board_height // sheet_height)
    num_sheets_landscape = (board_width // sheet_height) * (board_height // sheet_width)
    
    if num_sheets_portrait > num_sheets_landscape:
        return num_sheets_portrait, 'portrait'
    else:
        return num_sheets_landscape, 'landscape'

def plot_board(board_width, board_height, sheet_width, sheet_height, orientation):
    fig, ax = plt.subplots()
    ax.set_xlim([0, board_width])
    ax.set_ylim([0, board_height])
    
    # Set color for different orientations
    color = 'blue' if orientation == 'portrait' else 'red'
    
    # Calculate number of sheets and add them to the plot
    num_width = int(board_width // sheet_width) if orientation == 'portrait' else int(board_width // sheet_height)
    num_height = int(board_height // sheet_height) if orientation == 'portrait' else int(board_height // sheet_width)
    
    for i in range(num_width):
        for j in range(num_height):
            lower_left_x = i * sheet_width if orientation == 'portrait' else i * sheet_height
            lower_left_y = j * sheet_height if orientation == 'portrait' else j * sheet_width
            rect = patches.Rectangle((lower_left_x, lower_left_y), sheet_width, sheet_height, linewidth=1, edgecolor='black', facecolor=color)
            ax.add_patch(rect)
            ax.annotate('A4', (lower_left_x + sheet_width/2, lower_left_y + sheet_height/2), color='white', weight='bold', 
                        fontsize=9, ha='center', va='center')
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Determine the best configuration
max_sheets, best_orientation = calculate_sheets(board_width, board_height, a4_width, a4_height)

# Determine dimensions based on orientation
if best_orientation == 'portrait':
    plot_board(board_width, board_height, a4_width, a4_height, best_orientation)
else:
    plot_board(board_width, board_height, a4_height, a4_width, best_orientation)

print(f"Max sheets: {max_sheets}, Orientation: {best_orientation}")

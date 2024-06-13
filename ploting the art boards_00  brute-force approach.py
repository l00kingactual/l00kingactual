import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Board dimensions
board_width = 90
board_height = 60

# A4 dimensions in cm
a4_portrait = (21, 29.7)
a4_landscape = (29.7, 21)

def place_sheets(width, height, sheet_dim):
    """Calculate the maximum number of sheets that can be placed based on the dimension."""
    num_sheets = int(width // sheet_dim[0]) * int(height // sheet_dim[1])
    rem_width = width % sheet_dim[0]
    rem_height = height % sheet_dim[1]
    return num_sheets, rem_width, rem_height

def find_best_configuration():
    # Try placing portrait first, then landscape
    portrait_count, rem_width_portrait, _ = place_sheets(board_width, board_height, a4_portrait)
    landscape_count_after_portrait, _, _ = place_sheets(rem_width_portrait, board_height, a4_landscape)
    
    # Try placing landscape first, then portrait
    landscape_count, rem_width_landscape, _ = place_sheets(board_width, board_height, a4_landscape)
    portrait_count_after_landscape, _, _ = place_sheets(rem_width_landscape, board_height, a4_portrait)
    
    # Determine which configuration fits more sheets
    if (portrait_count + landscape_count_after_portrait) > (landscape_count + portrait_count_after_landscape):
        return 'portrait_first', portrait_count, landscape_count_after_portrait
    else:
        return 'landscape_first', landscape_count, portrait_count_after_landscape

def plot_configuration():
    config, num_portrait, num_landscape = find_best_configuration()
    
    fig, ax = plt.subplots()
    ax.set_xlim([0, board_width])
    ax.set_ylim([0, board_height])

    # Variables to track where the next sheet starts
    x_offset = 0
    y_offset = 0
    
    # Plot portrait or landscape first depending on the best configuration
    if config == 'portrait_first':
        primary = a4_portrait
        secondary = a4_landscape
        primary_count = num_portrait
        secondary_count = num_landscape
    else:
        primary = a4_landscape
        secondary = a4_portrait
        primary_count = num_landscape
        secondary_count = num_portrait

    # Place primary orientation sheets
    for _ in range(primary_count):
        rect = patches.Rectangle((x_offset, y_offset), primary[0], primary[1], edgecolor='blue', facecolor='blue', alpha=0.5)
        ax.add_patch(rect)
        ax.annotate('P' if primary == a4_portrait else 'L', (x_offset + primary[0]/2, y_offset + primary[1]/2), color='white', ha='center', va='center')
        x_offset += primary[0]
        if x_offset + primary[0] > board_width:
            x_offset = 0
            y_offset += primary[1]

    # Place secondary orientation sheets
    for _ in range(secondary_count):
        rect = patches.Rectangle((x_offset, y_offset), secondary[0], secondary[1], edgecolor='red', facecolor='red', alpha=0.5)
        ax.add_patch(rect)
        ax.annotate('L' if secondary == a4_landscape else 'P', (x_offset + secondary[0]/2, y_offset + secondary[1]/2), color='white', ha='center', va='center')
        x_offset += secondary[0]
        if x_offset + secondary[0] > board_width:
            x_offset = 0
            y_offset += secondary[1]

    plt.show()

plot_configuration()

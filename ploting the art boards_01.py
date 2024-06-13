import matplotlib.pyplot as plt

# Function to calculate the total number of sheets per board
def total_sheets(portrait_sheets, landscape_sheets):
    total = portrait_sheets + landscape_sheets
    return total

# Function to visualize the art board with portrait layout
def plot_portrait_layout(width, height, portrait_sheets):
    plt.figure(figsize=(width/10, height/10))
    plt.gca().add_patch(plt.Rectangle((0, 0), width, height, fill=None, edgecolor='black'))
    plt.title(f"Portrait Layout - Total Sheets: {portrait_sheets}")
    plt.axis('equal')
    plt.axis('off')
    plt.show()

# Function to visualize the art board with landscape layout
def plot_landscape_layout(width, height, landscape_sheets):
    plt.figure(figsize=(height/10, width/10))
    plt.gca().add_patch(plt.Rectangle((0, 0), width, height, fill=None, edgecolor='black'))
    plt.title(f"Landscape Layout - Total Sheets: {landscape_sheets}")
    plt.axis('equal')
    plt.axis('off')
    plt.show()

# Dimensions of the art board
board_width = 90
board_height = 60

# Number of sheets in portrait and landscape layouts
portrait_sheets = 5
landscape_sheets = 3

# Plotting portrait layout
plot_portrait_layout(board_width, board_height, portrait_sheets)

# Plotting landscape layout
plot_landscape_layout(board_width, board_height, landscape_sheets)

# Total number of sheets per board
total = total_sheets(portrait_sheets, landscape_sheets)
print(f"Total sheets per board: {total}")

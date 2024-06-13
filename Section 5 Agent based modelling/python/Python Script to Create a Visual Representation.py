import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define the size of the map
map_size = 8192
quadrant_size = map_size // 3

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Define colors for different regions
colors = {
    'field': 'green',
    'productions': 'blue',
    'specialist_fields': 'yellow',
    'forestry': 'darkgreen',
    'renewables': 'orange',
    'animals': 'brown'
}

# Draw fields in col 1
ax.add_patch(patches.Rectangle((0, 0), quadrant_size, map_size, edgecolor='black', facecolor=colors['field'], label='Field'))

# Draw fields in col 2
ax.add_patch(patches.Rectangle((quadrant_size, 2 * quadrant_size), quadrant_size, quadrant_size, edgecolor='black', facecolor=colors['field'], label='Field'))
ax.add_patch(patches.Rectangle((quadrant_size, 0), quadrant_size, quadrant_size, edgecolor='black', facecolor=colors['field'], label='Field'))

# Draw productions in center of col 2
ax.add_patch(patches.Rectangle((quadrant_size, quadrant_size), quadrant_size, quadrant_size, edgecolor='black', facecolor=colors['productions'], label='Productions'))

# Draw small/med specialist fields around productions
specialist_size = quadrant_size // 3
ax.add_patch(patches.Rectangle((quadrant_size + specialist_size, quadrant_size + specialist_size), specialist_size, specialist_size, edgecolor='black', facecolor=colors['specialist_fields'], label='Specialist Fields'))

# Draw fields in col 3
ax.add_patch(patches.Rectangle((2 * quadrant_size, 0), quadrant_size, map_size, edgecolor='black', facecolor=colors['field'], label='Field'))

# Draw forestry, renewables, and animals
ax.add_patch(patches.Rectangle((quadrant_size + 50, quadrant_size - 50), 200, 200, edgecolor='black', facecolor=colors['forestry'], label='Forestry'))
ax.add_patch(patches.Rectangle((2 * quadrant_size - 250, quadrant_size + 50), 200, 200, edgecolor='black', facecolor=colors['renewables'], label='Renewables'))
ax.add_patch(patches.Rectangle((quadrant_size + 100, 100), 200, 200, edgecolor='black', facecolor=colors['animals'], label='Animals'))

# Set the limits and title
ax.set_xlim(0, map_size)
ax.set_ylim(0, map_size)
ax.set_title('4x Map Layout')
ax.set_xlabel('East-West (pixels)')
ax.set_ylabel('North-South (pixels)')

# Create a legend
handles, labels = [], []
for region, color in colors.items():
    handles.append(patches.Patch(color=color, label=region.capitalize()))
ax.legend(handles=handles)

# Display the plot
plt.gca().invert_yaxis()
plt.show()

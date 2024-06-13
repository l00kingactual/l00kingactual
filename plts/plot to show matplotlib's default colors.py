import matplotlib.pyplot as plt

# Create a plot to show matplotlib's default colors
for i in range(10):
    plt.plot([0, 1], [i, i], label=f'C{i}', linewidth=3)
plt.legend()
plt.show()

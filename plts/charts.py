import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [4, 3, 2, 1],
    'C': [2, 3, 4, 1]
})

# Line plot
df.plot(kind='line')
plt.show()

# Bar plot
df.plot(kind='bar')
plt.show()

# Histogram
df['A'].plot(kind='hist')
plt.show()

# Scatter plot
df.plot(kind='scatter', x='A', y='B')
plt.show()

# Box plot
df.plot(kind='box')
plt.show()

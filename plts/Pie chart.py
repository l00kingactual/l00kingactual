import matplotlib.pyplot as plt

# Pie chart
labels = 'A', 'B', 'C', 'D'
sizes = [15, 30, 45, 10]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()

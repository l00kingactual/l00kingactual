import seaborn as sns

# Load example dataset
iris = sns.load_dataset('iris')

# Pair plot
sns.pairplot(iris, hue='species')
plt.show()

# Heatmap
sns.heatmap(df.corr(), annot=True)
plt.show()

# Violin plot
sns.violinplot(x='species', y='sepal_length', data=iris)
plt.show()

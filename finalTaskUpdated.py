import pandas as pd
import matplotlib.pyplot as plt
import math

weights = [
    57.2, 62.8, 62, 65, 60, 78.9, 66, 55.2, 66, 64, 62.1, 62, 55.4, 79, 82,
    56.6, 56, 46, 55, 59, 52, 70, 61, 44, 64, 51, 45, 58, 54, 63, 66, 61.9,
    69, 62, 68, 63, 67, 64, 66.3, 65, 72.7, 60, 57.1, 78, 68, 69, 71, 55.9,
    79, 48, 50, 52, 58, 55, 65, 88, 75.8, 80, 86.1
]

df = pd.DataFrame(weights, columns=['Weight'])

mean = df['Weight'].mean()
std_dev = df['Weight'].std()
print(f"Mean of weights: {mean:.2f}")
print(f"Standard deviation of weights: {std_dev:.2f}")

x_values = pd.Series([x for x in range(int(min(weights)), int(max(weights)) + 1)])

pdf = (1 / (std_dev * math.sqrt(2 * math.pi))) * \
      pd.Series([math.exp(-0.5 * ((x - mean) / std_dev) ** 2) for x in x_values])

plt.figure(figsize=(10, 6))

plt.hist(df['Weight'], bins=10, density=True, alpha=0.6, color='yellow', edgecolor='black', label='Histogram')

plt.plot(x_values, pdf, color='red', linewidth=2, label='Normal Distribution Curve')

plt.title('Weight Distribution', fontsize=16)
plt.xlabel('Weight (kg)', fontsize=14)
plt.ylabel('Density', fontsize=14)
plt.legend()

plt.savefig('updated_weight_distribution.png')
print("Graph saved as 'updated_weight_distribution.png'")

plt.show()

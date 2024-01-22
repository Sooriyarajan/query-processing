import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)  # Setting a seed for reproducibility
num_points = 100
random_x = np.random.randn(num_points)
random_y = np.random.randn(num_points)

# Create a scatter plot with empty circles
plt.scatter(random_x, random_y, facecolors='none', edgecolors='blue', marker='o', label='Random Data')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Empty Circles and Random Data')

# Adding legend
plt.legend()

# Display the scatter plot
plt.show()

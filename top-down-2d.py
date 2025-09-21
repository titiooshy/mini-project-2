import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# loading in the data from the scanner
my_data = pd.read_csv("scan.csv")

# conversion to make the pan angle and distance to top-down view

pan_radians = np.radians(my_data["Pan"])
x_direction = my_data["Distance"] * np.sin(pan_radians)
y_direction = my_data["Distance"] * np.cos(pan_radians)

# visualizing and making the plots
plt.figure(figsize=(6, 6))
plt.scatter(x_direction, y_direction, c="red", s=10)
plt.title("2D Scan of the Pan going Top and Down for the Star")
plt.xlabel("X(cm)")
plt.ylabel("Y(cm)")
plt.axis("equal")
plt.show()

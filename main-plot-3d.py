import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# loading in the data from the scanner
my_data = pd.read_csv("scan.csv")

# conversion to make the pan and tilt angles and the distance x,y,
# and z values
pan_radians = np.radians(my_data["Pan"])
tilt_radians = np.radians(my_data["Tilt"])

# basic spherical to Cartesian conversion
x_direction = my_data["Distance"] * np.cos(tilt_radians) * np.cos(pan_radians)
y_direction = my_data["Distance"] * np.cos(tilt_radians) * np.cos(pan_radians)
z_direction = my_data["Distance"] * np.sin(tilt_radians)

# visualizing and making the plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(x_direction, y_direction, z_direction, c="blue", s=10)

ax.set_xlabel("X (cm)")
ax.set_ylabel("Y (cm)")
ax.set_zlabel("Z (cm)")
ax.set_title("3D Scan of Star")
plt.show()

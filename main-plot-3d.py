import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load scan data
my_data = pd.read_csv("scan.csv")

# Convert pan/tilt to radians
pan_rad = np.radians(my_data["Pan"])
tilt_rad = np.radians(my_data["Tilt"])
distance = my_data["Distance"]

# Spherical to Cartesian
x = distance * np.cos(tilt_rad) * np.cos(pan_rad)
y = distance * np.cos(tilt_rad) * np.sin(pan_rad)  # <-- use sin here
z = distance * np.sin(tilt_rad)

# 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(x, y, z, c="blue", s=10)

ax.set_xlabel("X (cm)")
ax.set_ylabel("Y (cm)")
ax.set_zlabel("Z (cm)")
ax.set_title("3D Scan of Object")
plt.show()

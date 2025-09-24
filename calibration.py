import pandas as pd
import matplotlib.pyplot as plt

# Load calibration data
df = pd.read_csv("calibration_data.csv")
analog = df["AnalogValue"]
distance = df["Distance_cm"]

# Simple manual calibration: Distance ≈ 10000 / (Analog - 20)
predicted = 10000 / (analog - 20)

# Calibration plot
plt.figure(figsize=(6, 4))
plt.scatter(analog, distance, label="Measured")
plt.plot(analog, predicted, color="red", label="Approx. Distance")
plt.xlabel("Analog Value")
plt.ylabel("Distance (cm)")
plt.title("IR Sensor Calibration")
plt.legend()
plt.grid(True)
plt.show()

# Error plot
error = predicted - distance
plt.figure(figsize=(6, 4))
plt.scatter(distance, error)
plt.axhline(0, color="black", linestyle="--")
plt.xlabel("Actual Distance (cm)")
plt.ylabel("Prediction Error (cm)")
plt.title("Calibration Error")
plt.grid(True)
plt.show()

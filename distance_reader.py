import serial
import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
from statistics import mean
import csv
import time

# === CONFIGURATION ===
PORT = 'COM3'        # Replace with your Arduino COM port
BAUDRATE = 9600
MAX_LEN = 100        # Number of points on the plot
CSV_FILE = "distance_log.csv"
ROLLING_WINDOW = 5   # Smoothing window

# === SETUP ===
ser = serial.Serial(PORT, BAUDRATE)
data_buffer = deque([0]*MAX_LEN, maxlen=MAX_LEN)
distance_window = deque(maxlen=ROLLING_WINDOW)
distances = []

# === CSV INITIALISATION ===
with open(CSV_FILE, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp", "Raw Distance (cm)", "Smoothed Distance (cm)"])

# === PLOT STYLE ===
plt.style.use('seaborn-v0_8-deep')
fig, ax = plt.subplots()
line, = ax.plot([], [], label='Smoothed Distance')
threshold_line = ax.axhline(y=50, color='r', linestyle='--', label='Threshold (50cm)')
ax.set_ylim(0, 400)
ax.set_xlim(0, MAX_LEN)
ax.set_title("Live Distance (cm)")
ax.set_xlabel("Time (frames)")
ax.set_ylabel("Distance (cm)")
ax.legend()

# === UPDATE FUNCTION ===
def update(frame):
    if ser.in_waiting:
        serial_line = ser.readline().decode('utf-8').strip()
        try:
            data = json.loads(serial_line)
            raw_distance = float(data["distance_cm"])
            distance_window.append(raw_distance)
            smoothed = mean(distance_window)
            distances.append(smoothed)
            if len(distances) > MAX_LEN:
                distances.pop(0)

            # Update plot
            line.set_ydata(distances)
            line.set_xdata(range(len(distances)))

            # Log to CSV
            with open(CSV_FILE, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([time.time(), raw_distance, smoothed])

        except (json.JSONDecodeError, KeyError, ValueError):
            pass

# === START ANIMATION ===
ani = animation.FuncAnimation(fig, update, interval=100)
plt.show()

# === CLEAN UP ON CLOSE ===
ser.close()
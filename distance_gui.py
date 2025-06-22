import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque
import time

# --- SETTINGS ---
THRESHOLD_CM = 50
MAX_POINTS = 100
SMOOTHING_WINDOW = 5
SERIAL_BAUD = 9600
SERIAL_PORT = 'COM3'  # You can change this manually for now

# --- STATE ---
running = False
distances = deque([0]*MAX_POINTS, maxlen=MAX_POINTS)
smoothed = deque([0]*MAX_POINTS, maxlen=MAX_POINTS)

# --- FUNCTIONS ---
def smooth(values, window=5):
    if len(values) < window:
        return values[-1]
    return sum(list(values)[-window:]) / window

def read_serial_data():
    global ser
    try:
        if not ser.is_open:
            ser.open()
        line = ser.readline().decode('utf-8').strip()
        return float(line)
    except:
        return None

def update_plot(frame):
    #if not running:
     #   return
    #value = read_serial_data()
    #if value is not None:
     #   distances.append(value)
      #  smoothed.append(smooth(distances, SMOOTHING_WINDOW))
       # line.set_ydata(smoothed)
        #line.set_xdata(range(len(smoothed)))
        #threshold_line.set_ydata([THRESHOLD_CM] * MAX_POINTS)
        #ax.relim()
        #ax.autoscale_view()
      json_data = json.loads(line)
    print("Got data:", json_data)
    distance = json_data.get("distance_cm")
    if distance is not None:
        data.append(distance)
        if len(data) > MAX_POINTS:
            data.pop(0)
        smoothed = smooth(data, SMOOTHING_WINDOW)
        line_plot.set_ydata(smoothed)
        line_plot.set_xdata(range(len(smoothed)))
        threshold_line.set_ydata([THRESHOLD_CM] * len(smoothed))
        ax.relim()
        ax.autoscale_view()
except json.JSONDecodeError:
    print("Bad data:", line)

def start_reading():
    global running
    running = True

def stop_reading():
    global running
    running = False

# --- SERIAL INIT ---
try:
    ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1)
except:
    ser = serial.Serial()
    ser.port = SERIAL_PORT
    ser.baudrate = SERIAL_BAUD
    ser.timeout = 1

# --- TKINTER GUI ---
root = tk.Tk()
root.title("Live Distance GUI")

# Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=5)

start_button = ttk.Button(button_frame, text="Start", command=start_reading)
start_button.pack(side=tk.LEFT, padx=5)

stop_button = ttk.Button(button_frame, text="Stop", command=stop_reading)
stop_button.pack(side=tk.LEFT, padx=5)

# Matplotlib Plot
fig, ax = plt.subplots(figsize=(6, 4))
line, = ax.plot([], [], label='Smoothed Distance')
threshold_line, = ax.plot([], [], 'r--', label=f'Threshold ({THRESHOLD_CM}cm)')
ax.set_title("Live Distance (cm)")
ax.set_xlabel("Time (frames)")
ax.set_ylabel("Distance (cm)")
ax.legend()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

ani = animation.FuncAnimation(fig, update_plot, interval=100)

root.mainloop()
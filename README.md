Got you, Enio. No stress — here’s your **fully corrected, clean, copy-paste-ready `README.md`** file. Just delete everything in your current README and replace it with this exact content below:

---

````markdown
# Distance Sensor with Arduino + Python 📏💻

This project uses an Arduino and an HC-SR04 ultrasonic sensor to measure real-time distance and display it live using a Python script over serial communication. Visual feedback is provided via LEDs and a buzzer, making it a simple but powerful embedded system project.

---

## 🚀 Features

- 📏 Live distance readings (in cm)  
- 🔴 Red & 🟢 Green LEDs for proximity alerts  
- 🔊 Buzzer that triggers when distance is too close  
- 🧠 Python script that reads and filters the serial data  
- 🛠️ Extendable: supports logging, plotting, or GUI dashboards  

---

## 🧰 Hardware Used

- Arduino Uno / Nano  
- HC-SR04 Ultrasonic Sensor  
- Green LED  
- Red LED  
- Passive Piezo Buzzer  
- Resistors, Breadboard, Jumper Wires  

---

## 🖥️ Software Used

- Arduino IDE (for uploading `.ino` code)  
- Python 3.13+  
- Python library: `pyserial`  

---

## 💻 How to Use

1. Upload `distance_reader.ino` to your Arduino  
2. Connect the circuit (see preview image below)  
3. Install Python dependency:

```bash
pip install pyserial
````

4. Edit and run the Python script:

```python
PORT = 'COM4'  # Change to your actual port
python distance_reader.py
```

---

## 🗂️ File Structure

```
distance-sensor-python/
├── distance_reader.ino       # Arduino code
├── distance_reader.py        # Python script
├── README.md                 # This file
├── *.png / *.jpg             # Screenshots and preview images
```

---

## 🧠 Notes

* Sensor values above 400 cm are ignored in software to avoid ghost data
* JSON output structure from Arduino makes Python parsing easier
* LEDs and buzzer activate based on thresholds you can adjust

---

## 🛠️ Planned Upgrades

* 📈 Live plotting with matplotlib
* 🖼️ GUI interface with Tkinter or PyQt
* 🧾 CSV logging for data storage
* 💡 Auto port detection

---

## 👤 Author

Created by **Enio Mecaj** — feel free to use, share, or improve this project!

```

import serial
import json
import time

PORT = 'COM3'   # Change this to match your actual Arduino port
BAUD = 9600

arduino = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

print("📡 Reading distance in cm...\n")

try:
    while True:
        line = arduino.readline().decode('utf-8').strip()
        if line.startswith('{') and line.endswith('}'):
            data = json.loads(line)
            distance = data['distance_cm']
            print(f"📏 Distance: {distance:.1f} cm")

except KeyboardInterrupt:
    print("\nExiting...")
    arduino.close()

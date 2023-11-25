import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import serial

if serial.Serial:
    serial.Serial().close()

# Open the serial port
s = serial.Serial("COM3", baudrate=57600)

x = 0
y = []
print("START!")
while x < (15 * 512):
    noise = 0
    x += 1
    data = s.readline().decode('utf-8').rstrip("\r\n")
    if data:
        value = int(float(data))
    else:
        x -= 1
        continue
    print(value)
    y.append(value)

# Use to get data
df = pd.DataFrame(y)
df.to_csv("Dat_1.csv")

# Close the serial port
print("DONE")
s.close()
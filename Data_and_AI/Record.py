# This file use to record data.
import numpy as np
import pandas as pd
# import pickle
import matplotlib.pyplot as plt
import serial

if serial.Serial:
    serial.Serial().close()

# Open the serial port
s = serial.Serial("COM3", baudrate=57600)  # COMx in window or /dev/ttyACMx with x is number of serial port.

x = 0
y = np.array([], dtype=int)
print("START!")
while x < (240 * 512):
    try:
        if x % 512 == 0:
            print(x / 512)
        x += 1
        data = s.readline().decode('utf-8').rstrip("\r\n")
        y = np.append(y, int(data))
    except:
        pass
print(y)
plt.plot(y)
plt.show()

# Use to get data txt
np.savetxt("Dat_1.txt", y, fmt="%d")  # Save in int

# Close the serial port
print("DONE")
s.close()

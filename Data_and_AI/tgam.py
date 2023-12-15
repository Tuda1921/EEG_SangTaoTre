# This file use to record data.
import numpy as np
import pandas as pd
# import pickle
import matplotlib.pyplot as plt
import serial
import time

if serial.Serial:
    serial.Serial().close()
time.sleep(1)
x = 0
y = np.array([], dtype=int)
# Open the serial port
time.sleep(1)
s = serial.Serial("COM8", baudrate=57600)  # COMx in window or /dev/ttyACMx in Ubuntu with x is number of serial port.
path = r"Data\tgam.txt"
file = open(path, "a")
print("START!")
while x < (60*2 * 512):
    try:
        if x % 512 == 0:
            print(x / 512)
        x += 1
        data = s.readline()
        for byte in data:
            print(byte)
    except:
        pass
print(y)
plt.plot(y)
plt.show()

# Use to get data txt
# np.savetxt("Subject_1_momat.txt", y, fmt="%d")  # Save in int

# Close the serial port
print("DONE")
s.close()

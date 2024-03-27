# This file use to record data.
import numpy as np
import pandas as pd
# import pickle
import matplotlib.pyplot as plt
import serial
import time
from decode import init_ser, read_one_byte, process_brainwave_data

s = init_ser("COM10", 57600)
x = 0
y = np.array([], dtype=int)
# Open the serial port
path = r"Data\tgam.txt"
file = open(path, "w")

print("START!")
while len(y) < (10 * 512):
    x += 1
    if len(y) % 512 == 0:
        print(len(y)//512)
    diction = process_brainwave_data(s)
    if diction != -999:
        y = np.append(y, diction["raw_data"])

print(y)
plt.plot(y)
plt.show()

# Use to get data txt
np.savetxt("tgam.txt", y, fmt="%d")  # Save in int

# Close the serial port
print("DONE")
s.close()

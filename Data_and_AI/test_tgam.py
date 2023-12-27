# This file use to record data.
import numpy as np
import pandas as pd
# import pickle
import matplotlib.pyplot as plt
import serial
import time
from decode import init_ser, read_one_byte,process_brainwave_data

s = init_ser("COM8", 57600)
x = 0
y = np.array([], dtype=int)
# Open the serial port
path = r"Data\tgam.txt"
file = open(path, "w")

print("START!")
while x < (10 * 512):
    try:
        x += 1
        if x % 512 == 0:
            print(x//512)
        diction = process_brainwave_data(s)
        if diction != -999:
            print(diction)
            y = np.append(y, diction["raw_data"])
    except:
        pass

print(y)
plt.plot(y)
plt.show()

# Use to get data txt
np.savetxt("tgam.txt", y, fmt="%d")  # Save in int

# Close the serial port
print("DONE")
s.close()

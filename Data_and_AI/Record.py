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
# time.sleep(30)
s = serial.Serial("COM3", baudrate=57600)  # COMx in window or /dev/ttyACMx with x is number of serial port.
path = r"C:\Users\nguye\PycharmProjects\EEG_SangTaoTre\EEG_SangTaoTre\Data_and_AI\Data\Subject_1_testmonham.txt"
file = open(path, "a")
print("START!")
while x < (60*3 * 512):
    try:
        if x % 512 == 0:
            print(x / 512)
        x += 1
        data = s.readline().decode('utf-8').rstrip("\r\n")
        y = np.append(y, int(data))
        file.write(data)
        file.write('\n')

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
file.close()

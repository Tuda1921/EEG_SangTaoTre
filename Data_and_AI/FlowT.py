# flow realtime for demo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import serial
import time
import pickle
import scipy as sp
from Preprocessing import slide_func, filter_data, FeatureExtract
from decode import init_ser, read_one_byte,process_brainwave_data

s = init_ser("COM3", 57600) # COMx in window or /dev/ttyACMx in Ubuntu with x is number of serial port.
# path = r"Data_Iso\Subject_1_15Hz.txt"
# file = open(path, "a")
x = 0  # iterator of sample
y = np.array([], dtype=int)  # value
time_rec = 20
k = 10 * 512  # window
window_size = k
noise = []
feature = []
slide = []

print("START!")
while x < (time_rec * 512):
    x += 1
    if x % 512 == 0:
        print(x / 512)
    diction = process_brainwave_data(s)

    if diction != -999:
        print(diction["attention"])
        # print(diction["raw_data"])
        y = np.append(y, diction["raw_data"])
        # print(y)

        # if x >= window_size:
        #     if x % (1 * 512) == 0:
        #         sliding_window_start = x - window_size
        #         sliding_window_end = x
        #         sliding_window = np.array(y[sliding_window_start:sliding_window_end])  # sliding_window ~ y
        #         print(sliding_window)
        # preprocess
        # slide = filter_data(slide)
        # f, t, Zxx = sp.signal.stft(slide, 512, nperseg=512 * 10, noverlap=512 * 9)
        # feature_window = FeatureExtract(slide)
        # feature.append(feature_window)

        # plot
        # AI

        slide = []
        # file.write(data)
        # file.write('\n')
print(y)
print(len(y))
plt.plot(y)
plt.show()

# Close the serial port
print("DONE")
s.close()
# file.close()

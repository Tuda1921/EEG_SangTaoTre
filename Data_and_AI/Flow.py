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

s = init_ser("COM4", 57600) # COMx in window or /dev/ttyACMx in Ubuntu with x is number of serial port.
# path = r"Data_Iso\Subject_1_15Hz.txt"
# file = open(path, "a")
x = 0  # iterator of sample
y = np.array([], dtype=int)  # value
time_rec = 60 * 2
k = 10 * 512  # window
window_size = k
noise = []
feature = []
slide = []

print("START!")
while x < (time_rec * 512):
    if x % 512 == 0:
        print(x / 512)
    diction = process_brainwave_data(s)
    if diction != -999:
        y = np.append(y, diction["raw_data"])
        print(y)
        # if slide_func(y, window_size=window_size, iter=x) is not None:
        slide = slide_func(y, window_size=window_size, iter=x)
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
    x += 1
print(y)
plt.plot(y)
plt.show()

# Close the serial port
print("DONE")
s.close()
# file.close()

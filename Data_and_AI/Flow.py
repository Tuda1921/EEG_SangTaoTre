# flow realtime for demo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import serial
import time
import pickle
from Preprocessing import slide_func, filter_data, FeatureExtract
from decode import init_ser, read_one_byte,process_brainwave_data

if serial.Serial:
    serial.Serial().close()
time.sleep(1)
# Open the serial port
time.sleep(1)
s = serial.Serial("COM8", baudrate=57600)  # COMx in window or /dev/ttyACMx in Ubuntu with x is number of serial port.
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
    try:
        noise.append(0)
        if x % 512 == 0:
            print(x / 512)
        x += 1
        data = s.readline().decode('utf-8').rstrip("\r\n")
        y = np.append(y, int(data))
        if y[x] < -255 or y[x] > 255:
            noise[x] += 1
        if slide_func(y, window_size=window_size, iter=x) is not None:
            slide = slide_func(y, window_size=window_size, iter=x)
            # preprocess
            slide = filter_data(slide)
            f, t, Zxx = sp.signal.stft(slide, 512, nperseg=512 * 10, noverlap=512 * 9)

            feature_window = FeatureExtract(slide)
            feature.append(feature_window)

            # plot
            # AI

            slide = []
            # file.write(data)
            # file.write('\n')
    except:
        pass
print(y)
plt.plot(y)
plt.show()

# Close the serial port
print("DONE")
s.close()
# file.close()

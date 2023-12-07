# flow realtime for demo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import serial
import time
import pickle
from Preprocessing import filter_data, FeatureExtract

if serial.Serial:
    serial.Serial().close()
time.sleep(1)
# Open the serial port
time.sleep(1)
s = serial.Serial("COM3", baudrate=57600)  # COMx in window or /dev/ttyACMx in Ubuntu with x is number of serial port.
# path = r"Data_Iso\Subject_1_15Hz.txt"
# file = open(path, "a")

x = 0  # iterator of sample
y = np.array([], dtype=int)  # value
time_rec = 60 * 2
k = 10 * 512  # window
window_size = k
noise = []
feature = []

plt.ion()
plx = np.arange(window_size)
ply = np.zeros(window_size)
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(2, 2, 1)
ax1.set_title('EEG Raw Values')
ax1.set_xlabel('Samples')
ax1.set_ylabel('RawValue')
raw, = ax1.plot(plx, ply)

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

        # Cập nhật sliding window
        ply = np.roll(ply, -1)
        ply[-1] = int(data)

        # Cập nhật đồ thị
        raw.set_ydata(ply)
        ax1.relim()  # Cập nhật giới hạn trục
        ax1.autoscale_view()  # Tự động điều chỉnh tỷ lệ đồ thị
        plt.draw()
        plt.pause(0.01)  # Tạm dừng khoảng thời gian ngắn

        if x >= k:
            if x % (1 * 512) == 0:
                sliding_window_start = x - k
                sliding_window_end = x
                sliding_window = np.array(y[sliding_window_start:sliding_window_end])  # sliding_window ~ y

                # preprocess
                sliding_window = filter_data(sliding_window)
                feature_window = FeatureExtract(sliding_window, plot=0)
                feature.append(feature_window)

                # plot
                # AI

                sliding_window = []
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

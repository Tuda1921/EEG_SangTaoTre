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
s = serial.Serial("COM3", baudrate=57600)  # COMx in window or /dev/ttyACMx in Ubuntu with x is number of serial port.

# Khởi tạo sliding window và dữ liệu ban đầu
window_size = 100
plx = np.arange(window_size)
ply = np.zeros(window_size)



# Vòng lặp vẽ đồ thị realtime
# while True:
#     # Tạo dữ liệu mới
#     new_data = np.random.rand()
#
#     # Cập nhật sliding window
#     ply = np.roll(ply, -1)
#     ply[-1] = new_data
#
#     # Cập nhật đồ thị
#     line.set_ydata(ply)
#     ax.relim()  # Cập nhật giới hạn trục
#     ax.autoscale_view()  # Tự động điều chỉnh tỷ lệ đồ thị
#
#     plt.draw()
#     plt.pause(0.01)  # Tạm dừng khoảng thời gian ngắn

x = 0
y = np.array([], dtype=int)  # value
time_rec = 60 * 2
k = 10 * 512  # window
window_size = k

ply = np.zeros(window_size)
# Khởi tạo đồ thị
plt.ion()  # Chế độ interactive mode cho đồ thị
fig, ax1 = plt.subplots()
line, = ax1.plot(ply)
ax1.set_title('EEG Raw Values')
ax1.set_xlabel('Samples')
ax1.set_ylabel('RawValue')
raw, = ax1.plot(ply)
while x < (time_rec * 512):
    try:
        if x % 512 == 0:
            print(x / 512)
            # Cập nhật đồ thị
            raw.set_ydata(ply)
            ax1.relim()  # Cập nhật giới hạn trục
            ax1.autoscale_view()  # Tự động điều chỉnh tỷ lệ đồ thị
            plt.draw()
            plt.pause(1)  # Tạm dừng khoảng thời gian ngắn
        x += 1
        data = s.readline().decode('utf-8').rstrip("\r\n")
        # Cập nhật sliding window
        ply = np.roll(ply, -1)
        ply[-1] = int(data)

    except:
        pass
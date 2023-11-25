import numpy as np
import pandas as pd
# import pickle
import matplotlib.pyplot as plt
import serial

if serial.Serial:
    serial.Serial().close()

# Open the serial port
s = serial.Serial("/dev/ttyACM0", baudrate=57600)
# s.flushInput()
#
# while True:
#     try:
#         ser_bytes = s.readline()
#         decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
#         print(decoded_bytes)
#     except:
#         print("Keyboard Interrupt")
#         break
#
x = 0
y = np.array([], dtype=int)
print("START!")
while x < (1 * 512):
    try:
        x += 1
        data = s.readline().decode('utf-8').rstrip("\r\n")
        print(data)
        y = np.append(y, int(data))
    except:
        pass
print(y)
plt.plot(y)
plt.show()

# Use to get datatxtd
np.savetxt("Dat_1.txt", y, fmt="%d")

# Close the serial port
print("DONE")
s.close()
# flow realtime for demo
import numpy as np
import matplotlib.pyplot as plt
from Preprocessing import slide_func, filter_data, FeatureExtract
from decode import init_ser, read_one_byte, process_brainwave_data
import time
s = init_ser("COM11", 57600)  # COMx in window or /dev/ttyACMx in Ubuntu with x is number of serial port.
# path = r"testBT_TGAM.txt"
# file = open(path, "r")
x = 0  # iterator of sample
y = np.array([], dtype=int)  # value
time_rec = 2
k = 10  # window
window_size = k * 512
noise = []
feature = []
slide = []
start_time = time.time()
print("START!")

# Close the serial port
print("DONE")
s.close()

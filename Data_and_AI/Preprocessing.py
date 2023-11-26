import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

y = np.loadtxt("Dat_1.txt")
# plt.plot(y)
# plt.show()
f, t, Zxx = sp.signal.stft(y, 512, nperseg=512*15, noverlap=512*15*14//15)
plt.pcolormesh(t, f, np.abs(Zxx), vmin=-1, vmax=10, shading='auto')
plt.title('STFT Magnitude')
plt.ylim(0, 100)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

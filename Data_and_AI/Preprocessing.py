import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
y = np.loadtxt("Data/Subject_2.txt")
# mean = np.mean(y)
# std = np.std(y)
# # Lọc mảng theo phân phối chuẩn
# y = y[(y > mean - 2 * std) & (y < mean + 2 * std)]


# STFT
f, t, Zxx = sp.signal.stft(y, 512, nperseg=512 * 10, noverlap=512 * 9)
# 0.5-50 Hz
# trim = np.where((f >= 0.5) & (f <= 50))[0]
# f = f[trim]
# Zxx = Zxx[trim, :]

plt.figure(0)
plt.plot(y)

plt.figure(1)
plt.pcolormesh(t, f, np.abs(Zxx), vmin=-1, vmax=10, shading='auto')
plt.title('STFT Magnitude')
plt.ylim(0.5,50)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
# plt.show()

def FeatureExtract(t, f, Zxx):
    delta = np.array([], dtype=float)
    theta = np.array([], dtype=float)
    alpha = np.array([], dtype=float)
    beta = np.array([], dtype=float)
    abr = np.array([], dtype=float)
    tbr = np.array([], dtype=float)
    dbr = np.array([], dtype=float)
    tar = np.array([], dtype=float)
    dar = np.array([], dtype=float)
    dtabr = np.array([], dtype=float)
    for i in range(0, int(t[-1])//15):
        indices = np.where((f >= 0.5) & (f <= 4))[0]
        delta = np.append(delta, np.sum(np.abs(Zxx[indices, i])))

        indices = np.where((f >= 4) & (f <= 8))[0]
        theta = np.append(theta, np.sum(np.abs(Zxx[indices, i])))

        indices = np.where((f >= 8) & (f <= 13))[0]
        alpha = np.append(alpha, np.sum(np.abs(Zxx[indices, i])))

        indices = np.where((f >= 13) & (f <= 30))[0]
        beta = np.append(beta, np.sum(np.abs(Zxx[indices, i])))

    abr = alpha / beta
    tbr = theta / beta
    dbr = delta / beta
    tar = theta / alpha
    dar = delta / alpha
    dtabr = (alpha + beta) / (delta + theta)

    diction = {"delta": delta,
               "theta": theta,
               "alpha": alpha,
               "beta": beta,
               "abr": abr,
               "tbr": tbr,
               "dbr": dbr,
               "tar": tar,
               "dar": dar,
               "dtabr": dtabr
               }
    return diction


feature = FeatureExtract(t, f, Zxx)
plt.figure(2)
plt.plot(feature['delta'], label="delta")
plt.plot(feature['theta'], label="theta")
plt.plot(feature['alpha'], label="alpha")
plt.plot(feature['beta'], label="beta")
plt.legend()
plt.show()
# df = pd.DataFrame.from_dict(feature)
# df.to_csv("test.csv")
# print(df)
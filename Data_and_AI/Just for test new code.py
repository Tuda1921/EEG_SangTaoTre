import numpy as np
from scipy.stats import norm, kurtosis
import matplotlib.pyplot as plt
import scipy.stats as stats

data = np.loadtxt("Data/Subject_2.txt")
mean = np.mean(data)
std = np.std(data)

# Lọc mảng theo phân phối chuẩn
filtered_data = data[(data > mean - 2 * std) & (data < mean + 2 * std)]
plt.plot(filtered_data)
plt.title('Phân phối của mảng')
plt.show()
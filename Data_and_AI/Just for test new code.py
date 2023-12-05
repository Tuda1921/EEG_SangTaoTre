import numpy as np
import mne

# Đường dẫn đến tệp tin văn bản
file_path = "Data/Subject_2.txt"

# Đọc dữ liệu từ tệp tin văn bản
data = np.loadtxt(file_path)

# Tạo một đối tượng Raw của MNE từ dữ liệu
ch_names = ['EEG Channel']  # Tên kênh EEG
fs = 512  # Tần số lấy mẫu (Hz)
info = mne.create_info(ch_names=ch_names, sfreq=fs)
raw = mne.io.RawArray(data.reshape(1, -1), info)

# Khám phá và xử lý dữ liệu EEG
print(type(raw))  # Xem thông tin về kênh, tần số lấy mẫu, v.v.

# Tiếp tục xử lý dữ liệu EEG theo nhu cầu của bạn

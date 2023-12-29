import serial


def init_ser(port, baudrate):
    if serial.Serial:
        serial.Serial().close()
    ser = serial.Serial(port,
                        baudrate)  # COMx in window or /dev/ttyACMx in Ubuntu with x is number of serial port.
    return ser


def read_one_byte(ser):
    return ser.read(1)[0]


generated_checksum = 0
checksum = 0
payload_data = [0] * 65
poor_quality = 200
attention = 0
meditation = 0
eeg_values = [0] * 8
raw_data = 0
big_packet = False


def process_brainwave_data(ser):
    global big_packet, poor_quality, attention, meditation, raw_data, generated_checksum, checksum
    if read_one_byte(ser) == 170:
        if read_one_byte(ser) == 170:
            payload_length = read_one_byte(ser)
            if payload_length > 169:
                return
            generated_checksum = 0
            for i in range(0, payload_length):
                payload_data[i] = read_one_byte(ser)
                generated_checksum += payload_data[i]
            checksum = read_one_byte(ser)
            generated_checksum = 255 - generated_checksum
            if checksum == generated_checksum:
                for i in range(0, payload_length):
                    packet = payload_data[i]
                    if packet == 2:  # poorQuality
                        i += 1
                        poor_quality = payload_data[i]
                        big_packet = True
                    elif packet == 4:  # attention
                        i += 1
                        attention = payload_data[i]
                    elif packet == 5:  # meditation
                        i += 1
                        meditation = payload_data[i]
                    elif packet == 0x80:  # rawData
                        i += 1
                        raw_data = (payload_data[i + 1] << 8) | payload_data[i + 2]
                        # rawData = rawData * 1.8 / 4096 / 2000;
                        # print(raw_data)
                        i += 2
                    elif packet == 0x83:  # EEG values
                        i += 1
                        for k in range(i + 1, i + 26, 3):
                            value = (payload_data[k] << 16) | (payload_data[k + 1] << 8) | payload_data[k + 2]
                            eeg_values[(k - (i + 1)) // 3] = value
                        i += 24
                    else:
                        i += 1
        if big_packet:
            diction = {"poor_quality": poor_quality,  # 0-200
                       "attention": attention,
                       "meditation": meditation,
                       "eeg_values": eeg_values,
                       "raw_data": raw_data}
            big_packet = False
            return diction
        return -999
    return -999

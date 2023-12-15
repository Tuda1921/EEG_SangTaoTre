
def process_brainwave_data(payload_data):

    poor_quality = 200
    attention = 0
    meditation = 0
    eeg_values = [0] * 8
    raw_data = 0

    i = 0
    while i < len(payload_data):
        packet = payload_data[i]
        if packet == 2:  # poorQuality
            i += 1
            poor_quality = payload_data[i]
        elif packet == 4:  # attention
            i += 1
            attention = payload_data[i]
        elif packet == 5:  # meditation
            i += 1
            meditation = payload_data[i]
        elif packet == 0x80:  # rawData
            i += 1
            raw_data = (payload_data[i + 1] << 8) | payload_data[i + 2]
            i += 2
        elif packet == 0x83:  # EEG values
            i += 1
            for k in range(i + 1, i + 26, 3):
                value = (payload_data[k] << 16) | (payload_data[k + 1] << 8) | payload_data[k + 2]
                eeg_values[(k - (i + 1)) // 3] = value
            i += 24
        else:
            i += 1

    return poor_quality, attention, meditation, eeg_values, raw_data
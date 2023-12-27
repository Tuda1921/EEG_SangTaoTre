import serial

# Constants
SYNC_BYTE = bytes([170])
DEBUG_OUTPUT = False

# Serial port settings
SERIAL_PORT = 'COM8'  # Replace with the appropriate serial port
BAUD_RATE = 57600

# Initialize the serial port
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)


def read_one_byte():
    while ser.in_waiting == 0:
        pass
    byte_read = ser.read(1)

    if DEBUG_OUTPUT:
        print(byte_read.decode(), end='')  # Echo the same byte out the console (for debug purposes)

    return byte_read


def process_data():
    # Check for sync bytes
    if read_one_byte() == SYNC_BYTE and read_one_byte() == SYNC_BYTE:
        payload_length = read_one_byte()[0]

        if payload_length > 169:
            return

        generated_checksum = 0
        payload_data = []

        for _ in range(payload_length):
            payload_byte = read_one_byte()[0]
            payload_data.append(payload_byte)
            generated_checksum += payload_byte

        checksum = read_one_byte()[0]
        generated_checksum = 255 - generated_checksum

        if checksum == generated_checksum:
            poor_quality = 200
            attention = 0
            meditation = 0
            eeg_values = [0] * 8

            i = 0
            while i < payload_length:
                data_byte = payload_data[i]

                if data_byte == 2:  # poorQuality
                    i += 1
                    if i < payload_length:
                        poor_quality = payload_data[i]
                elif data_byte == 4:  # attention
                    i += 1
                    if i < payload_length:
                        attention = payload_data[i]
                elif data_byte == 5:  # meditation
                    i += 1
                    if i < payload_length:
                        meditation = payload_data[i]
                elif data_byte == 0x80:  # rawData
                    i += 1
                    if i + 2 < payload_length:
                        raw_data = (payload_data[i + 1] << 8) | payload_data[i + 2]
                        print(raw_data)
                        i += 2
                elif data_byte == 0x83:  # analyze 8 columns of brainwave data
                    i += 1
                    if i + 25 < payload_length:
                        for k in range(i + 1, i + 26, 3):
                            eeg_values[(k - (i + 1)) // 3 + 1] = (payload_data[k] << 16) | (
                                        (payload_data[k + 1] << 8) | payload_data[k + 2])
                        i += 24
                else:
                    i += 1

            # if not DEBUG_OUTPUT:
            #     # Add your code here
            #     if DEBUG_OUTPUT:
            #         print(poor_quality, attention, meditation, eeg_values)

        else:
            # Checksum error
            pass


# Main loop
while True:
    process_data()
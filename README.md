read_register.py

This script will read modbus TCP registers from an RS485 to TCP device

Update the below values in the script to your needs

TCP_IP = "192.168.1.10"  # Replace with your device's IP address
TCP_PORT = 502            # Default Modbus TCP port
SLAVE_ID = 1              # Replace with your Modbus slave ID
START_REGISTER = 240      # Starting register address
NUMBER_OF_REGISTERS = 30  # Number of registers to read in range

REMARK: this is a test script.

Handling Large Ranges:
  Modbus devices typically limit the number of registers that can be read in a single request (e.g., 125 or 120 registers). Check your device’s documentation for the maximum allowed range.

I used a waveshare "RS485 TO POE ETH (B)", to read the values of an Oxilife pool Hydrolyse (also known as Neopool, Sugar Valley, ...)

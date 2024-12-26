from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException

# Configuration
TCP_IP = "192.168.1.10"  # Replace with your device's IP address
TCP_PORT = 502            # Default Modbus TCP port
SLAVE_ID = 1              # Replace with your Modbus slave ID
START_REGISTER = 240      # Starting register address
NUMBER_OF_REGISTERS = 30  # Number of registers to read in range



try:
    # Connect to the Modbus device
    client = ModbusTcpClient(host=TCP_IP, port=TCP_PORT)
    connection = client.connect()
    
    if client.connect():
        print("Connection successful!")
    else:
        print("Connection failed!")

    if connection:
        # Read a range of holding registers
        response = client.read_holding_registers(
            address=START_REGISTER,
            count=NUMBER_OF_REGISTERS,
            slave=SLAVE_ID  # Use 'slave' to specify the Modbus ID
        )

        if not response.isError():  # Check for errors
            # Print the register values
            print(f"Register values from {START_REGISTER} to {START_REGISTER + NUMBER_OF_REGISTERS - 1}:")
            
            # Print register IDs and values
            for i, value in enumerate(response.registers):
                register_id = START_REGISTER + i
                print(f"Register {register_id}: {value}")
            
        else:
            print(f"Error reading registers: {response}")

    else:
        print("Unable to connect to the Modbus TCP device.")

except ModbusException as e:
    print(f"Modbus error: {e}")

finally:
    # Close the connection
    client.close()

from netmiko import ConnectHandler
# from getpass import getpass
# from datetime import datetime

# Start clock
# start_time = datetime.now()


class NetworkManager:
    def __init__(self, deviceType, host, username, password, numDevices):
        # Global Environment Variables
        self.deviceType = deviceType
        self.host = host
        self.userName = username
        self.password = password
        self.numDevices = numDevices
        self.devices = {}
        self.connection = None
        self.interface = []

    # Define Number of Devices
    def defdevices(self):
        for index in range(self.numDevices):
            self.devices[index] = {
                'device_type': self.deviceType[index],  # Assuming all devices are of the same type
                'host': self.host[index],
                'username': self.userName,
                'password': self.password,
            }

    def defports(self, numPorts, intfcName):
        self.interface = [intfcName + f"{index+1}" for index in range(numPorts)]

    # Connect to Device
    def connect(self, devices, devicenum):
        try:
            self.connection = ConnectHandler(**self.devices[devicenum])
            print(self.connection.find_prompt())
        except Exception as e:
            print(f"Connection Failure: Device {devicenum}. Error: {str(e)}")

    # Check status of interfaces
    def checkStatus(self, devices, devicenum):
        # Establish the connection
        net_connect = ConnectHandler(**devices[devicenum])
        output = net_connect.send_command('show ip interface brief')
        print("Status of Interfaces:\n", output)

    # Bring Port Up
    def portup(self, devices, devicenum, portNum):

        # Ports must already be defined
        config_commands = [f'interface {self.interface[portNum]}', 'no shutdown']
        net_connect = ConnectHandler(**devices[devicenum])
        output = net_connect.send_config_set(config_commands)
        print(f"Bringing up {self.interface[portNum]}:\n", output)
        net_connect.disconnect()  # New Update

    # Shut Port Down
    def portdown(self, devices, devicenum, portNum):

        # Ports must already be defined
        config_commands = [f'interface {self.interface[portNum]}', 'shutdown']
        net_connect = ConnectHandler(**devices[devicenum])
        output = net_connect.send_config_set(config_commands)
        print(f"Shutting Down {self.interface[portNum]}:\n", output)
        net_connect.disconnect()  # New Update

    # Pings a Given Network
    def ping(self, devices, devicenum):
        # Define the network to ping
        network = '8.8.8.8'

        # Ping the network
        net_connect = ConnectHandler(**devices[devicenum])
        output = net_connect.send_command(f'ping {network}')
        print(f"Pinging {network}:\n", output)

    def disconnect(self, devices, devicenum):
        net_connect = ConnectHandler(**devices[devicenum])
        net_connect.disconnect()
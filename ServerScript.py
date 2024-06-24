from Connection import NetworkManager
import time

# Define device connection details
device_type = ['cisco_ios', 'cisco_ios', 'cisco_ios', 'cisco_ios', 'cisco_ios']
hosts = ['172.25.0.133', '172.25.0.132', '172.25.0.134', '172.25.0.136', '172.25.0.137']
username = 'lperpall'
password = '$#P@$$w0rd1'
numDevices = len(hosts)
intrfaceName = 'GigabitEthernet1/0/'
numPorts = 18

# Instantiate the NetworkManager class & define Devices, Ports
RWBServer = NetworkManager(device_type, hosts, username, password, numDevices)
RWBServer.defdevices()
RWBServer.defports(numPorts, intrfaceName)


# main Logic

# Try Connection To Ports & Shuts down 1-18 on all Switches
for devices in range(RWBServer.numDevices):
    RWBServer.connect(RWBServer.devices, devices)
    for index in range(numPorts):
        RWBServer.portdown(RWBServer.devices, devices, index)
    print(f"Device{devices}, {numPorts} Ports Shut Down. Complete!")
    # Wait for 4 minutes
    time.sleep(30 * 60)  # 30 minutes * 60 seconds per minute

# Try Bring ports up
for devices in range(RWBServer.numDevices):
    RWBServer.connect(RWBServer.devices, devices)

    # Try Ports 1-8 Bring Up
    intv1 = 8
    for index in range(intv1):
        RWBServer.portup(RWBServer.devices, devices, index)

    print(f"Device{devices}, {intv1} Ports Is Up. Complete!")
    # Wait for 4 minutes
    time.sleep(4 * 60)  # 4 minutes / 60 seconds per minute

    # Try Ports 1-8 Bring Up
    intv2_start = 8
    intv2_end = 18

    for port_index in range(intv2_start, intv2_end):
        RWBServer.portup(RWBServer.devices, devices, port_index)
    print(f"Device {devices}, Ports {intv2_start + 1}-{intv2_end} are up. Complete!")
    # Wait for 4 minutes
    time.sleep(4 * 60)  # 4 minutes / 60 seconds per minute

    # Disconnect
    RWBServer.disconnect(RWBServer.devices, devices)
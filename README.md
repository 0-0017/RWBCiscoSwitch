# RWBCiscoSwitch
Network Automation Project Overview This project aims to automate various network management tasks using the Netmiko Python library. The current functionality allows users to:

Check the status of network interfaces. Bring specific ports down and up on a schedule. Perform a ping test to a specified network. Securely handle user credentials. Functionalities

Check Status of Interfaces The script connects to a Cisco IOS device and retrieves the status of all network interfaces using the show ip interface brief command. The output is printed to the console.

Shut Down / Bring Up Ports The script can manage the state of specific network interfaces. It performs the following actions:

Brings a specified range of ports down using the shutdown command. Brings a specified range of ports up using the no shutdown command. Both actions are executed in configuration mode and the results are printed to the console. Detailed Logic: Shutdown Ports 1-18 on All Devices

Connect to each device. Shut down ports 1-18. Wait for 30 minutes before proceeding to the next device. Bring Up Ports in Intervals

Connect to each device. Bring up ports 1-8. Wait for 4 minutes. Bring up ports 9-18. Disconnect from the device. 3. Ping Test The script performs a ping test to a specified network (e.g., 8.8.8.8). The result of the ping test is printed to the console.

Secure Credential Handling The script uses the getpass library to securely prompt the user for their password when establishing a connection to the network device.
Script Structure Initialization: Define device connection details and instantiate the NetworkManager class. Define Devices and Ports: Initialize devices and ports. Shutdown Ports: Connect to each device. Shut down ports 1-18. Wait for 30 minutes. Bring Up Ports: Connect to each device. Bring up ports 1-8. Wait for 4 minutes. Bring up ports 9-18. Disconnect from the device. Disconnect: Ensure all devices are disconnected after operations are complete.

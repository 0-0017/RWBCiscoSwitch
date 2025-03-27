# RWBCiscoSwitch  

## Network Automation Project Overview  
This project was developed for my **previous employer** to automate network management tasks on Cisco switches using the Netmiko Python library. It provides functionalities for:  

- Checking the status of network interfaces.  
- Bringing specific ports down and up on a schedule.  
- Performing a ping test to a specified network.  
- Securely handling user credentials.  

### Notes:
**Tested on Windows only!**
**Credentials Modified For Safety & Privacy!**
**Simple Script Used For One Specific Task, With Potential For Improvement & Scalabiliy!**

---

## Table of Contents  
- [Features](#features)  
  - [Check Status of Interfaces](#check-status-of-interfaces)  
  - [Shut Down / Bring Up Ports](#shut-down--bring-up-ports)  
  - [Ping Test](#ping-test)  
  - [Secure Credential Handling](#secure-credential-handling)  
- [Script Structure](#script-structure)  
- [Installation & Setup](#installation--setup)  
- [Usage](#usage)  

---

## Features  

### Check Status of Interfaces  
The script connects to a Cisco IOS device and retrieves the status of all network interfaces using the `show ip interface brief` command. The output is printed to the console.  

### Shut Down / Bring Up Ports  
The script manages the state of specific network interfaces using:  

- `shutdown` command to disable ports.  
- `no shutdown` command to re-enable ports.  

**Detailed Logic:**  
1. Shut down **ports 1-18** on all devices.  
   - Connect to each device.  
   - Shut down ports 1-18.  
   - Wait for **30 minutes** before proceeding to the next device.  
2. Bring up ports in intervals:  
   - Connect to each device.  
   - Bring up **ports 1-8** → Wait **4 minutes**.  
   - Bring up **ports 9-18** → Wait **4 minutes**.  
   - Disconnect from the device.  

### Ping Test  
The script performs a ping test to a specified network (default: `8.8.8.8`). The result is printed to the console.  

### Secure Credential Handling  
The script uses the `getpass` library to securely prompt for user credentials when establishing a connection to the network device.  

---

## Script Structure  
1. **Initialization:** Define device connection details and instantiate the `NetworkManager` class.  
2. **Define Devices & Ports:** Initialize devices and interfaces.  
3. **Shutdown Ports:**  
   - Connect to each device.  
   - Shut down **ports 1-18**.  
   - Wait **30 minutes**.  
4. **Bring Up Ports:**  
   - Connect to each device.  
   - Bring up **ports 1-8**, wait **4 minutes**.  
   - Bring up **ports 9-18**, wait **4 minutes**.  
   - Disconnect.  

---

## Installation & Setup  
### Prerequisites  
Ensure you have Python installed on your system. Then, install the required dependencies:  

```sh
pip install -r requirements.txt

### Requirements:
  - netmiko
  - requests
  - pyinstaller

## Usage
```sh
python main.py

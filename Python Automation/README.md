# Enterprise Network Lab Automation

##  Overview & Motivation
After successfully configuring this Enterprise Network Lab manually, I decided to take it a step further by automating the entire process. The goal was to eliminate repetitive tasks, save time, simplify future modifications, and ensure the network is easily scalable when adding new devices. 

To achieve this, I wrote a Python script (a solid version 1.0, with plans to optimize it further) that deploys the entire configuration in mere seconds, replacing hours of manual CLI input.

---

## How It Works (The "Zero-Day" Setup)

When starting a fresh lab on PNETLab, the devices are completely blank (factory reset, with no IP addresses or initial configurations). This script is designed to handle this "Zero-Day" environment by leveraging the emulator's console architecture:

* **Emulator IP:** PNETLab uses a single IP address for the entire Virtual Machine (in this script, it defaults to `192.168.83.129`).
* **Console Ports:** Each virtual router or switch is assigned a unique, dedicated port for console access (e.g., `30418`, `30421`).

### How to Find Your Device Ports
You can easily find the specific port for any device by simply **hovering your mouse over the node** in your PNETLab topology. The port number will appear next to the device name.

---

## Technical Execution

1. **Initial Connection:** Because the devices lack IP addresses, the script uses the **Netmiko** library with the `cisco_ios_telnet` device type. By targeting the specific VM IP and the unique device ports, the script connects exactly as if a physical console cable were plugged in.
2. **Pushing Configurations:** The script iterates through the topology device by device. It establishes a connection and pushes the predefined configuration lists, which include protocols and technologies like **VLANs, OSPF, EtherChannel, and HSRP**.
3. **Enabling Remote Management:** As part of the automated deployment, the script pushes **SSH configurations** and creates local credentials. This crucial step ensures that all devices are immediately ready for secure, standard remote management for any future operations.

---

##  Customization & Usage Guide
This script serves as a foundational template. Before running it in your own environment, please make the following adjustments:

* **Update the PNETLab IP:** Change `PNET_IP = "192.168.83.129"` to match your local VM's IP.
* **Update the Ports:** Modify the port numbers in the `Device Definitions` section based on what appears in your specific topology.
* **Tweak the Configurations:** Adjust the IP addressing, VLAN IDs, and routing parameters inside the `cmds` lists to fit your specific network design.

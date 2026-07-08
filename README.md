# Enterprise Network Lab

A Cisco Enterprise Network Lab designed to simulate a real-world enterprise environment using a three-tier architecture.

## Features

- Enterprise Network Design
- Three-Tier Architecture
  - Core Layer
  - Distribution Layer
  - Access Layer
- VLANs
- VTP Version 3
- Inter-VLAN Routing
- OSPF
- HSRP
- EtherChannel (LACP)
- Rapid PVST+
- DHCP
- Trunking (802.1Q)
- ISP Simulation
- Network Troubleshooting

---

## Topology

The lab simulates an enterprise network connected to an ISP router to provide a realistic routing environment.

### Network Layers

- Core Layer
- Distribution Layer
- Access Layer
- Edge Router
- ISP

---

## Technologies Used

| Technology | Description |
|------------|-------------|
| VLAN | Network Segmentation |
| VTP v3 | Centralized VLAN Management |
| OSPF | Dynamic Routing |
| HSRP | Gateway Redundancy |
| EtherChannel | Link Aggregation (LACP) |
| Rapid PVST+ | Loop Prevention |
| DHCP | Automatic IP Assignment |
| Trunk | VLAN Transportation |
| Cisco IOS | Device Configuration |

---

## Project Structure

```
Enterprise-Network-Lab/
│
├── Config/
│   └── Config.html
│
├── Troubleshooting/
│
├── Topology/
│
└── README.md
```

---

## Configuration Files

All device configurations are available inside the **Config** folder.

The configuration file is provided as an **HTML** file for easier navigation.

If GitHub displays it as plain text:

1. Download the file.
2. Open **Notepad**.
3. Paste the content.
4. Save the file with the **.html** extension.
5. Open it using any web browser.

The page contains all device configurations organized by device name for quick access.

---

## Future Improvements

The next phase of this project will focus on **Network Automation using Python**, including:

- Automated Configuration Deployment
- SSH Automation using Netmiko
- Verification Scripts

---

## Author

**Ali Amin Salah**

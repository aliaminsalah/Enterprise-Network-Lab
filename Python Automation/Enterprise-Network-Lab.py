from netmiko import ConnectHandler
import time

# PNETLab IP Address
PNET_IP = "192.168.83.129"

# ==========================================
# 1. Device Definitions
# ==========================================

csw1 = {
    "device_type": "cisco_ios_telnet",
    "host": PNET_IP,
    "port": 30418, 
    "secret": "", 
}

csw2 = {
    "device_type": "cisco_ios_telnet",
    "host": PNET_IP,
    "port": 30419,  
    "secret": "", 
}

dsw1 = {
    "device_type": "cisco_ios_telnet",
    "host": PNET_IP,
    "port": 30421,  
    "secret": "", 
}

dsw2 = {
    "device_type": "cisco_ios_telnet",
    "host": PNET_IP,
    "port": 30420,  
    "secret": "", 
}

asw1 = {
    "device_type": "cisco_ios_telnet",
    "host": PNET_IP,
    "port": 30422,  
    "secret": "", 
}

asw2 = {
    "device_type": "cisco_ios_telnet",
    "host": PNET_IP,
    "port": 30423, 
    "secret": "", 
}

r1 = {
    "device_type": "cisco_ios_telnet",
    "host": PNET_IP,
    "port": 30416,  
    "secret": "", 
}

# ==========================================
# 2. Configuration Commands Lists
# ==========================================

# --- CSW1 ---
csw1_cmds = [
    "hostname CSW1",
    "no ip domain-lookup",
    "ip domain-name campus.local",
    "username admin privilege 15 secret admin123",
    "crypto key generate rsa modulus 2048",
    "ip ssh version 2",
    "line vty 0 4",
    "login local",
    "transport input ssh",
    "exit",
    "vtp domain CAMPUS",
    "vtp version 3",
    "vtp mode server",
    "vtp password cisco123",
    "do vtp primary force",
    "ip routing",
    "ipv6 unicast-routing",
    "interface Loopback0",
    "ip address 10.0.128.2 255.255.255.255",
    "interface Ethernet0/0",
    "description LINK_TO_R1",
    "no switchport",
    "ip address 10.0.131.2 255.255.255.252",
    "no shutdown",
    "interface Vlan99",
    "ip address 10.0.131.9 255.255.255.248",
    "no shutdown",
    "exit",
    "router ospf 1",
    "router-id 10.0.128.2",
    "network 10.0.131.0 0.0.0.255 area 0",
    "interface range Ethernet0/1 - 2",
    "description LACP_TO_CSW2",
    "channel-group 1 mode active",
    "no shutdown",
    "exit",
    "interface Port-channel 1",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "no shutdown",
    "exit",
    "interface range Ethernet0/3 , Ethernet1/0",
    "description TRUNKS_TO_DSW",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "no shutdown"
]

csw1_vlans = [
    "vlan 10", "name CLIENTS",
    "vlan 20", "name VOICE",
    "vlan 30", "name PRINTERS",
    "vlan 40", "name MANAGEMENT",
    "vlan 99", "name OSPF_TRANSIT"
]

# --- CSW2 ---
csw2_cmds = [
    "hostname CSW2",
    "no ip domain-lookup",
    "ip domain-name campus.local",
    "username admin privilege 15 secret admin123",
    "crypto key generate rsa modulus 2048",
    "ip ssh version 2",
    "line vty 0 4",
    "login local",
    "transport input ssh",
    "exit",
    "vtp domain CAMPUS",
    "vtp version 3",
    "vtp mode client",
    "vtp password cisco123",
    "ip routing",
    "ipv6 unicast-routing",
    "interface Loopback0",
    "ip address 10.0.128.3 255.255.255.255",
    "interface Ethernet0/0",
    "description LINK_TO_R1",
    "no switchport",
    "ip address 10.0.131.6 255.255.255.252",
    "no shutdown",
    "interface Vlan99",
    "ip address 10.0.131.10 255.255.255.248",
    "no shutdown",
    "exit",
    "router ospf 1",
    "router-id 10.0.128.3",
    "network 10.0.131.0 0.0.0.255 area 0", 
    "interface range Ethernet0/1 - 2",
    "description LACP_TO_CSW1",
    "channel-group 1 mode passive",
    "no shutdown",
    "exit",
    "interface Port-channel 1",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "no shutdown",
    "exit",
    "interface range Ethernet0/3 , Ethernet1/0",
    "description TRUNKS_TO_DSW",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "no shutdown"
]

# --- DSW1 ---
dsw1_cmds = [
    "hostname DSW1",
    "ip domain-name campus.local",
    "username admin privilege 15 secret admin123",
    "crypto key generate rsa modulus 2048",
    "ip ssh version 2",
    "line vty 0 4",
    "login local",
    "transport input ssh",
    "exit",
    "vtp domain CAMPUS",
    "vtp version 3",
    "vtp mode client",
    "vtp password cisco123",
    "spanning-tree mode rapid-pvst",
    "spanning-tree vlan 10,20,30,40 root primary",
    "interface range Ethernet0/2 - 3",
    "description LACP_TO_DSW2",
    "channel-group 2 mode active",
    "no shutdown",
    "exit",
    "interface Port-channel 2",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "no shutdown",
    "exit",
    "interface range Ethernet0/0 - 1",
    "description TRUNKS_TO_CSW",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "no shutdown",
    "exit",
    "ip routing",
    "interface Vlan10",
    "ip address 10.0.0.1 255.255.255.128",
    "standby 10 ip 10.0.0.126",
    "standby 10 priority 110",
    "standby 10 preempt",
    "no shutdown",
    "interface Vlan40",
    "ip address 10.0.0.209 255.255.255.248",
    "standby 40 ip 10.0.0.214",
    "standby 40 priority 110",
    "standby 40 preempt",
    "no shutdown",
    "interface Vlan99",
    "ip address 10.0.131.11 255.255.255.248",
    "no shutdown",
    "router ospf 1",
    "router-id 10.0.128.4",
    "network 10.0.0.0 0.0.0.255 area 0",
    "network 10.0.131.0 0.0.0.255 area 0"
]

# --- DSW2 ---
dsw2_cmds = [
    "hostname DSW2",
    "ip domain-name campus.local",
    "username admin privilege 15 secret admin123",
    "crypto key generate rsa modulus 2048",
    "ip ssh version 2",
    "line vty 0 4",
    "login local",
    "transport input ssh",
    "exit",
    "vtp domain CAMPUS",
    "vtp version 3",
    "vtp mode client",
    "vtp password cisco123",
    "spanning-tree mode rapid-pvst",
    "spanning-tree vlan 10,20,30,40 root secondary",
    "interface range Ethernet0/2 - 3",
    "description LACP_TO_DSW1",
    "channel-group 2 mode passive",
    "no shutdown",
    "exit",
    "interface Port-channel 2",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "no shutdown",
    "exit",
    "interface range Ethernet0/0 - 1",
    "description TRUNKS_TO_CSW",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "no shutdown",
    "exit",
    "ip routing",
    "interface Vlan10",
    "ip address 10.0.0.2 255.255.255.128",
    "standby 10 ip 10.0.0.126",
    "standby 10 priority 105",
    "standby 10 preempt",
    "no shutdown",
    "interface Vlan40",
    "ip address 10.0.0.210 255.255.255.248",
    "standby 40 ip 10.0.0.214",
    "standby 40 priority 105",
    "standby 40 preempt",
    "no shutdown",
    "interface Vlan99",
    "ip address 10.0.131.12 255.255.255.248",
    "no shutdown",
    "router ospf 1",
    "router-id 10.0.128.5",
    "network 10.0.0.0 0.0.0.255 area 0",
    "network 10.0.131.0 0.0.0.255 area 0"
]

# --- ASW1 ---
asw1_cmds = [
    "hostname ASW1",
    "ip domain-name campus.local",
    "username admin privilege 15 secret admin123",
    "crypto key generate rsa modulus 2048",
    "ip ssh version 2",
    "line vty 0 4",
    "login local",
    "transport input ssh",
    "exit",
    "vtp domain CAMPUS",
    "vtp version 3",
    "vtp mode client",
    "vtp password cisco123",
    "interface range Ethernet0/0 - 1",
    "description TRUNKS_TO_DSW",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "no shutdown",
    "exit",
    "interface Ethernet0/2",
    "description LINK_TO_PC",
    "switchport mode access",
    "switchport access vlan 10",
    "spanning-tree portfast edge",
    "spanning-tree bpduguard enable",
    "no shutdown",
    "interface Vlan40",
    "ip address 10.0.0.211 255.255.255.248",
    "no shutdown",
    "ip default-gateway 10.0.0.214"
]

# --- ASW2 ---
asw2_cmds = [
    "hostname ASW2",
    "ip domain-name campus.local",
    "username admin privilege 15 secret admin123",
    "crypto key generate rsa modulus 2048",
    "ip ssh version 2",
    "line vty 0 4",
    "login local",
    "transport input ssh",
    "exit",
    "vtp domain CAMPUS",
    "vtp version 3",
    "vtp mode client",
    "vtp password cisco123",
    "interface range Ethernet0/0 - 1",
    "description TRUNKS_TO_DSW",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "no shutdown",
    "exit",
    "interface Ethernet0/2",
    "description LINK_TO_PC",
    "switchport mode access",
    "switchport access vlan 10",
    "spanning-tree portfast edge",
    "spanning-tree bpduguard enable",
    "no shutdown",
    "interface Vlan40",
    "ip address 10.0.0.212 255.255.255.248",
    "no shutdown",
    "ip default-gateway 10.0.0.214"
]

# --- R1 ---
r1_cmds = [
    "hostname R1",
    "no ip domain-lookup",
    "ip domain-name campus.local",
    "username admin privilege 15 secret admin123",
    "crypto key generate rsa modulus 2048",
    "ip ssh version 2",
    "line vty 0 4",
    "login local",
    "transport input ssh",
    "exit",
    "ip dhcp excluded-address 10.0.0.1 10.0.0.10",
    "ip dhcp excluded-address 10.0.0.128 10.0.0.138",
    "ip dhcp pool VLAN10_CLIENTS",
    "network 10.0.0.0 255.255.255.128",
    "default-router 10.0.0.126",
    "ip dhcp pool VLAN20_VOICE",
    "network 10.0.0.128 255.255.255.192",
    "default-router 10.0.0.190",
    "ipv6 unicast-routing",
    "interface Loopback0",
    "ip address 10.0.128.1 255.255.255.255",
    "ipv6 address 2001:DB8:0:128::1/128",
    "ipv6 ospf 1 area 0",
    "interface Ethernet0/0",
    "description LINK_TO_CSW1",
    "ip address 10.0.131.1 255.255.255.252",
    "ipv6 address 2001:DB8::1:1/127",
    "ipv6 ospf 1 area 0",
    "no shutdown",
    "interface Ethernet0/1",
    "description LINK_TO_CSW2",
    "ip address 10.0.131.5 255.255.255.252",
    "ipv6 address 2001:DB8::2:1/127",
    "ipv6 ospf 1 area 0",
    "no shutdown",
    "interface Ethernet0/2",
    "description LINK_TO_ISP",
    "ip address 172.16.1.1 255.255.255.252",
    "no shutdown",
    "ip route 0.0.0.0 0.0.0.0 172.16.1.2",
    "router ospf 1",
    "router-id 10.0.128.1",
    "network 10.0.128.1 0.0.0.0 area 0",
    "network 10.0.131.0 0.0.0.3 area 0",
    "network 10.0.131.4 0.0.0.3 area 0",
    "default-information originate"
]

# ==========================================
# 3. Connection and Execution Function
# ==========================================

def push_config(device, cmds, device_name):
    print(f"\n[*] Connecting to {device_name}...")
    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable() 
        print(f"[+] Connected to {device_name}. Sending configurations...")
        output = net_connect.send_config_set(cmds)
        print(output)
        return net_connect
    except Exception as e:
        print(f"[-] Failed to connect/configure {device_name}: {e}")
        return None

# ==========================================
# 4. Execution Flow
# ==========================================

print("Starting Campus Network Automation Script...")

# 1. CSW1 (Primary Core)
csw1_conn = push_config(csw1, csw1_cmds, "CSW1")
if csw1_conn:
    time.sleep(3) 
    vlan_output = csw1_conn.send_config_set(csw1_vlans)
    print(vlan_output)
    csw1_conn.disconnect()

# 2. CSW2 (Secondary Core)
csw2_conn = push_config(csw2, csw2_cmds, "CSW2")
if csw2_conn: 
    csw2_conn.disconnect()

# 3. DSW1 (Primary Distribution)
dsw1_conn = push_config(dsw1, dsw1_cmds, "DSW1")
if dsw1_conn: 
    dsw1_conn.disconnect()

# 4. DSW2 (Secondary Distribution)
dsw2_conn = push_config(dsw2, dsw2_cmds, "DSW2")
if dsw2_conn: 
    dsw2_conn.disconnect()

# 5. ASW1 (Access Switch 1)
asw1_conn = push_config(asw1, asw1_cmds, "ASW1")
if asw1_conn: 
    asw1_conn.disconnect()

# 6. ASW2 (Access Switch 2)
asw2_conn = push_config(asw2, asw2_cmds, "ASW2")
if asw2_conn: 
    asw2_conn.disconnect()

# 7. R1 (Edge Router)
r1_conn = push_config(r1, r1_cmds, "R1")
if r1_conn: 
    r1_conn.disconnect()

print("\n[+] FULL Automation Script Completed successfully!")

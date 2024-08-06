# arp-spoofer 🕵️‍♂️

`arp-spoofer` is a Python tool designed for ARP (Address Resolution Protocol) spoofing. It allows you to intercept network traffic between two devices on a local network by impersonating their ARP entries.
-------------------------------------------
## 🚀 Features

- **Targeted ARP Spoofing**: Specify target and gateway IP addresses to control the spoofing.
- **Full Duplex Mode**: Optionally enable or disable full duplex communication.
- **Custom Interface Selection**: Choose which network interface to use for the attack.
-------------------------------------------
## 🛠️ Dependencies

'''
python3
python3-pip
'''
-------------------------------------------
## 📦 Installation

To get started with `arp-spoofer`, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/ilolm/arp-spoofer.git
cd arp-spoofer
pip3 install -r requirements.txt
chmod +x arp_spoof.py
```
-------------------------------------------
## 🎮 Usage

Run the `arp_spoofer.py` script with the required options. Root privileges are required to execute ARP spoofing.

```bash
sudo ./arp_spoof.py [options]
```
-------------------------------------------
### Options

- `-h, --help`: Show this help message and exit.
- `-t TARGET_IP, --target=TARGET_IP`: Enter the target IP address.
- `-g GATEWAY_IP, --gateway=GATEWAY_IP`: Enter the gateway IP address.
- `-f FULLDUPLEX, --fullduplex=FULLDUPLEX`: Set full duplex mode? Set True or False. Default=True.
- `-i IFACE, --iface=IFACE`: Select a network interface. Default is "eth0".
-------------------------------------------
### Example

```bash
sudo ./arp_spoof.py -t 192.168.1.10 -g 192.168.1.1 -f True -i wlan0
```

This command will spoof the ARP entries for the target IP `192.168.1.10` and the gateway IP `192.168.1.1` using the `wlan0` interface with full duplex enabled.
-------------------------------------------
## ⚠️ Disclaimer

This tool is intended for educational purposes only. Use it responsibly and only on networks where you have permission to perform such activities. Misuse of this tool can lead to legal consequences.
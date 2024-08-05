# arp-spoofer

**DEPENDENCIES:**
```
python3
```

-------------------------------------------------------

**INSTALLATION:**
```
git clone https://github.com/ilolm/arp-spoofer.git
cd arp-spoofer
pip3 install -r requirements.txt
chmod +x arp_spoof.py
```

-------------------------------------------------------

**USAGE:**
```
Usage: sudo ./arp_spoof.py [options]

Options:
  -h, --help            show this help message and exit
  -t TARGET_IP, --target=TARGET_IP
                        Enter target IP address.
  -g GATEWAY_IP, --gateway=GATEWAY_IP
                        Enter gateway IP address.
  -f FULLDUPLEX, --fullduplex=FULLDUPLEX
                        Set fullduplex? Set True or False. Default=True.
  -i IFACE, --iface=IFACE
                        Select an interface. Default - "eth0"
```

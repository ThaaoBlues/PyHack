from scapy.all import *
from scapy.layers.dns import DNSRR
from scapy.layers.inet import IP
import socket
from scapy.utils import PcapWriter
from platform import system


def callback(packet):
    pktdump = PcapWriter("sniff_results.pcap", append=True, sync=True)
    pktdump.write(packet)
    pktdump.close()

    if packet.haslayer(DNSRR):
        if isinstance(packet.an, DNSRR):
            if packet.haslayer(IP):
                print("from : {} to {} :: {}".format(packet[IP].src,packet[IP].dst,packet.an.rrname))





sniff(prn=callback)


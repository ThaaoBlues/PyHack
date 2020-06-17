from scapy.all import *
import socket
from scapy.utils import PcapWriter


def callback(packet):
    pktdump = PcapWriter("sniff_results.pcap", append=True, sync=True)
    pktdump.write(packet)
    pktdump.close()

    if packet.haslayer(DNSRR):
        if isinstance(packet.an, DNSRR):
            if packet.haslayer(IP):
                print("from : {} to {} :: {}".format(packet[IP].src,packet[IP].dst,packet.an.rrname))

sniff(prn=callback)


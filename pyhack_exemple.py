import port_scanner, DNS_sniffer, keylogger_recever, virus_scanner, simple_DHCP_scan, wordlist_maker
from multiprocessing import freeze_support


if __name__ == "__main__":
    freeze_support()
    while True:
        cmd = input("select a module : ")
        if "port scanner" in cmd:
            ps = port_scanner.port_scanner()
            ps.scan(input("IP : "),max=int(input("PORT RANGE : ")))

        if "wordlist_maker" in cmd:
            wordlist_maker1 = wordlist_maker.wordlist_maker()

        if "dns sniffer" in cmd:
            dns = DNS_sniffer.DNS_sniffer()

        if "keylogger recever" in cmd:
            klg_rcv = keylogger_recever.live_recever()

        if "virus scanner" in cmd:
            virus_scan = virus_scanner.virus_scanner()

        if "network scan" in cmd:
            netscan = simple_DHCP_scan.scanner()

        if "help" in cmd:
            print("""
            network scan : run the fastest host discovery scanner in the world
            virus scanner : scan the network to machines with a specific port open
            keylogger recever : run the live keyslogger recever that comes with the keylogger I wrote
            dns sniffer : ...all is in the name bro, it displays all the dns requests in human-friendly way
            wordlist maker : basic script to generate basic wordlists
            port scanner : scan all the ports from 1 to the max you specified on a target you specified
            
            """)

        else:
            print("[!] unknown command, type help to get a list of available commands.")

from scapy.all import * 
import socket
from io import StringIO

class scanner():
    def __init__(self,ip_range):
        if ip_range == "all":
            hostname = socket.gethostname()
            ip = socket.gethostbyname_ex(hostname)
            ip = str(ip[-1][-1])
            print("YOU :: {} :: {}".format(hostname,ip))
            base_ip = ip.split(sep=".")
            base = "{}.{}.{}.1/24".format(base_ip[0],base_ip[1],base_ip[2])
            self.scan(base,base_ip[0])

        else:
            self.scan(ip_range)


    def scan(self,ip,first_3):
        output = []
        i = 0
        with Capturing(output) as output:
            arping(ip)
        for line in output:
            lines = line.split()
            for addr in lines:
                if addr[:3] in first_3:
                    i += 1
                    print("[{}] {} :: {} ".format(i,line,str(socket.gethostbyaddr(addr)[0])))


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

if __name__ == "__main__":
    scan = scanner("all")

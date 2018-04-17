from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException

class items:
	def __init__(self,port,protocol,state,service):
		self.port=port
		self.protocol=protocol
		self.state=state
		self.service=service
	def serialize(self):
		return { 'port':self.port, 'protocol':self.protocol, 'state':self.state, 'service':self.service}

def ret_scan(nmproc):
    parsed = NmapParser.parse(nmproc.stdout)

    lst=[]

    for host in parsed.hosts:
        for serv in host.services:
            item=items(str(serv.port),serv.protocol,serv.state,serv.service);
            lst.append(item)
           
    return lst

def start_scan(website,scan_type):
    nmap_proc = NmapProcess(targets = website, options=scan_type)
    nmap_proc.sudo_run_background()    
    return nmap_proc
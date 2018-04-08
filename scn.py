import nmap

class items(object):
    def __init__(port,protocol,state,service):
        self.port=port
        self.protocol=protocol
        self.state=state
        self.service=service

def do_scan(website,flag):
	nmproc = nmap.PortScanner()
	nmproc.scan(website,arguments=flag)
	lst=[]
	for host in nmproc.all_hosts():

		for proto in nmproc[host].all_protocols():
			lproto=nmproc[host][proto].keys()

			for l in lproto:
				lst.append(items.__init__(l,proto,nmproc[host][proto][l]['state'],nmproc[host][proto][l]['name']))

	return lst
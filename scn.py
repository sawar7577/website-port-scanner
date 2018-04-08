import nmap


nm = nmap.PortScanner()


# nm.scan('www.gitaniketan.org',arguments='-O -sS')

# for host in nm.all_hosts():
 
#     for port in nm[host].all_protocols():
#         lport = nm[host][port].keys()
#         lport.sort()
    
#         for l in lport:
#             print ("port: {} service: {}").format(port,nm[host][port][l]['name'])
        
    
class items(object):
	def __init__(self,port,protocol,state,service):
		self.port=port
		self.protocol=protocol
		self.state=state
		self.service=service

def do_scan(website, flag):
	nmproc = nmap.PortScanner()
	nmproc.scan(website,arguments=flag)
	lst=[]
	for host in nmproc.all_hosts():
		for proto in nmproc[host].all_protocols():
			lproto=nmproc[host][proto].keys()
			for l in lproto:
				new_item = items(l,proto,nmproc[host][proto][l]['state'],nmproc[host][proto][l]['name'])
				lst.append(new_item)

	return lst

# k = do_scan("www.gitaniketan.org",'sV')
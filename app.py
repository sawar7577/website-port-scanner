from flask import Flask, session, render_template, Response,request, jsonify
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException
from time import sleep
import random
import string

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
        if len(host.hostnames):
            tmp_host = host.hostnames.pop()
        else:
            tmp_host = host.address

        for serv in host.services:
            item=items(str(serv.port),serv.protocol,serv.state,serv.service);
            lst.append(item)
            pserv = "{0:>5s}/{1:3s}  {2:12s}  {3}".format(
                    str(serv.port),
                    serv.protocol,
                    serv.state,
                    serv.service)
            if len(serv.banner):
                pserv += " ({0})".format(serv.banner)
            print(pserv)
    return lst
    # return [items.serialize() for item in lst]



nmap_queue = {}

app = Flask(__name__)

def generate_random_key(size=64, chars=string.ascii_uppercase + string.digits):
	return "asdasdasdasdsad"

@app.route('/',methods=['POST','GET'])
def index():
	if request.method == 'POST':
		website=request.form['website']
		
		key = "asdasd"

		nmap_proc = NmapProcess(targets = website, options="sV")
		nmap_proc.run_background()

		nmap_queue[key] = nmap_proc
		print(key in nmap_queue)
		return render_template('results.html', nmap_key = key, target_site = website)
	else:
		# if nid == "":
		return render_template('index.html',items=[])
		# else:
			# return render_template('index.html',items=ret_scan(nmap_queue[nid]))

@app.route('/res/<string:nid>')
def res(nid):
	return render_template('index.html',items=ret_scan(nmap_queue[nid]))



@app.route('/ajax/nmout/<string:nid>')
def update(nid):
	
	data = { "valid" : True }
	if str(nid) not in nmap_queue:
		data["valid"] = False
		return jsonify(data), 200

	data["progress"] = nmap_queue[nid].progress


	if not nmap_queue[nid].is_running():
		data["summary"] = nmap_queue[nid].summary

	return jsonify(data), 200


if __name__ == "__main__":
	app.run(debug=True)

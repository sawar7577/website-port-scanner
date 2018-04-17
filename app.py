from flask import Flask, session, render_template, Response,request, jsonify
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException
from time import sleep
import random
import string
import socket
from ipwhois import IPWhois
import port_scan

nmap_queue = {}

app = Flask(__name__)

def generate_random_key(size=64, chars=string.ascii_uppercase + string.digits):
	return "asdasdasdasdsad"

@app.route('/',methods=['POST','GET'])
def index():
	if request.method == 'POST':
		website=request.form['website']
		scan_type = request.form['scan_type']
		key = "asdasd"
		if scan_type == 'whois' :
			return look_up()
		else :	
			if scan_type == 'tcp':
				scan_type = '-sV'
			elif scan_type == 'udp':
				scan_type = '-sU'

			print (type(scan_type))		
			# print (nmap_proc.current_task)
			nmap_queue[key] = port_scan.start_scan(website,scan_type)
			print(key in nmap_queue)
			return render_template('results.html', nmap_key = key, target_site = website)
	else:
			return render_template('index.html')

@app.route('/res/<string:nid>')
def res(nid):
	items=port_scan.ret_scan(nmap_queue[nid])
	for item in items:
		print(item.port,item.protocol,item.state,item.service,end='\n')
	print(items)
	return render_template('index.html',items=items)

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

@app.route('/look',methods=['POST','GET'])
def look_up():
	if request.method == 'POST':
		website=request.form['website']	
		ip = socket.gethostbyname(website)
		obj = IPWhois(ip)
		results = obj.lookup_whois()
		print ("length is",len(results['nets']))
		return render_template('look_up.html',results=results)

if __name__ == "__main__":
	app.run(debug=True)

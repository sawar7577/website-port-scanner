from flask import Flask, render_template,request
import scn

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
	items=[]
	if request.method == 'POST':
		website=request.form['website']
		items=scn.do_scan(website,"sV")
		return render_template("home.html",items=items)
	else:
		return render_template("home.html",items=items)

@app.route('/tcp',methods=['POST','GET'])
def tcp():
	items=[]
	if request.method == 'POST':
		website=request.form['website']
		items=scn.do_scan(website,"sV")
		return render_template("scans.html",items=items)
	else:
		return render_template("scans.html",items=items)

@app.route('/udp',methods=['POST','GET'])
def udp():
	items=[]
	if request.method == 'POST':
		website=request.form['website']
		items=scn.do_scan(website,"sU")
		return render_template("scans.html",items=items)
	else:
		return render_template("scans.html",items=items)


if __name__ == "__main__":
	app.run(debug=True)
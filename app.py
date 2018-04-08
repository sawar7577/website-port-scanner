from flask import Flask, render_template
from scn import *

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
	# items=None
	# if method == 'POST':
	items=scn.do_scan("www.gitaniketan.org","sV")
	return render_template("home.html",items)
	# else:
		# return render_template("home.html",items)

if __name__ == "__main__":
	app.run(debug=True)
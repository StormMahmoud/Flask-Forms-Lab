from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["zain","antony","Adan", "juduyyyyyy", "Fouad", "faridd"]


@app.route('/', methods = ['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		if(username == request.form['username'] and password == request.form['password']):
			return redirect(url_for('home'))
		else:
			return render_template('login.html')	

@app.route('/home') 
def home():
	facebook_friends=["zain","antony","Adan", "juduyyyyyy", "Fouad", "faridd"]
	return render_template('home.html', zane = facebook_friends)

@app.route('/friend_exists/<string:name>', methods = ['GET','POST']) 
def friend_exists(name):
	return render_template('friend_exists.html', n = name)	




if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
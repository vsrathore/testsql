from flask import Flask, render_template, request, make_response, abort, redirect, url_for
from form import EmailPasswordForm
import mod
from flask import session


app = Flask(__name__)
app.config['SECRET_KEY'] = 's\xdd\xed\x8f\x8e\xbb\xb9\xf3\x8f\n\xd5).\x00m\xac\xd3E\xbf\xb2\xdes\x1d,'


#######################Page Requests:########################################

#Index Page Request
@app.route('/test')
def tt():
	return mod.testx()

@app.route('/testx')
def ttsx():
	ress=mod.ttxs()
	return ress

#Index Page Request
@app.route('/')
def index():
	loged_in = request.cookies.get('Loged_in')
	if loged_in == None:
		return render_template('index.html', Tim="Stranger")
	return render_template('index.html', Tim=request.cookies.get('Username'))


#Form Page Request
@app.route('/login', methods=["GET", "POST"])
def login():
	loged_in = request.cookies.get('Loged_in')
	if loged_in == 'True':
		return render_template('index.html', Tim=request.cookies.get('Username'), dirv='Redirected from login page.!')

	form = EmailPasswordForm(request.form)
	if form.email.data == 'Vishan@gmail.com':
		res = make_response(render_template('index.html', Tim=form.password.data, dirv='Form filled!'))
		res.set_cookie('Username', form.password.data)
		res.set_cookie('Loged_in','True')
		session['loged_in'] = 'True'
		return res
	return render_template('login.html')


#logout Request
@app.route('/logout', methods=["GET"])
def logout():
		res = make_response(render_template('index.html', Tim='Stranger', dirv='Loged_out Succesfully !'))
		res.set_cookie('Username', '')
		res.set_cookie('Loged_in', '')
		if ('loged_in' and 'csrf_token') in session:
			del session['loged_in']
			del session['csrf_token']
		return res


@app.route('/testing')
def testing():
	if mod.test_login():
		return '<h1>Loged_in</h1> '
	return '<h1>Not Loged_in</h1>'


#Running Server on Host:127:0:0:1 with port:5000 (this is default port & host)
if __name__=='__main__':
	app.run()
#	app.run(host='0.0.0.0', port=5000)

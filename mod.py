from flask import render_template, session, Flask
from database_inti import Role, User, db



app = Flask(__name__)
app.config['SECRET_KEY'] = 's\xdd\xed\x8f\x8e\xbb\xb9\xf3\x8f\n\xd5).\x00m\xac\xd3E\xbf\xb2\xdes\x1d,'



def testx():
    tt1 = User.query.all()
    tt2 = Role.query.all()
    return render_template('index.html', tgf=tt1, ttgf=tt2, Tim="to NASA's Database")


def ttxs():
    if 'loged_in' not in session:
        session['loged_in'] = False
    if 'Username' not in session:
        session['Email'] = 'test_email'
        session['Username'] = 'test_username'
        session['Password'] = 'test_password'
    return render_template('index.html', Tim='Admin')


def test_login():
    if 'loged_in' in session :
        return True
    return False

from flask import *
from database import *
public=Blueprint('public',__name__)
@public. route('/')
def home():

	return render_template('welcome.html')
@public. route('/login',methods=['post','get'])
def login():
	if "submit" in request.form:
		n=request.form['name']
		p=request.form['password']
		q="select * from login where username ='%s' and password ='%s'"%(n,p)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['user_type']=="admin":
				return redirect(url_for('admin.adminhome'))
			
	return render_template("login.html")
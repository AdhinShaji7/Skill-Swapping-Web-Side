from flask import *
from database import *

public=Blueprint('public',__name__)
@public.route('/')
def home():
	return render_template('home.html')
@public.route('/login',methods=['post','get'])
def login():
	if "sub" in request.form:
		u=request.form['uname']
		p=request.form['pwd']
		s="select * from login where username='%s' and password='%s'" %(u,p)
		res=select(s)
		if res:
			session['login_id']=res[0]['login_id']
			print('my login',session['login_id'])

			if res[0]['usertype']=='admin':
				return redirect(url_for('admin.adminhome'))


			elif res[0]['usertype']=='proffessional':
				q="select * from proffessional where login_id='%s'"%(session['login_id'])
				val=select(q)
				if val:
					session['pid']=val[0]['pid']
					return redirect(url_for('pro.prohome'))
			elif res[0]['usertype']=='staff':
				q="select * from staff where login_id='%s'"%(session['login_id'])
				val=select(q)
				if val:
					session['sid']=val[0]['staff_id']
					return redirect(url_for('staff.staffhome'))
		else:
			flash("username or password is incorrect")

	return render_template('login.html')

@public.route('/staff_register',methods=['post','get'])
def staff_register():
	if 'ds' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		pla=request.form['pla']
		phn=request.form['phn']
		mail=request.form['mail']
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="insert into login values(null,'%s','%s','staff')"%(uname,pwd)
		res=insert(q)
		q="insert into staff values(null,'%s','%s','%s','%s','%s','%s')"%(res,fname,lname,pla,phn,mail)
		insert(q)
	return render_template('staff_register.html')

@public.route('/proffessional_register',methods=['post','get'])
def proffessional_register():
	if 'ds' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		pla=request.form['pla']
		phn=request.form['phn']
		mail=request.form['mail']
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="insert into login values(null,'%s','%s','proffessional')"%(uname,pwd)
		res=insert(q)
		q="insert into proffessional values(null,'%s','%s','%s','%s','%s','%s')"%(res,fname,lname,pla,phn,mail)
		insert(q)
	return render_template('proffessional_register.html')
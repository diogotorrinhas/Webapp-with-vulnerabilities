from flask import Blueprint,render_template,request, redirect, url_for
from flask.helpers import flash
from .models import User
from database.database import db
from flask_login import login_user, login_required, logout_user, current_user
import hashlib
import sqlite3

auth = Blueprint('auth', __name__, template_folder="templates/")

@auth.route('/login', methods=['GET','POST'])
def login():
	debug = None
	if current_user.is_authenticated:
		flash("You're already logged in")
		return redirect(url_for('views.home'))

	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		sql = f"select * from User where email='{email}'"
		
		try:
			user1 = User.query.from_statement(db.text(sql)).first()
			if user1:
				sql = f"select * from User where email='{email}' and password='{hashlib.md5(password.encode('utf-8')).hexdigest()}'"
				user2 = User.query.from_statement(db.text(sql)).first()
				if user2:
					flash('Logged in successfully!', category='success')
					login_user(user2,remember=True)
					return redirect(url_for('views.home'))
				else:
					flash('Incorrect password, try again.', category='error')
					if request.args.get('debug') == 'true':
						debug = sql, user1.password
			else:
				flash('Email does not exist.', category='error')

		except Exception as ex:
			flash("Something went wrong!", category="error")
			debug = sql, ex

	return render_template("login.html", user=current_user, debug=debug) #se estiver autenticado, na template aparece no canto superior esquerdo(na barra) Home,Logout

@auth.route('/logout')
@login_required	#nao conseguimos fazer logout a não ser que estejamos logados
def logout():
	logout_user()
	return redirect(url_for('views.home'))

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
	if current_user.is_authenticated:
		flash("You're already logged in")
		return redirect(url_for('views.home'))

	if request.method == 'POST':
		email = request.form.get('email')
		first_name = request.form.get('firstName')
		last_name = request.form.get('lastName')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')

		user = User.query.filter_by(email=email).first()  # query 
		if user:
			flash('Email already exists.', category='error')	#o category está na base.html, basicamente -> if category == 'error' em html, imprime o erro a vermelho
		elif len(email) < 4:
			flash('Email must be greater than 3 characters.', category='error')
		elif len(first_name) < 2:
			flash('First name must be greater than 1 character.', category='error')
		elif len(last_name) < 2:
			flash('Last name must be greater than 1 character.', category='error')
		elif password1 != password2:
			flash('Passwords don\'t match.', category='error')
		elif len(password1) < 4:
			flash('Password must be at least 4 characters.', category='error')
		else:
			new_user = User(email = email, first_name = first_name, last_name = last_name, password=hashlib.md5(password.encode('utf-8')).hexdigest())	#creating user
			db.session.add(new_user)
			db.session.commit()
			login_user(new_user, remember=True)
			flash('Account created!', category='success')
			return redirect(url_for('views.home'))	#redirect to home page

	return render_template("sign_up.html", user=current_user)	#se não estiver autenticado na template aparece no canto superior esquerdo(na barra) Login,Sign-in

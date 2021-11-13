from flask import Blueprint,render_template,request, redirect, url_for, make_response
from flask.helpers import flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from database.database import db
from flask_login import login_user, login_required, logout_user, current_user
from .views import set_headers

auth = Blueprint('auth', __name__, template_folder="templates/")

@auth.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		flash("You're already logged in")
		return redirect(url_for('views.home'))

	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')

		user = User.query.filter_by(email=email).first()	# query, FAZER EM RAW CODE (DÁ ERRO POR CAUSA DA dataBase (last_name))
		if user:
			if check_password_hash(user.password, password):
				flash('Logged in successfully!', category='success')
				login_user(user,remember=True)
				return redirect(url_for('views.home'))
			else:
				flash('Incorrect email or password, try again.', category='error')
		else:
			flash('Incorrect email or password, try again.', category='error')

	r = make_response(render_template("login.html", user=current_user)) #se estiver autenticado, na template aparece no canto superior esquerdo(na barra) Home,Logout
	return set_headers(r)

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

		user = User.query.filter_by(email=email).first()  # query, FAZER EM RAW CODE (DÁ ERRO POR CAUSA DA dataBase (last_name))
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
			new_user = User(email = email, first_name = first_name, last_name = last_name, password=generate_password_hash(password1,method='sha256'))	#creating user
			db.session.add(new_user)
			# Adicionar user a tabela de role
			db.session.commit()
			login_user(new_user, remember=True)
			flash('Account created!', category='success')
			return redirect(url_for('views.home'))	#redirect to home page

	r = make_response(render_template("sign_up.html", user=current_user))	#se não estiver autenticado na template aparece no canto superior esquerdo(na barra) Login,Sign-in
	return set_headers(r)

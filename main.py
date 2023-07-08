from flask import Flask, render_template, jsonify, request, redirect, session
from dp import Database
import api

app = Flask(__name__)
dbo = Database()


@app.route('/')
def home():
  return render_template("login.html")


@app.route('/register')
def register():
  return render_template("register.html")


@app.route('/perform_registration', methods=['POST'])
def perform_registration():
  name = request.form['user_ka_naam']
  email = request.form['user_ka_email']
  password = request.form['user_ka_password']

  response = dbo.insert(name, email, password)
  if response == 1:
    return render_template(
      'login.html', message='Registration sucsessfull now login to proceed')
  else:
    return render_template('register.html', message='Email Already exist')


@app.route('/perform_login', methods=['post'])
def perform_login():
  email = request.form['user_ka_email']
  password = request.form['user_ka_password']
  response = dbo.search(email, password)
  if response == -1:
    return render_template('login.html',
                           message='email not exist please register')
  elif response == 1:
    return redirect('/profile')
  else:
    return render_template('login.html', message='Incorrect email/password')


@app.route('/profile')
def profile():
  return render_template('profile.html')


@app.route('/ner')
def ner():
  return render_template('ner.html')


@app.route('/perform_ner', methods=['post'])
def perform_ner():
  text = request.form['ner_text']
  response = api.ner(text)

  return render_template('ner.html', response=response)


# @app.route('/perform_ner', method=['post'])
# def perform_ner():
#   text = request.form.get('ner_text')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

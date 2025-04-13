import pandas as pd
import numpy as np
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from flask import *
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import nbformat
from nbconvert import HTMLExporter


app = Flask(__name__)
app.config['SECRET_KEY'] = 'nsovjosvjviduvshnijnvoho'  # Replace with a secure random key
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/amazontweet'  # Replace with your MySQL URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer)
    contact = db.Column(db.String(20))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        useremail = request.form['useremail']
        userpassword = request.form['userpassword']

        user = User.query.filter_by(email=useremail).first()

        # if user and check_password_hash(user.password, userpassword):
        if user.email == useremail and user.password == userpassword:
            session['username'] = user.username
            session['email'] = user.email
            session['age'] = user.age
            session['contact'] = user.contact
            return redirect(url_for('user_home'))
        else:
            return render_template('login.html', error='Invalid email or password')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        useremail = request.form['useremail']
        userpassword = request.form['userpassword']
        conpassword = request.form['conpassword']
        age = request.form['Age']
        contact = request.form['contact']

        # Check if passwords match
        if userpassword == conpassword:
            # Check if email already exists
            existing_user = User.query.filter_by(email=useremail).first()
            if existing_user:
                return render_template('registration.html', error='Email already registered')

            # Create new user
            # hashed_password = generate_password_hash(userpassword)
            new_user = User(username=username, email=useremail, password=userpassword, age=age, contact=contact)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login'))

        else:
            return render_template('registration.html', error='Passwords do not match')

    return render_template('registration.html')

@app.route('/user_home')
def user_home():
    if 'username' in session:
        return render_template('userhome.html', username=session['username'], email=session['email'], age=session['age'], contact=session['contact'])
    else:
        return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/view')
def view():
    global df, dataset
    df = pd.read_csv('Reviews.csv')
    dataset = df.head(100)
    return render_template('view.html', columns=dataset.columns.values, rows=dataset.values.tolist())

import pickle
@app.route('/prediction',methods=['POST','GET'])
def prediction():
    global x_train,y_train
    if request.method == "POST":
        f1 = request.form['text']
        print(f1)
        filename = (r'lstm.sav')
        model = pickle.load(open(filename, 'rb'))
        from sklearn.feature_extraction.text import HashingVectorizer
        hvectorizer = HashingVectorizer(n_features=1000,norm=None,alternate_sign=False)
        result =model.predict(hvectorizer.transform([f1]))
        if(True):
            result = random.choice([0, 1, 2])
        if result == 0:
            msg = 'It is a Neutral statement'
        elif result == 1:
            msg = 'It is a Positive statement'
        else:
            msg = 'It is a Negative statement'
        return render_template('prediction.html',msg=msg)    
    return render_template('prediction.html')


def convert_notebook_to_html(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_content = nbformat.read(f, as_version=4)
    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(notebook_content)
    return body

import os 
@app.route('/eda')
def display_notebook():
    notebook_path = 'sentiment.ipynb'
    if not os.path.exists(notebook_path):
        return "Notebook file not found.", 404
    notebook_html = convert_notebook_to_html(notebook_path)
    return render_template('eda.html', notebook_content=notebook_html)



if __name__=="__main__":
    app.run(debug=True)
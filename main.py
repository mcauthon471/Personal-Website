from flask import Flask, render_template, request, redirect, url_for, session, flash
import os 
import json
from pymongo import MongoClient
from urllib.parse import quote_plus
username = quote_plus('michaelcauthonbusiness')
password = quote_plus('MWACj@ck2004+')
app = Flask(__name__,template_folder='template_files',static_folder='static_files')
dbconnection = MongoClient('mongodb+srv://' +username +':'+password+'@cluster0-pl-0.rs6nm.mongodb.net/?retryWrites=true&w=majority')
db = dbconnection.github
collection = db.repositories

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/projects')
def projects():
    db_items = collection.find()
    return render_template('projects.html', db_items=db_items) 


@app.errorhandler(404)
def page_not_found(e):
    return redirect(""), 404, {"Refresh": "1; url=/"}

if __name__ == '__main__':
    app.run(debug=True)
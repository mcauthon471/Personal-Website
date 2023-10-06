from flask import Flask, render_template, request, redirect, url_for, session, flash
import os 
import json

app = Flask(__name__,template_folder='template_files',static_folder='static_files')


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
    return render_template('projects.html')

@app.errorhandler(404)
def page_not_found(e):
    return redirect(""), 404, {"Refresh": "1; url=/"}

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, make_response,redirect, url_for
import json
from options import DEFAULTS

app = Flask(__name__)

@app.route("/")
def index():
    name = {'firstname':'Emmanuel', 'lastname':'Semutenga'}
    return render_template('home.html', **name)

@app.route('/register', methods=['POST','GET'])
def register():
    #in flask cookies are set on the response, if none is available, fake a response using make_response

    #response = make_response(redirect(url_for('index')))
    if request.method == 'POST':
        #storing a cookie
        response = make_response(redirect(url_for('index')))
        response.set_cookie('user', json.dumps(dict(request.form.items())))#cookie name and value, json dumps turns data into a json string
        return response
        #return f"you have posted {request.form['firstname']} and {request.form['lastname']}"
    #retrieving the cookie
    return render_template('form.html', saves = get_saved_data())

#get saved data from cookie
def get_saved_data():
    try:
        data = json.loads(request.cookies.get('user'))#loads stands for load string, json.loads make data into python code again
    except TypeError:
        #if we get something that can't be converted into json
        data = {}
    return data

#using cookies helps to hold onto data

@app.route('/builder', methods=['POST', 'GET'])
def builder():
    if request.method == "POST":
         #storing a cookie
        response = make_response(redirect(url_for('builder')))
        response.set_cookie('user', json.dumps(dict(request.form.items())))#cookie name and value, json dumps turns data into a json string
        return response
    return render_template('builder.html', saves=get_saved_data(), options = DEFAULTS)
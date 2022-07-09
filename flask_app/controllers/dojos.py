from flask import render_template, redirect, request

from flask_app import app

from flask_app.models.dojo import Dojo


@app.route('/')
def route():
    return redirect ('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('dojo.html', dojos = Dojo.get_all())

@app.route('/dojos/create', methods=["POST"])
def create_dojo():
    Dojo.new_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data ={
        "id":id
    }
    return render_template('dojo_show.html',dojo=Dojo.get_one_w_ninja(data))


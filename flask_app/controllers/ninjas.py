from flask import render_template, redirect, request

from flask_app import app


from flask_app.models import dojo, ninja

@app.route('/ninjas')
def create_ninja():
    return render_template('ninja.html', dojos = dojo.Dojo.get_all())

@app.route('/create/ninja', methods=["POST"])
def new_ninja():
    ninja.Ninja.create_ninja(request.form)
    return redirect('/dojos')
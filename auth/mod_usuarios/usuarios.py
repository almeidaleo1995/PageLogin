from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from __init__ import db



bp_usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios', template_folder='templates')


@bp_usuarios.route("/view")
def formUsuario():
    user = User.query.all()    
    return render_template("formUsuario.html",user=user)


@bp_usuarios.route('/', methods = ['GET', 'POST'])
def addUsuario():
    if request.method == 'POST': 
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))         
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('usuarios.formUsuario'))
    return render_template('addUsuario.html')   
       
  
@bp_usuarios.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    user = User.query.get(id)
    if request.method == 'POST':        
        user.email = request.form['email']
        senha = request.form['password']
        user.password = generate_password_hash(senha, method='sha256')        
        user.name = request.form['name']        
        db.session.commit()
        return redirect(url_for('usuarios.formUsuario'))
    return render_template('editUsuarios.html', user=user)


@bp_usuarios.route('/delete/<int:id>')
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('usuarios.formUsuario'))

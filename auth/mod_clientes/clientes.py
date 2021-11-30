from flask import Blueprint, render_template, request, redirect, url_for

from models import Cliente
from __init__ import db

bp_clientes = Blueprint('clientes', __name__, url_prefix='/clientes', template_folder='templates')


@bp_clientes.route("/")

def formCliente():
    cliente = Cliente.query.all()
    return render_template("formClientes.html", cliente=cliente)


@bp_clientes.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        cliente = Cliente(request.form['nome'], request.form['cpf'], request.form['idade'])
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('clientes.formCliente'))
    return render_template('add.html')    


@bp_clientes.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cliente = Cliente.query.get(id)
    if request.method == 'POST':
        cliente.nome = request.form['nome']
        cliente.cpf = request.form['cpf']
        cliente.idade = request.form['idade']
        db.session.commit()
        return redirect(url_for('clientes.formCliente'))
    return render_template('edit.html', cliente=cliente)


@bp_clientes.route('/delete/<int:id>')
def delete(id):
    cliente = Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('clientes.formCliente'))
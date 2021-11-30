import os
import base64
from flask import Blueprint, render_template, request, redirect, url_for
from models import Produto
from __init__ import db



bp_produtos = Blueprint('produtos', __name__, url_prefix='/produtos', template_folder='templates')


@bp_produtos.route("/view")
def formProduto():
    produto = Produto.query.all()
    for prod in produto:
        prod.image_str = prod.image.decode("utf-8")  
    return render_template("formProduto.html",produto=produto)


@bp_produtos.route('/', methods = ['GET', 'POST'])
def addProduto():
    if request.method == 'POST':  
        image_string = get_image(request)         
        produto = Produto(request.form['nome'], request.form['valor'], image_string)        
        db.session.add(produto)
        db.session.commit()
        return redirect(url_for('produtos.formProduto'))
    return render_template('addProduto.html')   


def get_image(request):
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    image_string = None
    filename = file.filename
    if filename == '':          
        return redirect(request.url)
    if file:
        image_string = base64.b64encode(file.read())   
    return image_string       
    

@bp_produtos.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    produto = Produto.query.get(id)
    if request.method == 'POST':
        produto.image = get_image(request)      
        produto.nome = request.form['nome']
        produto.valor = request.form['valor']    
        db.session.commit()
        return redirect(url_for('produtos.formProduto'))
    return render_template('editProdutos.html', produto=produto)


@bp_produtos.route('/delete/<int:id>')
def delete(id):
    produto = Produto.query.get(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('produtos.formProduto'))

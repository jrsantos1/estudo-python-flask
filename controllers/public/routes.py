from flask import render_template, url_for, redirect, request, flash
from datetime import datetime
from config import App
from models.tables import *
from flask_login import login_user, logout_user, login_required, current_user

app = App().get_app()

@app.route("/")
@login_required
def home():
    
    from config_db import get_connection as conexao
    import pandas as pd 
    
    conn = conexao()

    atores = []

    # with conn.cursor() as cursor:
    #
    #     cursor.execute("SELECT * from actor")
    #     dados = cursor.fetchall()
    #
    #     df = pd.DataFrame(data=dados, columns=['id', 'name', 'cidade', 'data'])
    #
    #     df['data'] = pd.to_datetime(df['data'])
    #     df['data'] = df['data'].apply(lambda x : x.strftime("%m/%d/%Y"))
    #
    #     atores = df.to_dict(orient='records')

    print(current_user.id)
    print('dsfd')

    return render_template('home.html', atores=atores)

@app.route("/fundos")
def fundos(): 
    
    from utils.mesas import mesas 
    lista_mesas = enumerate(mesas().getMesas())
    
    print(lista_mesas)
    
    for i, lista in lista_mesas:
        print(i)
        print(lista)

    return render_template('fundos.html', lista_mesas=lista_mesas)
    
@app.route("/login", methods=['POST', 'GET'])
def login(): 
    
    if request.method == 'POST':
    
        usuario = request.form['usuario']
        senha = request.form['senha']
        
        if usuario and senha: 
            
            user: Usuario = Usuario.query.filter_by(usuario=usuario).first()
            
            if user and check_password_hash(user.senha,senha):
                login_user(user)
                return redirect(url_for('home'))
            else:
                
                flash('Usuário ou senha inválidos')
                return redirect(url_for('login'))
        
    return render_template('login.html')

@app.route("/grafico")
def grafico():
    return render_template('grafico.html')

@app.route("/autenticar")
def autenticar():
    pass
    
@app.route("/logout")
def logout():
   
    logout_user()
   
    return redirect(url_for('login'))
from config import App
from flask import request, redirect, url_for
app = App().get_app()


@app.route('/busca_fundo', methods=['GET', 'POST'])
def busca_fundo():
    
    cod_sac = request.form['cod_sac'] 
    
    print(cod_sac)
    
    return redirect(url_for('fundos'))    
    
@app.route('/buscar/<id>', methods=['GET', 'POST'])
def buscar(id):
    print(id)

    return redirect(url_for('fundos'))
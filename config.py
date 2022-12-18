from flask import Flask
import pyodbc
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Date
import os
from flask_login import LoginManager

class App: 
    
    app = Flask(__name__)
    app.secret_key = 'macro_vision'
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'macro_vision.db')
    
    login_manager = LoginManager(app=app)
    
    def get_app(self):
        return self.app 
    
    def get_db(self) -> SQLAlchemy:
        db = SQLAlchemy(self.app)
        return db
        
    def get_cnx_sqlserver():
        
        driver = 'SQL SERVER'
        server = 'DESKTOP-EN90SVC'
        database = 'sekila'
        
        try:
            str_conect = f'Driver={driver}; Server={server}; Database={database}'
        except Exception as e:
            print(e)
        
        return pyodbc.connect(str_conect)
        
        
    
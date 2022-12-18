import mysql.connector 
from mysql.connector import errorcode
import pandas as pd 

def get_connection():
    try: 
        conn = mysql.connector.connect(
            database="sakila",
            host="127.0.0.1",
            user="root",
            password="root123"
        )
        
        print("Conexão realizada com sucesso")

        return conn
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Nome de usuário ou senha errados')
        else:
            print(err)
            
get_connection()
        
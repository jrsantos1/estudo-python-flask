from werkzeug.security import generate_password_hash
import sqlite3



print(generate_password_hash('12345'))

con = sqlite3.connect('macro_vision.db')

cur = con.cursor()

user = 'ribejhu'
senha =   generate_password_hash('12345')

cur.execute(f"insert into user (senha, usuario) values ('{senha}','{user}' )")

con.commit()





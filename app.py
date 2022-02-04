
from flask import Flask,render_template,request

from flask_mysqldb import MySQL

app=Flask(__name__)


app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "user"
app.config['MYSQL_PASSWORD'] = "password"
app.config['MYSQL_DB'] = "user_db"

mysql = MySQL(app)



@app.route('/',methods=['GET','POST'])
def index():


    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']


        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO user_info(user_name,gmail) VALUES (%s,%s)",(name,email))

        mysql.connection.commit()
  
        cur.close()
         
        return "success"


    return render_template('index.html')


if __name__== "__main__":
    app.run(debug=True)



 

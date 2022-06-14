from flask import Flask, render_template, request, redirect 
import module2 as m2
#from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
#db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html',ap=m2.ap,bn=m2.bn,og=m2.og,ot=m2.ot,ipath=m2.ipath)
if __name__ == "__main__":
    app.run(debug=True)

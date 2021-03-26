from flask import Flask, render_template, request
from html import unescape
import requests, mysql.connector, psycopg2, flask_mail
app = Flask(__name__)

@app.route('/')
def home(): return render_template('base.html',
                                   pages=('Filler',
                                          'Hex Color Pallete',
                                          'Simple Calculator'),
                                   )

@app.route('/snippet/<file>',methods=["POST"])
def snippet(file):       
    return render_template(unescape(file),**request.args)

if __name__=='__main__': 
    app.run(debug=True, 
            port=9999)
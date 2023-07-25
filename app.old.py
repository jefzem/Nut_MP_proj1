#hello1

import os
from flask import Flask, redirect, render_template, request, send_from_directory, url_for, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/traitement')
def traitement():
    conn = sqlite3.connect('PILCv0.5.db')
    ##conn.row_factory = dict_factory  <= rajoute le nom des colonnes
    cur = conn.cursor()
    all_usagers = cur.execute('SELECT nom, prenom FROM usagers').fetchall()
    return jsonify(all_usagers)
   # return render_template('resultat.html',nom='JFG', list_nom=all_usagers)    

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()

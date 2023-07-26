

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


@app.route('/marketplace')
def marketplace():
    print('marketplace')
    return render_template('MarketPlace.html')

@app.route('/api_usagers')
def api_usagers():
    print('api_usagers')
    return render_template('api_usagers.html')

@app.route('/api_entreprises')
def api_entreprises():
    print('api_entreprises')
    return render_template('api_entreprises.html')

@app.route('/simulations')
def simulations():
    print('simulations')
    return render_template('simulations.html')
##### API Marketplace ##############
@app.route('/info_contenants_V1')
def info_contenants_V1():
    print('info contenants V1')
    return render_template('API/List_Contenants_References_V01.html')

@app.route('/Contenants_enregistres_V1',methods=['GET'])
def Contenants_enregistres_V1():
    print('info contenants enregistresV1')
    conn = sqlite3.connect('PILCv0.5.db')
    ##conn.row_factory = dict_factory  <= rajoute le nom des colonnes
    cur = conn.cursor()
    all_Contenants = cur.execute('SELECT * FROM Contenants').fetchall()
    return jsonify(all_Contenants)
    #return render_template('API/Contenants_enregistrés_V1.html')

@app.route('/Contenants_enregistres_parfab_V1',methods=['POST'])
def Contenants_enregistres_parfab_V1():
    print('info contenants enregistresV1 parfab_')
    donnees = request.form
    print (donnees)
    print ("toto")
    nom=donnees.get('nom')
    print (nom)
    conn = sqlite3.connect('PILCv0.5.db')
    ##conn.row_factory = dict_factory  <= rajoute le nom des colonnes
    cur = conn.cursor()
    all_Contenants = cur.execute("SELECT * FROM Contenants WHERE fabricant = ?", (nom,)).fetchall()
    #return "Traitement des données"
    return jsonify(all_Contenants)
    #return render_template('API/Contenants_enregistrés_V1.html')


Contenants_enregistres_parfab_V1
##### API Usagers ###########

#### API  Entreprises ########

##### API Simulations  ##########

##### ANNEXES ########
@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/login')
def login():
       return render_template('login.html')

###### RUN ##############
if __name__ == '__main__':
   app.run()

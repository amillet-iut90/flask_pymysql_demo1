from flask import Flask, request, render_template, redirect, url_for, abort  # application WSGI

import datetime

liste_etudiants = [
    {'id':1,'nom':'tom', 'groupe':'A1'},
    {'id':2,'nom':'enzo', 'groupe':'A1'},
    {'id':3,'nom':'laurence', 'groupe':'A2'},
    {'id':4,'nom':'theo', 'groupe':'A2'},
    {'id':5,'nom':'mehdi', 'groupe':'B1'}
]

# (interface de serveur web python)
# comportements et méthodes d'un serveur web


app = Flask(__name__)    # instance de classe Flask (en paramètre le nom du module)

@app.route('/')
@app.route('/etudiant/show')
def show_etudiants():
    return render_template('etudiant/show_etudiants.html', etudiants=liste_etudiants )


@app.route('/etudiant/add', methods=['GET'])
def add_etudiant():
    print('''affichage du formulaire pour saisir un étudiant''')
    return render_template('etudiant/add_etudiant.html')

@app.route('/etudiant/delete')
def delete_etudiant():
    print('''suppression d'un étudiant''')
    print(request.args)
    #print(request.args['id'])
    print(request.args.get('id'))
    print(request.args.get('id',0))
    return redirect('/etudiant/show')

@app.route('/etudiant/edit', methods=['GET'])
def edit_etudiant():
    print('''affichage du formulaire pour modifier un étudiant''')
    print(request.args)
    print(request.args.get('id'))
    id=request.args.get('id')
    if id != None and id.isnumeric():
        indice = int(id)
        etudiant=liste_etudiants[indice-1]
    else:
        etudiant=[]
    return render_template('etudiant/edit_etudiant.html', etudiant=etudiant)


@app.route('/etudiant/add', methods=['POST'])
def vaid_add_etudiant():
    print('''ajout de l'étudiant dans le tableau''')
    nom = request.form['nom']
    nom = request.form.get('nom')
    groupe = request.form.get('groupe')
    message = 'nom :' + nom + ' - groupe :' + groupe
    print(message)
    return redirect('/etudiant/show')

@app.route('/etudiant/edit', methods=['POST'])
def valid_edit_etudiant():
    print('''modification de l'étudiant dans le tableau''')
    id = request.form.get('id')
    nom = request.form.get('nom')
    groupe = request.form.get('groupe')
    message = 'nom :' + nom + ' - groupe :' + groupe + ' pour l etudiant d identifiant :' + id
    print(message)
    return redirect('/etudiant/show')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

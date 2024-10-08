from flask import Blueprint, render_template, request
import random
from sklearn import datasets
from flask import Flask, request, render_template
from sklearn.datasets import load_digits, load_iris, load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

scikit_page = Blueprint("scikit_page", __name__)

@scikit_page.route('/iris', methods=['GET','POST'])
def iris():
    iris = datasets.load_iris()
    table = generate_table(iris)
    random_row_table = None

    if request.method == 'POST':
        random_index = random.randint(0, len(iris.data) - 1)
        random_row = iris.data[random_index]
        random_row_class = iris.target_names[iris.target[random_index]]
        random_row = list(random_row) + [random_row_class]
        random_row_table = generate_random_row_table(iris, random_row)
    return render_template("scikit/index.html", table=table, name="IRIS", randomrowtable=random_row_table)

@scikit_page.route('/diabetes', methods=['GET','POST'])
def diabetes():
    diabetes = datasets.load_diabetes()
    table = generate_table(diabetes)
    random_row_table = None

    if request.method == 'POST':
        random_index = random.randint(0, len(diabetes.data) - 1)
        random_row = diabetes.data[random_index]
        random_row_class = diabetes.target[random_index]
        random_row = list(random_row) + [random_row_class]
        random_row_table = generate_random_row_table(diabetes, random_row)

    return render_template("scikit/index.html", table=table, name="DIABETES", randomrowtable=random_row_table)

@scikit_page.route('/digits', methods=['GET','POST'])
def digits():
    digits = datasets.load_digits()
    table = generate_table(digits)
    random_row_table = None

    if request.method == 'POST':
        random_index = random.randint(0, len(digits.data) - 1)
        random_row = digits.data[random_index]
        random_row_class = digits.target[random_index]
        random_row = list(random_row) + [random_row_class]
        random_row_table = generate_random_row_table(digits, random_row)

    return render_template("scikit/index.html", table=table, name="DIGITS", randomrowtable=random_row_table)

def generate_table(data):
    html = ""
    tmp = ""
    for entete in data.feature_names:
        tmp += generate_th(entete)
    tmp += generate_th("Class")
    html += generate_tr(tmp)

    tmp = ""
    for ligne in range(len(data.data)):
        for cellule in range(len(data.feature_names)):
            tmp += generate_td(data.data[ligne][cellule])

        tmp += generate_td(data.target_names[data.target[ligne]] if hasattr(data, 'target_names') else data.target[ligne])
        html += generate_tr(tmp)
        tmp = ""

    return generate_t(html)

def generate_random_row_table(data, random_row):
    html = ""
    tmp = ""
    for entete in data.feature_names:
        tmp += generate_th(entete)
    tmp += generate_th("Class")
    html += generate_tr(tmp)

    tmp = ""
    for cellule in random_row[:-1]:
        tmp += generate_td(cellule)
    tmp += generate_td(random_row[-1])
    html += generate_tr(tmp)

    return generate_t(html)

def generate_th(data):
    return f"<th>{data}</th>"

def generate_tr(data):
    return f"<tr>{data}</tr>"

def generate_td(data):
    return f"<td>{data}</td>"

def generate_t(data):
    return f"<table class='table table-striped table-bordered table-hover'>{data}</table>"




@scikit_page.route('/testt', methods=['GET', 'POST'])
def train_model():
    if request.method == 'POST':
        # Récupérer les valeurs du formulaire
        dataset_name = request.form['dataset']
        test_size = float(request.form['test_size'])
        n_estimators = int(request.form['n_estimators'])

        # Choisir le jeu de données
        if dataset_name == 'digits':
            dataset = datasets.load_digits()
        elif dataset_name == 'iris':
            dataset = datasets.load_iris()
        elif dataset_name == 'diabetes':
            dataset = datasets.load_diabetes()

        # Diviser les données
        Xtrain, Xtest, ytrain, ytest = train_test_split(
            dataset.data, dataset.target, test_size=test_size)

        # Créer le modèle
        model = RandomForestClassifier(n_estimators=n_estimators)
        model.fit(Xtrain, ytrain)

        # Prédiction et évaluation
        ypred = model.predict(Xtest)
        report = metrics.classification_report(ypred, ytest)

        # Retourner le rapport dans la page
        return f"<h2>Résultat du modèle Random Forest</h2><pre>{report}</pre>"
    return render_template('scikit/testt.html')
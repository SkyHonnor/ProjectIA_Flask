# Mon Projet Flask (SQLAlchemy, InfluxDB et Classification)

![Mindmap](https://media.discordapp.net/attachments/1027886603814830101/1306269475938762763/Diagramme_sans_nom_2_3.png?ex=67360dc0&is=6734bc40&hm=ad0a9d6f4be27cb3453796cbf5c01374958d8bccf5f505ca4797e84e656d2265&=&format=webp&quality=lossless)
## Description
[![Python](https://img.shields.io/badge/Python-3.9-yellow?style=flat&logo=python&logoColor=white&labelColor=gray)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white&labelColor=gray)](https://www.docker.com/)

Ce projet est une application web développée en Python avec Flask, qui utilise plusieurs modules et bibliothèques pour manipuler et afficher des données, interagir avec des bases de données (SQL et NoSQL), et intégrer des modèles de machine learning.

### Fonctionnalités principales

1. **Backend avec Flask** : Une API construite avec Flask et organisée en modules et routes.
2. **Base de données SQL** : Utilisation de SQLite avec SQLAlchemy (ORM) pour accéder aux données.
3. **Base de données NoSQL** : Intégration d'InfluxDB pour manipuler des données de séries temporelles.
4. **Machine Learning** : Modèles de classification intégrés via Scikit-Learn et TensorFlow pour des tâches d'analyse et de prédiction.
5. **Frontend** : Une interface utilisateur simple avec HTML, CSS (Bootstrap), et JavaScript (jQuery).

### Arborescence du projet
```
ProjectIA_Flask
├── Dockerfile
├── requirements.txt
├── app
│   ├── app.py                 # Point d'entrée principal de l'application
│   ├── config.py              # Configuration de l'application
│   ├── database.py            # Gestion de la connexion à SQLite
│   ├── influxdb.py            # Connexion à InfluxDB
│   ├── watchroute.py
│   ├── database
│   │   └── chinook.db         # Base de données SQLite (exemple de Chinook)
│   ├── models
│   │   └── models.py          # Définition des modèles SQLAlchemy
│   ├── routes                 # Différentes routes de l'application
│   │   ├── route_chinook.py   # Route pour accès à la BD Chinook
│   │   ├── route_classifieur.py
│   │   ├── route_influxdb.py
│   │   ├── route_main.py
│   │   ├── route_scikit.py
│   │   └── route_temperature.py
│   ├── static                 # Fichiers statiques (CSS, JS, images)
│   │   ├── css
│   │   │   └── bootstrap.min.css
│   │   ├── img
│   │   └── js
│   │       ├── bootstrap.min.js
│   │       └── jquery.min.js
│   └── templates              # Templates HTML
│       ├── chinook
│       ├── classifieur
│       ├── influxdb
│       ├── scikit
│       ├── temperature
│       └── layout.html
```

## Installation et Lancement

### Prérequis

- **Docker** : Pour exécuter l'application dans un environnement conteneurisé.
- **Python 3.9** : Pour une exécution locale en dehors de Docker.

### Installation

1. **Clonez le dépôt :**
```bash
git clone https://github.com/SkyHonnor/ProjectIA_Flask.git
cd ProjectIA_Flask
```
2. **Installez les dépendances (si vous exécutez l'application localement) :**
```bash
pip install -r requirements.txt
```

### Exécution avec Docker

1.  **Construire l'image Docker** :
```bash
docker build -t mon-projet-flask .
```
2. **Lancer le conteneur** :
```bash
docker run -p 80:80 mon-projet-flask
```
3. **Accédez à l'application sur [http://localhost:80](http://localhost:80)**

### Exécution locale
1. **Dans le répertoire `app/`, lancez l'application :**
```bash
python app.py
```
2. **Accédez à l'application sur [http://localhost:80](http://localhost:80)**

## Organisation des Routes

- `route_main.py` : Route principale et affichage des pages de base.
- `route_chinook.py` : Route pour manipuler les données de la base Chinook.
- `route_influxdb.py` : Route pour interagir avec InfluxDB (ex : données Bitcoin).
- `route_classifieur.py` : Route pour les modèles de classification.
- `route_scikit.py` : Route pour les fonctionnalités machine learning avec Scikit-Learn.
- `route_temperature.py` : Route pour manipuler des données de température.

## Modules et Bibliothèques Utilisés

- **Flask** : Framework web pour construire des routes et une interface RESTful.
- **SQLAlchemy** : ORM pour interagir avec la base de données SQLite.
- **InfluxDB** : Gestion des données de séries temporelles.
- **Scikit-Learn & TensorFlow** : Pour intégrer des modèles de machine learning, notamment les classificateurs.
- **Bootstrap & jQuery** : Pour le frontend, permettant un design réactif et des interactions utilisateur.


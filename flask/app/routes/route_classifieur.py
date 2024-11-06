from flask import Blueprint, render_template, request
from sklearn.datasets import load_digits, load_iris, load_diabetes
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import Input
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.models import Model

classifieur_page = Blueprint("classifieur_page", __name__)

@classifieur_page.route('/RF', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        datasets_dict = {
            "iris": load_iris(),
            "diabetes": load_diabetes(),
            "digits": load_digits()
        }

        dataset_name = request.form.get('dataset', 'digits')
        test_size = float(request.form.get('test_size', 0.2))
        n_estimators = int(request.form.get('n_estimators', 10))

        dataset = datasets_dict.get(dataset_name, load_digits())
        X, y = dataset.data, dataset.target

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

        if dataset_name == "diabetes":
            model = RandomForestRegressor(n_estimators=n_estimators)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            mse = metrics.mean_squared_error(y_test, y_pred)
            report = {"MSE": mse}
        else:
            model = RandomForestClassifier(n_estimators=n_estimators)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            report = metrics.classification_report(y_test, y_pred, output_dict=True)

        return render_template("classifieur/classifieurrf.html", dataset=dataset_name, test_size=test_size, n_estimators=n_estimators, table=report)
    return render_template("classifieur/classifieurrf.html")

@classifieur_page.route('/ML', methods=['GET', 'POST'])
def ml():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        activation = request.form['activation']
        hidden_layers = int(request.form['hidden_layers'])
        neurons = list(map(int, request.form['neurons'].split(',')))
        loss = request.form['loss']
        optimizer = request.form['optimizer']
        batch_size = int(request.form['batch_size'])
        epochs = int(request.form['epochs'])
        validation_split = float(request.form['validation_split'])

        # Vérifier que le nombre de couches correspond au nombre de neurones donnés
        if len(neurons) != hidden_layers:
            return render_template("classifieur/classifieurml.html", alert="Erreur : le nombre de couches masquées ne correspond pas au nombre de valeurs de neurones fournies.")

        # Appeler la fonction de création et d'entraînement du modèle
        test_loss, test_accuracy = create_and_train_model(
            activation=activation,
            hidden_layers=hidden_layers,
            neurons=neurons,
            loss=loss,
            optimizer=optimizer,
            batch_size=batch_size,
            epochs=epochs,
            validation_split=validation_split
        )
        return render_template("classifieur/classifieurml.html", test_loss=test_loss, test_accuracy=test_accuracy)    
    return render_template("classifieur/classifieurml.html")



def create_and_train_model(activation='softmax', hidden_layers=1, neurons=[128], loss='categorical_crossentropy', optimizer='adam', batch_size=128, epochs=20, validation_split=0.1):
    # Load data
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    
    # Get data shapes
    num_train = X_train.shape[0]
    num_test = X_test.shape[0]
    img_height = X_train.shape[1]
    img_width = X_train.shape[2]
    
    # Reshape input data
    X_train = X_train.reshape((num_train, img_width * img_height))
    X_test = X_test.reshape((num_test, img_width * img_height))

    # Normalize pixel values
    X_train = X_train.astype('float32') / 255
    X_test = X_test.astype('float32') / 255

    # Encode labels to one-hot format
    y_train = to_categorical(y_train, num_classes=10)
    y_test = to_categorical(y_test, num_classes=10)

    # Define the model
    xi = Input(shape=(img_height * img_width,))

    # Add hidden layers dynamically based on input
    x = Dense(neurons[0], activation=activation)(xi)
    for i in range(1, hidden_layers):
        x = Dense(neurons[i], activation=activation)(x)

    # Output layer with softmax activation for classification
    y = Dense(10, activation='softmax')(x)

    model = Model(inputs=[xi], outputs=[y])

    # Print model summary
    model.summary()

    # Compile the model
    model.compile(loss=loss,
                  optimizer=optimizer,
                  metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train,
              batch_size=batch_size,
              epochs=epochs,
              verbose=1,
              validation_split=validation_split)

    # Evaluate the model
    score = model.evaluate(X_test, y_test, verbose=0)
    return score[0], score[1]  # Test loss, Test accuracy
 




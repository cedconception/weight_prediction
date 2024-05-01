import pickle
import joblib
from flask import Flask, render_template, request

# Charger le modèle Scikit-learn
model = pickle.load( open('model.pkl','rb'))

# Fonction de prédiction du poids
def predict_weight(height):
    # Préparer les données d'entrée
    X = [[height]]

    # Faire la prédiction
    predicted_weight = model.predict(X)[0]

    # Renvoyer le poids prédit
    return predicted_weight

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtenir la valeur de la taille
        height = float(request.form['height'])

        # Prédire le poids
        predicted_weight = predict_weight(height)

        # Rendre le template avec le poids prédit
        return render_template('index.html', predicted_weight=predicted_weight)
    else:
        # Rendre le template par défaut
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

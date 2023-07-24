import os
import pickle
import flask
from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)                    #Creating the flask app object
CORS(app)                                #Allows web app to be accessed from different domains

with open('model.pkl', 'rb') as handle:  #Loading the trained model
    model = pickle.load(handle)

@app.route('/')                          #Executes the main function when the url is accessed
def main():
    return render_template('main.html')

@app.route('/predict', methods=['POST']) #Executes the predict function when user sends a POST request
def predict():
    news = request.form.get('news')
    pred = model.predict([news])
    return render_template('main.html', y='"{}" news'.format(pred[0]))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True, use_reloader=False)
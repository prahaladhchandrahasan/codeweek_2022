import numpy as np

from tensorflow import keras


from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
model = keras.models.load_model("model.h5")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    """
    For rendering results on HTML GUI
    """
    int_features = [x for x in request.form.values()]
    print(type(int_features[0]))
    input = int_features[0]
    lis = input.split(",")
    lis1 = []
    for i in lis:
        lis1.append(float(i))
    lis1 = np.array(lis1)
    print(lis1.shape)
    prediction = model.predict(lis1.reshape(1, 29))
    result = "not fradulent"
    if prediction > 0.5:

        output = 1
    else:

        output = 0
        result = "fradulent"

    return render_template('index.html', prediction_text='The model output for the uploaded file {}'.format(output))

if __name__ == "__main__":
    app.run(port=8080 ,debug=True, threaded=True)

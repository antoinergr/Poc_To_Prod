from flask import Flask, request, render_template
from predict.predict import run


app = Flask(__name__)   

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/", methods =['POST'])
def guess_tags():
    text = request.form['comments']
    if len(text) > 0:
        model = run.TextPredictionModel.from_artefacts("saved_models/2022-12-14-14-30-01")
        pred = model.predict([text])
        return pred


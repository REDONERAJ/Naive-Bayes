from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('car_evaluation_naive_bayes_model.pkl')

buying_opts = ["vhigh", "high", "med", "low"]
maint_opts = ["vhigh", "high", "med", "low"]
doors_opts = ["2", "3", "4", "5more"]
persons_opts = ["2", "4", "more"]
lug_boot_opts = ["small", "med", "big"]
safety_opts = ["low", "med", "high"]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        data = [
            buying_opts.index(request.form["buying"]),
            maint_opts.index(request.form["maint"]),
            doors_opts.index(request.form["doors"]),
            persons_opts.index(request.form["persons"]),
            lug_boot_opts.index(request.form["lug_boot"]),
            safety_opts.index(request.form["safety"])
        ]
        pred = model.predict([data])[0]
        classes = ["unacc", "acc", "good", "vgood"]
        prediction = classes[pred]
    return render_template("index.html",
                           prediction=prediction,
                           buying=buying_opts,
                           maint=maint_opts,
                           doors=doors_opts,
                           persons=persons_opts,
                           lug_boot=lug_boot_opts,
                           safety=safety_opts)

if __name__ == "__main__":
    app.run(debug=True)

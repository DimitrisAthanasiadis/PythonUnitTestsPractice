from flask import Flask, json, jsonify, render_template, request
from forms import SimpleForm


app = Flask(__name__)
app.secret_key = "secret-key"

@app.route("/", methods=["GET", "POST"])
def index():
    form = SimpleForm(request.form)
    
    if request.method == "POST" and form.validate():
        f1 = form.text1.data
        f2 = form.text2.data
        context = {
            "f1": f1,
            "f2": f2
        }
        
        return jsonify({
            "success": "Post is successful",
            "f1": f1,
            "f2": f2
        }), 200
    return render_template("index.html", form=form, context={"test_meta": "testt"})


if __name__ == "__main__":
    app.run()
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        key = request.form.get("key")
        with open("keys.json", "r") as f:
            keys = json.load(f)
        if key in keys and not keys[key]["used"]:
            message = "✅ Acesso liberado ao painel!"
        else:
            message = "❌ Key inválida ou já usada."
    return render_template("painel.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

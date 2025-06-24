import os
from flask import Flask, request, render_template

from flask import Flask, request, render_template
import os

app = Flask(__name__)

def lire_texte(fichier):
    try:
        with open(fichier, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Texte manquant."

@app.route("/", methods=["GET", "POST"])
def recherche():
    index = []
    messages = []

    if request.method == "POST":
        profession = request.form.get("profession", "").lower()
        date = request.form.get("date", "")
        lieu = request.form.get("lieu", "").lower()

        tests = [
            ("militaire" in profession, "militaire.txt"),
            ("fisc" in profession, "fisc.txt"),
            ("douanier" in profession, "douane.txt"),
            ("fonctionnaire" in profession, "fonctionnaire.txt"),
        ]

        for test, fichier in tests:
            index.append(int(test))
            messages.append(lire_texte(fichier))

        # On passe les deux listes au template
        return render_template("resultats.html", index=index, messages=messages)

    return render_template("index.html")



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render attribue automatiquement un port
    app.run(host="0.0.0.0", port=port)


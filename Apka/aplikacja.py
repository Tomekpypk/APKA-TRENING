
from flask import Flask, render_template, request

app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)

# Słownik z ćwiczeniami
workout_dict = {
    "klatka": ["Wyciskanie hantli na skosie", "sztanga na płasko", "rozpiętki na skosie", "sztanga na ławce na skosie dodatnim",
                "sztanga na ławce na skosie ujemnym", "Wyciskanie hantli na ławce płaskiej","Wyciskanie hantli złączonych razem", "Przenoszenie hantla za głowę na ławce płaskiej",
                "Wyciskanie na hammerze- ławka płaska","Wyciskanie na hammerze- ławka w skosie dodatnim", "Wyciskanie na hammerze w siedzeniu", "Pompki",
                "Pompki z obciążeniem ułożonym na plecach" ],
    "barki": ["Wyciskanie żołnierskie", "Wyciskanie hantli siedząc", "Wznosy hantli bokie", "Wznosy hantli przodem"],
    "nogi": ["Suwnica", "Przysiad", "Rumuński Ciąg", "Prostowanie nóg", "Uginanie nóg", "Wspięcia na palce"],
    "biceps": ["Uginanie ramienia w pochyleniu przodem", "Supinacja", "Modlitewnik", "Młotki","Modlitewnik z hantlem jednorącz", "Uginanie ramion z gryfem łamanym", "Uginanie ramion na wyciągu dolny-lina"],
    "triceps": ["Wyciąg górny- trójkąt", "Wyciąg górny-lina", "Wyciskanie francuskie w leżeniu-Gryf łamany", "Prostowanie przedramion oburącz w pochyleniu przodem", "Wyciąg górny-jednorącz nachwytem", 
                "Uginanie francuskie jednorącz siedząc", "Prostowanie przedramion w pochyleniu przodem na wyciągu górnym"],
    "plecy": ["Drążek", "Wyciąg górny- ściaganie drążka", "Wiosłowanie", "Wyciąg dolny"]
}

# Główny endpoint

@app.route("/", methods=["GET", "POST"])
def console():
    if request.method == "POST":
        question = request.form.get("input", "").lower()

        if question in workout_dict:
            exercises = workout_dict[question]
            return render_template("console.html", group=question, exercises=exercises)
        else:
            return render_template("console.html", result="Nie ma informacji o podanej grupie mięśniowej.")




    return render_template("console.html")



if __name__ == "__main__":
    app.run()

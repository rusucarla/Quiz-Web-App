import re
from flask import render_template, request, jsonify, redirect, request, session, g
from flask import Flask
import json
import pandas as pd
from numpy import *
from sklearn import linear_model

app = Flask(__name__, static_folder="static")

# incarcarea datasetului
data = pd.read_csv('static/dataset.csv')
array = data.values

for i in range(len(array)):
  if array[i][0] == "Male":
    array[i][0] = 1
  else:
    array[i][0] = 0

df = pd.DataFrame(array)
maindf = df[[0, 1, 2, 3, 4, 5, 6]]
mainarray = maindf.values

temp = df[7]
train_y = temp.values
train_y = temp.values

for i in range(len(train_y)):
    train_y[i] = str(train_y[i])

mul_lr = linear_model.LogisticRegression(
    multi_class="multinomial", solver="newton-cg", max_iter=1000
)
mul_lr.fit(mainarray, train_y)
# terminare incarcare dataset

#  DICTIONARIES
# 1. menu_pages for the navbar
menu_pages = [
    ("Home", "/", "home"),
    ("Princess Quiz", "/princess_quiz", "princess_quiz"),
    ("Marvel Quiz", "/marvel_quiz", "marvel_quiz"),
    ("Personality Quiz", "/personality_quiz", "personality_quiz"),
    ("About", "/about", "about")
]
# 2. user_data for the about page
user_data = [
    ("admin", "admin", "checked")
]
# 3. questions_princess_quiz for the princess quiz
questions_princess_quiz = [
    {
        "question_text": "Ce nuanță te reprezintă cel mai bine?",
        "options": [
            {"option_text": "Albastru profund", "image_url": "../static/images/princess_quiz/question_1/albastru.png", "score": {"Cinderella": 2, "Ariel": 1, "Belle": 1, "Mulan": 1, "Elsa": 3, "Rapunzel": 2, "Tiana": 1}},
            {"option_text": "Roz vibrant", "image_url": "../static/images/princess_quiz/question_1/roz.png", "score": {"Cinderella": 1, "Ariel": 2, "Belle": 1, "Mulan": 1, "Elsa": 1, "Rapunzel": 3, "Tiana": 1}},
            {"option_text": "Galben solar", "image_url": "../static/images/princess_quiz/question_1/galben.png", "score": {"Cinderella": 1, "Ariel": 1, "Belle": 3, "Mulan": 1, "Elsa": 2, "Rapunzel": 1, "Tiana": 2}},
            {"option_text": "Verde natură", "image_url": "../static/images/princess_quiz/question_1/verde.png", "score": {"Cinderella": 1, "Ariel": 2, "Belle": 2, "Mulan": 1, "Elsa": 1, "Rapunzel": 1, "Tiana": 3}}
        ]
    },
    {
        "question_text": "Care dintre aceste activități îți umple sufletul de bucurie?",
        "options": [
            {"option_text": "Cântatul sub stele", "image_url": "../static/images/princess_quiz/question_2/cantat.jpg", "score": {"Cinderella": 1, "Ariel": 3, "Belle": 1, "Mulan": 1, "Elsa": 1, "Rapunzel": 2, "Tiana": 1}},
            {"option_text": "Cititul în liniște", "image_url": "../static/images/princess_quiz/question_2/citit.jpg", "score": {"Cinderella": 2, "Ariel": 1, "Belle": 3, "Mulan": 1, "Elsa": 1, "Rapunzel": 1, "Tiana": 1}},
            {"option_text": "Dansat cu pasiune", "image_url": "../static/images/princess_quiz/question_2/dansat.jpg", "score": {"Cinderella": 1, "Ariel": 1, "Belle": 1, "Mulan": 1, "Elsa": 2, "Rapunzel": 3, "Tiana": 1}},
            {"option_text": "Gătitul unor delicii", "image_url": "../static/images/princess_quiz/question_2/gatit.jpg", "score": {"Cinderella": 1, "Ariel": 1, "Belle": 1, "Mulan": 1, "Elsa": 2, "Rapunzel": 1, "Tiana": 3}}
        ]
    },
    {
        "question_text": "Care este locul tău preferat pentru vacanță?",
        "options": [
            {"option_text": "Plajă exotică", "image_url": "../static/images/princess_quiz/question_3/plaja_exotica.jpg", "score": {"Cinderella": 1, "Ariel": 3, "Belle": 1, "Mulan": 1, "Elsa": 3, "Rapunzel": 1, "Tiana": 1}},
            {"option_text": "Munte", "image_url": "../static/images/princess_quiz/question_3/munte.jpg", "score": {"Cinderella": 1, "Ariel": 1, "Belle": 3, "Mulan": 1, "Elsa": 1, "Rapunzel": 2, "Tiana": 1}},
            {"option_text": "Oraș aglomerat", "image_url": "../static/images/princess_quiz/question_3/oras_aglomerat.jpg", "score": {"Cinderella": 2, "Ariel": 1, "Belle": 1, "Mulan": 1, "Elsa": 2, "Rapunzel": 1, "Tiana": 3}},
            {"option_text": "Sat liniștit", "image_url": "../static/images/princess_quiz/question_3/sat_linistit.jpg", "score": {"Cinderella": 1, "Ariel": 1, "Belle": 1, "Mulan": 1, "Elsa": 1, "Rapunzel": 3, "Tiana": 2}}
        ]
    },
    {
        "question_text": "Ce fel de muzică îți place cel mai mult?",
        "options": [
            {"option_text": "Pop", "image_url": "../static/images/princess_quiz/question_4/muzica_pop.jpg", "score": {"Cinderella": 1, "Ariel": 3, "Belle": 1, "Mulan": 1, "Elsa": 1, "Rapunzel": 2, "Tiana": 1}},
            {"option_text": "Rock", "image_url": "../static/images/princess_quiz/question_4/muzica_rock.jpg", "score": {"Cinderella": 1, "Ariel": 1, "Belle": 3, "Mulan": 1, "Elsa": 1, "Rapunzel": 1, "Tiana": 2}},
            {"option_text": "Clasică", "image_url": "../static/images/princess_quiz/question_4/muzica_clasica.jpg", "score": {"Cinderella": 2, "Ariel": 1, "Belle": 1, "Mulan": 1, "Elsa": 3, "Rapunzel": 1, "Tiana": 1}},
            {"option_text": "Jazz", "image_url": "../static/images/princess_quiz/question_4/muzica_jazz.jpg", "score": {"Cinderella": 1, "Ariel": 1, "Belle": 1, "Mulan": 1, "Elsa": 2, "Rapunzel": 1, "Tiana": 3}}
        ]
    },
    {
        "question_text": "Ce superputere ai vrea să ai?",
        "options": [
            {"option_text": "Invizibilitate", "image_url": "../static/images/princess_quiz/question_5/invizibilitate.jpg", "score": {"Cinderella": 1, "Ariel": 2, "Belle": 1, "Mulan": 1, "Elsa": 3, "Rapunzel": 1, "Tiana": 1}},
            {"option_text": "Zbor", "image_url": "../static/images/princess_quiz/question_5/zbor.jpg", "score": {"Cinderella": 1, "Ariel": 1, "Belle": 3, "Mulan": 1, "Elsa": 1, "Rapunzel": 2, "Tiana": 1}},
            {"option_text": "Superforță", "image_url": "../static/images/princess_quiz/question_5/superforta.jpg", "score": {"Cinderella": 2, "Ariel": 1, "Belle": 1, "Mulan": 1, "Elsa": 2, "Rapunzel": 1, "Tiana": 2}},
            {"option_text": "Teleportare", "image_url": "../static/images/princess_quiz/question_5/teleportare.jpg", "score": {"Cinderella": 1, "Ariel": 1, "Belle": 1, "Mulan": 1, "Elsa": 1, "Rapunzel": 3, "Tiana": 2}}
        ]
    },
    {
        "question_text": "Ce tip de film îți place să vezi?",
        "options": [
            {"option_text": "Dramă", "image_url": "../static/images/princess_quiz/question_6/drama.jpg", "score": {"Cinderella": 1, "Ariel": 2, "Belle": 1, "Mulan": 1, "Elsa": 1, "Rapunzel": 3, "Tiana": 1}},
            {"option_text": "Comedie", "image_url": "../static/images/princess_quiz/question_6/comedie.jpg", "score": {"Cinderella": 1, "Ariel": 1, "Belle": 3, "Mulan": 1, "Elsa": 1, "Rapunzel": 1, "Tiana": 2}},
            {"option_text": "Aventură", "image_url": "../static/images/princess_quiz/question_6/aventura.jpg", "score": {"Cinderella": 2, "Ariel": 1, "Belle": 1, "Mulan": 1, "Elsa": 2, "Rapunzel": 1, "Tiana": 1}},
            {"option_text": "SF", "image_url": "../static/images/princess_quiz/question_6/SF.jpg", "score": {"Cinderella": 1, "Ariel": 1, "Belle": 1, "Mulan": 1, "Elsa": 3, "Rapunzel": 1, "Tiana": 2}}
        ]
    },
    {
        "question_text": "Ce ai face într-o zi ploioasă?",
        "options": [
            {"option_text": "Citit o carte", "image_url": "../static/images/princess_quiz/question_7/citit_o_carte.jpg", "score": {"Cinderella": 1, "Ariel": 2, "Belle": 1, "Mulan": 1, "Elsa": 3, "Rapunzel": 1, "Tiana": 1}},
            {"option_text": "Uitat la ploaie", "image_url": "../static/images/princess_quiz/question_7/uitat_la_ploaie.jpg", "score": {"Cinderella": 1, "Ariel": 1, "Belle": 3, "Mulan": 1, "Elsa": 1, "Rapunzel": 2, "Tiana": 1}},
            {"option_text": "Făcut un puzzle", "image_url": "../static/images/princess_quiz/question_7/facut_un_puzzle.jpg", "score": {"Cinderella": 2, "Ariel": 1, "Belle": 1, "Mulan": 1, "Elsa": 2, "Rapunzel": 1, "Tiana": 2}},
            {"option_text": "Gătit ceva bun", "image_url": "../static/images/princess_quiz/question_7/gatit_ceva_bun.jpg", "score": {"Cinderella": 1, "Ariel": 1, "Belle": 1, "Mulan": 1, "Elsa": 1, "Rapunzel": 3, "Tiana": 2}}
        ]
    }
]
# 4. description for the princess quiz results
description_princess_quiz = {
  "Cinderella" : {"description": "Reprezinți esența speranței și a rezilienței. Cu o voință de fier și o inimă plină de bunătate, îți împlinești visurile, indiferent de obstacole. Luminozitatea ta interioară și compasiunea strălucesc, ghidându-i pe cei din jur spre un viitor mai bun."},
  "Ariel" : {"description": "Ești spiritul aventuros al mării, mereu în căutare de noi orizonturi și mistere de dezvăluit. Sensibilitatea și empatia ta profundă te fac să te conectezi cu lumea în moduri unice, iar creativitatea ta debordantă îți colorează fiecare zi."},
  "Belle" : {"description": "Cu o sete neobosită de cunoaștere și o curaj de neclintit, ești o lumină în întuneric. Inteligența ta strălucitoare și ambiția ta pentru explorare transformă fiecare provocare într-o aventură, inspirând pe toți cei din jurul tău."},
  "Mulan" : {"description": "Simbol al curajului și determinării, tu sfidezi așteptările și îți croiești propriul drum. Înțelepciunea și tăria ta sunt o sursă de inspirație, dovedind că adevărata putere vine din interior."},
  "Elsa" : {"description": "Ești un dans grațios între forță și sensibilitate, o furtună de creativitate care modelează lumea în jur. Inteligența ta profundă și empatia ta vastă creează un refugiu de calm și înțelegere pentru cei care te înconjoară."},
  "Rapunzel" : {"description": "O adevărată artistă a vieții, îți țesezi povestea cu fire colorate de curiozitate și creativitate. Sensibilitatea și empatia ta aduc frumusețe în lume, în timp ce spiritul tău aventuros deschide noi drumuri de explorat."},
  "Tiana" : {"description": "Intruchipezi visele și muncă asiduă, fiind un far de determinare și succes. Inteligența și curajul tău sunt pilonii pe care îți construiești viitorul, demonstrând că orice vis poate deveni realitate cu suficient efort și pasiune."}
}
# 5. questions_marvel_quiz for the marvel quiz
questions_marvel_quiz = [
    {
        "question_text": "Care supererou Marvel îți place cel mai mult?",
        "options": [
            {"option_text": "Iron Man", "score": {"Iron Man": 4, "Spider-Man": 2, "Captain America": 1, "Thor": 3}},
            {"option_text": "Spider-Man", "score": {"Iron Man": 2, "Spider-Man": 4, "Captain America": 3, "Thor": 1}},
            {"option_text": "Captain America", "score": {"Iron Man": 1, "Spider-Man": 3, "Captain America": 4, "Thor": 2}},
            {"option_text": "Thor", "score": {"Iron Man": 3, "Spider-Man": 1, "Captain America": 2, "Thor": 4}}
        ]
    },
    {
        "question_text": "Care superputere ți-ar plăcea să o ai?",
        "options": [
            {"option_text": "Zbor", "score": {"Iron Man": 3, "Spider-Man": 2, "Captain America": 1, "Thor": 4}},
            {"option_text": "Aranjare de păianjen", "score": {"Iron Man": 2, "Spider-Man": 4, "Captain America": 1, "Thor": 3}},
            {"option_text": "Super putere fizică", "score": {"Iron Man": 1, "Spider-Man": 2, "Captain America": 4, "Thor": 3}},
            {"option_text": "Manipulare a elementelor", "score": {"Iron Man": 4, "Spider-Man": 1, "Captain America": 2, "Thor": 3}}
        ]
    },
    {
        "question_text": "Care antagonist Marvel îți place cel mai mult?",
        "options": [
            {"option_text": "Loki", "score": {"Iron Man": 2, "Spider-Man": 3, "Captain America": 1, "Thor": 4}},
            {"option_text": "Green Goblin", "score": {"Iron Man": 1, "Spider-Man": 4, "Captain America": 2, "Thor": 3}},
            {"option_text": "Red Skull", "score": {"Iron Man": 3, "Spider-Man": 2, "Captain America": 4, "Thor": 1}},
            {"option_text": "Thanos", "score": {"Iron Man": 4, "Spider-Man": 1, "Captain America": 3, "Thor": 2}}
        ]
    }
]
# 6. Informații despre supereroi Marvel
marvel_hero_info = {
    "Iron Man": {"description": "Iron Man este un inventator genial și om de afaceri, echipat cu o armură puternică."},
    "Spider-Man": {"description": "Spider-Man este un tânăr erou cu abilități de a se deplasa pe pereți și lansa pânze de păianjen."},
    "Captain America": {"description": "Captain America este un super-soldat cu o scută indestructibilă și abilități fizice îmbunătățite."},
    "Thor": {"description": "Thor este zeul norvegian al tunetului și fulgerului, echipat cu un ciocan magic numit Mjolnir."}
}
# 7. Descriere pentru rezultatele Personality Quiz
descrieri_personalitate = {
    "extraverted": "Extrovertit: Ești sociabil, energic și poți să te adaptezi ușor la situații noi. Îți place să fii înconjurat de oameni și să participi la activități diverse.",
    "serious": "Serios: Ești dedicat, concentrat și te gândești profund la deciziile pe care le iei. Preferezi să analizezi situațiile în detaliu înainte de a acționa.",
    "responsible": "Responsabil: Ești de încredere, conștiincios și îți asumi responsabilitatea pentru acțiunile tale. Oamenii se bazează pe tine pentru a îndeplini sarcini importante.",
    "lively": "Vioi: Ești plin de viață, entuziast și mereu în căutare de noi aventuri. Ești spiritul petrecerii și aduci bucurie în jurul tău.",
    "dependable": "De încredere: Ești stabil, constant și oamenii se pot baza pe tine. Îți asumi responsabilități serioase și le îndeplinești cu sârguință."
}

@app.before_request
def init_menu():
    g.menu_pages = menu_pages
    g.user_data = user_data
    g.questions_princess_quiz = questions_princess_quiz
    g.questions_marvel_quiz = questions_marvel_quiz

@app.route("/")
def home():
    return render_template("index.html", active_page="home")

@app.route("/princess_quiz", methods=["GET", "POST"])
def princess_quiz():
  global scores
  scores = {"Cinderella": 0, "Ariel": 0, "Belle": 0, "Mulan": 0, "Elsa": 0, "Rapunzel": 0, "Tiana": 0}
  if request.method == "POST":
  # vreau sa arata toate rapunsurile posibile din form
    for i, question in enumerate(questions_princess_quiz):
        selected_answer = request.form.get(f"question_{i}")
        print(f"Răspunsul selectat pentru întrebarea {i} este: {selected_answer}")
        if selected_answer:
            for option in question["options"]:
                if option["option_text"] == selected_answer:
                    for character, score in option["score"].items():
                        scores[character] += score
    # print(scores)
    max_princess = max(scores, key=scores.get)
    max_princess_description = description_princess_quiz[max_princess]["description"]
    if scores[max_princess] == 0:
      return render_template("princess_quiz_results.html", active_page="princess_quiz", scores=scores, max_princess="Nimeni", max_princess_description="Nu ai răspuns la nicio întrebare.")
    return render_template("princess_quiz_results.html", active_page="princess_quiz", scores=scores, max_princess=max_princess, max_princess_description=max_princess_description)
  return render_template("princess_quiz.html", active_page="princess_quiz", questions=g.questions_princess_quiz)

@app.route("/princess_quiz_result", methods=["POST"])
def princess_quiz_results():
  return render_template("princess_quiz_results.html", active_page="princess_quiz")

@app.route("/personality_quiz", methods=["GET", "POST"])
def personality_quiz():
  if request.method == "GET":
    return render_template("personality_quiz.html", active_page="personality_quiz")
  else:
    age = int(request.form.get("varsta"))
    if age < 17:
      age = 17
    elif age > 28:
      age = 28
    
    neuroticism = request.form.get("neuroticism")
    openness = request.form.get("deschiderea")
    conscientiousness = request.form.get("constiinciozitate")
    extraversion = request.form.get("extraversiune")
    agreeableness = request.form.get("agreabilitate")
    gender = request.form.get("gen")
    # transformare in engleza
    if gender == "Masculin":
      gender = "Male"
    elif gender == "Feminin":
      gender = "Female"
    
    # pregatesc input data pentru predictie
    inputdata = [
      [
        gender, age,
        9 - int(openness),
        9 - int(neuroticism), 
        9 - int(conscientiousness),
        9 - int(agreeableness),
        9 - int(extraversion)
      ]
    ]
    # ajustez datele la gen
    for i in range(len(inputdata)):
      if inputdata[i][0] == "Male":
        inputdata[i][0] = 1
      else:
        inputdata[i][0] = 0
    
    df1 = pd.DataFrame(inputdata)
    testdf = df1[[0, 1, 2, 3, 4, 5, 6]]
    maintestarray = testdf.values

    y_pred = mul_lr.predict(maintestarray)
    for i in range(len(y_pred)):
        y_pred[i] = str((y_pred[i]))
    DF = pd.DataFrame(y_pred, columns=["Predicted Personality"])
    DF.index = DF.index + 1
    DF.index.names = ["Person No"]
    per = DF["Predicted Personality"].tolist()[0]
    print("Personalitate " + per)
    rezultat = descrieri_personalitate.get(per, "Nu există descriere pentru această personalitate.")
    print(rezultat)
    print(age, gender, extraversion, agreeableness, openness, conscientiousness, neuroticism)
    return render_template("personality_quiz_results.html", active_page="personality_quiz", personalitate=per, rezultat=rezultat)


@app.route("/about", methods=["POST", "GET"])
def about():
    email = request.form.get("email")
    password = request.form.get("password")
    checked = request.form.get("checkbox")
    range_value = request.form.get("rangeInput")
    print(email, password, checked, range_value)
    if checked == "on":
        g.user_data.append((email, password, checked))
        print(g.user_data)
    else:
        print("unchecked")
    return render_template("about.html", active_page="about")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
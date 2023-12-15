import re
from flask import render_template, request, jsonify, redirect, request, session, g
from flask import Flask
import json

app = Flask(__name__, static_folder="static")

#  add more if needed
menu_pages = [
    ("Home", "/", "home"),
    ("Princess Quiz", "/princess_quiz", "princess_quiz"),
    ("About", "/about", "about")
]
user_data = [
    ("admin", "admin", "checked")
]
questions_princess_quiz = [ {
      "question_text": "Care este culoarea ta preferată?",
      "options": [
        {
          "option_text": "Albastru",
          "score": {
            "Cinderella": 2,
            "Ariel": 1,
            "Belle": 3,
            "Mulan": 4
          }
        },
        {
          "option_text": "Roz",
          "score": {
            "Cinderella": 1,
            "Ariel": 3,
            "Belle": 2,
            "Mulan": 4
          }
        },
        {
          "option_text": "Galben",
          "score": {
            "Cinderella": 3,
            "Ariel": 2,
            "Belle": 4,
            "Mulan": 1
          }
        },
        {
          "option_text": "Verde",
          "score": {
            "Cinderella": 4,
            "Ariel": 1,
            "Belle": 3,
            "Mulan": 2
          }
        }
      ]
    },
    {
      "question_text": "Ce activitate îți place cel mai mult?",
      "options": [
        {
          "option_text": "Cântat",
          "score": {
            "Cinderella": 1,
            "Ariel": 3,
            "Belle": 2,
            "Mulan": 4
          }
        },
        {
          "option_text": "Citit",
          "score": {
            "Cinderella": 2,
            "Ariel": 1,
            "Belle": 4,
            "Mulan": 3
          }
        },
        {
          "option_text": "Dansat",
          "score": {
            "Cinderella": 4,
            "Ariel": 2,
            "Belle": 1,
            "Mulan": 3
          }
        },
        {
          "option_text": "Gătit",
          "score": {
            "Cinderella": 3,
            "Ariel": 1,
            "Belle": 2,
            "Mulan": 4
          }
        }
      ]
    },
    {
      "question_text": "Care este animalul tău preferat?",
      "options": [
        {
          "option_text": "Câine",
          "score": {
            "Cinderella": 2,
            "Ariel": 1,
            "Belle": 4,
            "Mulan": 3
          }
        },
        {
          "option_text": "Pisică",
          "score": {
            "Cinderella": 1,
            "Ariel": 3,
            "Belle": 2,
            "Mulan": 4
          }
        },
        {
          "option_text": "Pasăre",
          "score": {
            "Cinderella": 4,
            "Ariel": 2,
            "Belle": 3,
            "Mulan": 1
          }
        },
        {
          "option_text": "Cal",
          "score": {
            "Cinderella": 3,
            "Ariel": 1,
            "Belle": 2,
            "Mulan": 4
          }
        }
      ]
    }
]
scores = {"Cinderella": 0, "Ariel": 0, "Belle": 0, "Mulan": 0}

@app.before_request
def init_menu():
    g.menu_pages = menu_pages
    g.user_data = user_data
    g.questions_princess_quiz = questions_princess_quiz
    g.scores = scores

@app.route("/")
def home():
    return render_template("index.html", active_page="home")

@app.route("/princess_quiz", methods=["POST", "GET"])
def princess_quiz():
    # stiu ca am 8 raspunsuri posibile si vreau sa le arat in ordine
    for i, question in enumerate(questions_princess_quiz):
        # print(i, question["question_text"])
        selected_answer = request.form.get(f"question_{i + 1}")
        if selected_answer:
            for option in question["options"]:
                # print(option["option_text"])
                if option["option_text"] == selected_answer:
                    for character, score in option["score"].items():
                        scores[character] += score
    # add 1 to the score of Cinderella
    # scores["Cinderella"] += 1
    print(scores)
    return render_template("princess_quiz.html", active_page="princess_quiz")
    # return render_template("princess_quiz_results.html", active_page="princess_quiz")
    # return render_template("princess_quiz_results.html", active_page="princess_quiz", scores=scores)

@app.route("/princess_quiz_results")
def princess_quiz_results():
    return render_template("princess_quiz_results.html", active_page="princess_quiz")

@app.route("/about", methods=["POST", "GET"])
def about():
    email = request.form.get("email")
    password = request.form.get("password")
    checked = request.form.get("checkbox")
    # print(email, password, checked)
    if checked == "on":
        g.user_data.append((email, password, checked))
        print(g.user_data)
    else:
        print("unchecked")
    return render_template("about.html", active_page="about")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
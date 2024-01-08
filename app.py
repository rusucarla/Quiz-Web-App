import re
from flask import render_template, request, jsonify, redirect, request, session, g
from flask import Flask
import json

app = Flask(__name__, static_folder="static")

#  DICTIONARIES
# 1. menu_pages for the navbar
menu_pages = [
    ("Home", "/", "home"),
    ("About", "/about", "about"),
    ("Princess Quiz", "/princess_quiz", "princess_quiz"),
    ("Marvel Quiz", "/marvel_quiz", "marvel_quiz"),
    ("Cartoon Quiz", "/cartoon_quiz", "cartoon_quiz"),
    ("Outfit Quiz", "/outfit_quiz", "outfit_quiz"),
    ("Percy Jackson Quiz", "/pjo_quiz", "pjo_quiz"),
    ("Hunger Games Quiz", "/hungergames_quiz", "hungergames_quiz")
]
# 2. user_data for the about page
user_data = [
    ("admin", "admin", "checked")
]
# 3. questions_princess_quiz for the princess quiz
questions_princess_quiz = [ {
      "question_text": "Care este culoarea ta preferată?",
      "options": [
        {"option_text": "Albastru", "image_url": "../static/images/princess_quiz/question_1/albastru.png" , "score": {"Cinderella": 2, "Ariel": 1, "Belle": 3, "Mulan": 2, "Elsa": 1, "Rapunzel": 3, "Tiana": 2}},
        {"option_text": "Roz", "image_url": "../static/images/princess_quiz/question_1/roz.png", "score": {"Cinderella": 1, "Ariel": 3, "Belle": 2, "Mulan": 4, "Elsa": 3, "Rapunzel": 2, "Tiana": 1}},
        {"option_text": "Galben", "image_url": "../static/images/princess_quiz/question_1/galben.png", "score": {"Cinderella": 3, "Ariel": 2, "Belle": 4, "Mulan": 1, "Elsa": 4, "Rapunzel": 1, "Tiana": 2}},
        {"option_text": "Verde", "image_url": "../static/images/princess_quiz/question_1/verde.png", "score": {"Cinderella": 4, "Ariel": 1, "Belle": 3, "Mulan": 2, "Elsa": 2, "Rapunzel": 4, "Tiana": 1}}
      ]
    },
    {
      "question_text": "Ce activitate îți place cel mai mult?",
      "options": [
        {"option_text": "Cântat", "image_url": "../static/images/princess_quiz/question_2/cantat.jpg", "score": {"Cinderella": 1, "Ariel": 3, "Belle": 2, "Mulan": 1, "Elsa": 2, "Rapunzel": 3, "Tiana": 1}},
        {"option_text": "Citit", "image_url": "../static/images/princess_quiz/question_2/citit.jpg", "score": {"Cinderella": 2, "Ariel": 1, "Belle": 4, "Mulan": 3, "Elsa": 1, "Rapunzel": 2, "Tiana": 3}},
        {"option_text": "Dansat", "image_url": "../static/images/princess_quiz/question_2/dansat.jpg", "score": {"Cinderella": 4, "Ariel": 2, "Belle": 1, "Mulan": 2, "Elsa": 3, "Rapunzel": 1, "Tiana": 2}},
        {"option_text": "Gătit", "image_url": "../static/images/princess_quiz/question_2/gatit.jpg", "score": {"Cinderella": 3, "Ariel": 1, "Belle": 2, "Mulan": 4, "Elsa": 4, "Rapunzel": 2, "Tiana": 3}}
      ]
    },
    {
      "question_text": "Care este locul tău preferat pentru vacanță?",
      "options": [
        {"option_text": "Plajă exotică", "image_url": "../static/images/princess_quiz/question_3/plaja_exotica.jpg", "score": {"Cinderella": 1, "Ariel": 3, "Belle": 2, "Mulan": 1, "Elsa": 4, "Rapunzel": 1, "Tiana": 2}},
        {"option_text": "Munte", "image_url": "../static/images/princess_quiz/question_3/munte.jpg", "score": {"Cinderella": 2, "Ariel": 1, "Belle": 4, "Mulan": 3, "Elsa": 2, "Rapunzel": 3, "Tiana": 1}},
        {"option_text": "Oraș aglomerat", "image_url": "../static/images/princess_quiz/question_3/oras_aglomerat.jpg", "score": {"Cinderella": 4, "Ariel": 2, "Belle": 1, "Mulan": 3, "Elsa": 3, "Rapunzel": 2, "Tiana": 4}},
        {"option_text": "Sat liniștit", "image_url": "../static/images/princess_quiz/question_3/sat_linistit.jpg", "score": {"Cinderella": 3, "Ariel": 1, "Belle": 2, "Mulan": 3, "Elsa": 1, "Rapunzel": 4, "Tiana": 3}}
      ]
    },
    {
      "question_text": "Ce fel de muzică îți place cel mai mult?",
      "options": [
        {"option_text": "Pop", "image_url": "../static/images/princess_quiz/question_4/muzica_pop.jpg", "score": {"Cinderella": 1, "Ariel": 3, "Belle": 2, "Mulan": 1, "Elsa": 2, "Rapunzel": 3, "Tiana": 1}},
        {"option_text": "Rock", "image_url": "../static/images/princess_quiz/question_4/muzica_rock.jpg", "score": {"Cinderella": 2, "Ariel": 1, "Belle": 4, "Mulan": 2, "Elsa": 1, "Rapunzel": 2, "Tiana": 3}},
        {"option_text": "Clasică", "image_url": "../static/images/princess_quiz/question_4/muzica_clasica.jpg", "score": {"Cinderella": 4, "Ariel": 2, "Belle": 1, "Mulan": 3, "Elsa": 3, "Rapunzel": 1, "Tiana": 2}},
        {"option_text": "Jazz", "image_url": "../static/images/princess_quiz/question_4/muzica_jazz.jpg", "score": {"Cinderella": 3, "Ariel": 1, "Belle": 2, "Mulan": 2, "Elsa": 4, "Rapunzel": 2, "Tiana": 3}}
      ]
    },
    {
      "question_text": "Ce superputere ai vrea să ai?",
      "options": [
        {"option_text": "Invizibilitate", "image_url": "../static/images/princess_quiz/question_5/invizibilitate.jpg", "score": {"Cinderella": 1, "Ariel": 3, "Belle": 2, "Mulan": 4, "Elsa": 4, "Rapunzel": 1, "Tiana": 2}},
        {"option_text": "Zbor", "image_url": "../static/images/princess_quiz/question_5/zbor.jpg", "score": {"Cinderella": 2, "Ariel": 1, "Belle": 4, "Mulan": 2, "Elsa": 2, "Rapunzel": 3, "Tiana": 1}},
        {"option_text": "Superforță", "image_url": "../static/images/princess_quiz/question_5/superforta.jpg", "score": {"Cinderella": 4, "Ariel": 2, "Belle": 1, "Mulan": 1, "Elsa": 3, "Rapunzel": 2, "Tiana": 4}},
        {"option_text": "Teleportare", "image_url": "../static/images/princess_quiz/question_5/teleportare.jpg", "score": {"Cinderella": 3, "Ariel": 1, "Belle": 2, "Mulan": 4, "Elsa": 1, "Rapunzel": 4, "Tiana": 3}}
      ]
    },
    {
      "question_text": "Ce tip de film îți place să vezi?",
      "options": [
        {"option_text": "Dramă", "image_url": "../static/images/princess_quiz/question_6/drama.jpg", "score": {"Cinderella": 1, "Ariel": 3, "Belle": 2, "Mulan": 1, "Elsa": 2, "Rapunzel": 3, "Tiana": 1}},
        {"option_text": "Comedie", "image_url": "../static/images/princess_quiz/question_6/comedie.jpg", "score": {"Cinderella": 2, "Ariel": 1, "Belle": 4, "Mulan": 1, "Elsa": 1, "Rapunzel": 2, "Tiana": 3}},
        {"option_text": "Aventură", "image_url": "../static/images/princess_quiz/question_6/aventura.jpg", "score": {"Cinderella": 4, "Ariel": 2, "Belle": 1, "Mulan": 2, "Elsa": 3, "Rapunzel": 1, "Tiana": 2}},
        {"option_text": "SF", "image_url": "../static/images/princess_quiz/question_6/SF.jpg", "score": {"Cinderella": 3, "Ariel": 1, "Belle": 2, "Mulan": 4, "Elsa": 4, "Rapunzel": 2, "Tiana": 3}}
      ]
    },
    {
      "question_text": "Ce ai face într-o zi ploioasă?",
      "options": [
        {"option_text": "Citit o carte", "image_url": "../static/images/princess_quiz/question_7/citit_o_carte.jpg", "score": {"Cinderella": 1, "Ariel": 3, "Belle": 2, "Mulan": 4, "Elsa": 4, "Rapunzel": 1, "Tiana": 2}},
        {"option_text": "Uitat la ploaie", "image_url": "../static/images/princess_quiz/question_7/uitat_la_ploaie.jpg", "score": {"Cinderella": 2, "Ariel": 1, "Belle": 4, "Mulan": 3, "Elsa": 2, "Rapunzel": 3, "Tiana": 1}},
        {"option_text": "Făcut un puzzle", "image_url": "../static/images/princess_quiz/question_7/facut_un_puzzle.jpg", "score": {"Cinderella": 4, "Ariel": 2, "Belle": 1, "Mulan": 3, "Elsa": 3, "Rapunzel": 2, "Tiana": 4}},
        {"option_text": "Gătit ceva bun", "image_url": "../static/images/princess_quiz/question_7/gatit_ceva_bun.jpg", "score": {"Cinderella": 3, "Ariel": 1, "Belle": 2, "Mulan": 4, "Elsa": 1, "Rapunzel": 4, "Tiana": 3}}
      ]
    }
]
# 4. description for the princess quiz results
description_princess_quiz = {
  "Cinderella" : {"description": "Ești o persoană foarte ambițioasă și nu te lași până nu obții ceea ce îți dorești. Ești o persoană foarte bună și îți place să ajuți pe cei din jurul tău. Ești o persoană foarte curajoasă și nu te lași până nu îți atingi obiectivele."},
  "Ariel" : {"description": "Ești o persoană foarte curioasă și îți place să încerci lucruri noi. Ești o persoană foarte sensibilă și îți pasă foarte mult de cei din jurul tău. Ești o persoană foarte creativă și îți place să îți exprimi sentimentele prin artă."},
  "Belle" : {"description": "Ești o persoană foarte inteligentă și îți place să înveți lucruri noi. Ești o persoană foarte curajoasă și îți place să încerci lucruri noi. Ești o persoană foarte ambițioasă și nu te lași până nu îți atingi obiectivele."},
  "Mulan" : {"description": "Ești o persoană foarte curajoasă și îți place să încerci lucruri noi. Ești o persoană foarte ambițioasă și nu te lași până nu îți atingi obiectivele. Ești o persoană foarte inteligentă și îți place să înveți lucruri noi."},
  "Elsa" : {"description": "Ești o persoană foarte creativă și îți place să îți exprimi sentimentele prin artă. Ești o persoană foarte sensibilă și îți pasă foarte mult de cei din jurul tău. Ești o persoană foarte inteligentă și îți place să înveți lucruri noi."},
  "Rapunzel" : {"description": "Ești o persoană foarte creativă și îți place să îți exprimi sentimentele prin artă. Ești o persoană foarte sensibilă și îți pasă foarte mult de cei din jurul tău. Ești o persoană foarte curioasă și îți place să încerci lucruri noi."},
  "Tiana" : {"description": "Ești o persoană foarte ambițioasă și nu te lași până nu îți atingi obiectivele. Ești o persoană foarte curajoasă și îți place să încerci lucruri noi. Ești o persoană foarte inteligentă și îți place să înveți lucruri noi."}
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
    },
        {
        "question_text": "Care ar fi superarma ta preferată?",
        "options": [
            {"option_text": "Un arc și săgeți", "score": {"Iron Man": 1, "Spider-Man": 3, "Captain America": 2, "Thor": 4}},
            {"option_text": "O sabie laser", "score": {"Iron Man": 3, "Spider-Man": 2, "Captain America": 1, "Thor": 4}},
            {"option_text": "Un scut indestructibil", "score": {"Iron Man": 2, "Spider-Man": 1, "Captain America": 4, "Thor": 3}},
            {"option_text": "O armă cu raze laser", "score": {"Iron Man": 4, "Spider-Man": 1, "Captain America": 2, "Thor": 3}}
        ]
    },
    {
        "question_text": "Care este locul preferat pentru a-ți petrece vacanța?",
        "options": [
            {"option_text": "Un oraș vibrant", "score": {"Iron Man": 3, "Spider-Man": 2, "Captain America": 1, "Thor": 4}},
            {"option_text": "O plajă exotică", "score": {"Iron Man": 2, "Spider-Man": 4, "Captain America": 1, "Thor": 3}},
            {"option_text": "O zonă montană", "score": {"Iron Man": 1, "Spider-Man": 2, "Captain America": 4, "Thor": 3}},
            {"option_text": "O lume de poveste", "score": {"Iron Man": 4, "Spider-Man": 1, "Captain America": 2, "Thor": 3}}
        ]
    },
    {
        "question_text": "Ce calitate apreciezi cel mai mult la un supererou?",
        "options": [
            {"option_text": "Inteligența", "score": {"Iron Man": 4, "Spider-Man": 2, "Captain America": 1, "Thor": 3}},
            {"option_text": "Curtarea dreptății", "score": {"Iron Man": 2, "Spider-Man": 4, "Captain America": 3, "Thor": 1}},
            {"option_text": "Curajul", "score": {"Iron Man": 1, "Spider-Man": 3, "Captain America": 4, "Thor": 2}},
            {"option_text": "Puterea fizică", "score": {"Iron Man": 3, "Spider-Man": 1, "Captain America": 2, "Thor": 4}}
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

questions_cartoon_quiz = [
  {
    "question_text": "Ce fel de situație amuzantă ai prefera să gestionezi?",
    "options": [
        {"option_text": "Crearea unor capcane elaborate pentru a prinde pe cineva", "score": {"Tom": 4, "Jerry": 1, "Bugs Bunny": 2, "Tweety": 3}},
        {"option_text": "Evitarea cu succes a tuturor încercărilor altora de a te prinde", "score": {"Tom": 2, "Jerry": 4, "Bugs Bunny": 3, "Tweety": 1}},
        {"option_text": "Jucarea de farse altor persoane", "score": {"Tom": 1, "Jerry": 3, "Bugs Bunny": 4, "Tweety": 2}},
        {"option_text": "Întoarcerea întotdeauna împotriva altora și ieșirea mereu învingător", "score": {"Tom": 3, "Jerry": 2, "Bugs Bunny": 1, "Tweety": 4}}
    ]
},
{
    "question_text": "Ce superputere ai vrea să ai în situațiile amuzante?",
    "options": [
        {"option_text": "Capacitatea de a crea capcane sofisticate", "score": {"Tom": 4, "Jerry": 1, "Bugs Bunny": 2, "Tweety": 3}},
        {"option_text": "Abilitatea de a evita cu succes orice încercare de prindere", "score": {"Tom": 2, "Jerry": 4, "Bugs Bunny": 3, "Tweety": 1}},
        {"option_text": "Abilitatea de a juca farse amuzante altor persoane", "score": {"Tom": 1, "Jerry": 3, "Bugs Bunny": 4, "Tweety": 2}},
        {"option_text": "Puterea de a întoarce întotdeauna situația în favoarea ta", "score": {"Tom": 3, "Jerry": 2, "Bugs Bunny": 1, "Tweety": 4}}
    ]
},
{
    "question_text": "Care dintre următoarele activități îți place cel mai mult?",
    "options": [
        {"option_text": "Explorarea și descoperirea unor noi locuri", "score": {"Tom": 2, "Jerry": 4, "Bugs Bunny": 1, "Tweety": 3}},
        {"option_text": "Găsirea modalităților de a evita situațiile neplăcute", "score": {"Tom": 1, "Jerry": 3, "Bugs Bunny": 4, "Tweety": 2}},
        {"option_text": "Crearea unor planuri amuzante pentru a-i înșela pe ceilalți", "score": {"Tom": 4, "Jerry": 1, "Bugs Bunny": 2, "Tweety": 3}},
        {"option_text": "Bucurarea de momentele relaxante și liniștite", "score": {"Tom": 3, "Jerry": 2, "Bugs Bunny": 1, "Tweety": 4}}
    ]
},
{
    "question_text": "Ce tip de umor îți place cel mai mult?",
    "options": [
        {"option_text": "Umorul negru", "score": {"Tom": 4, "Jerry": 1, "Bugs Bunny": 2, "Tweety": 3}},
        {"option_text": "Ironia și umorul inteligent", "score": {"Tom": 2, "Jerry": 4, "Bugs Bunny": 3, "Tweety": 1}},
        {"option_text": "Farsele și glumele neașteptate", "score": {"Tom": 1, "Jerry": 3, "Bugs Bunny": 4, "Tweety": 2}},
        {"option_text": "Umorul plin de tandrețe și inocent", "score": {"Tom": 3, "Jerry": 2, "Bugs Bunny": 1, "Tweety": 4}}
    ]
},
{
    "question_text": "Ce strategie preferi în situațiile dificile?",
    "options": [
        {"option_text": "Planificarea atentă și executarea precisă", "score": {"Tom": 2, "Jerry": 4, "Bugs Bunny": 1, "Tweety": 3}},
        {"option_text": "Găsirea soluțiilor creative și neașteptate", "score": {"Tom": 4, "Jerry": 1, "Bugs Bunny": 2, "Tweety": 3}},
        {"option_text": "Evitarea situațiilor dificile", "score": {"Tom": 1, "Jerry": 3, "Bugs Bunny": 4, "Tweety": 2}},
        {"option_text": "Abordarea cu umor și relaxare", "score": {"Tom": 3, "Jerry": 2, "Bugs Bunny": 1, "Tweety": 4}}
    ]
},
{
    "question_text": "Ce activitate preferi să faci într-o zi liniștită?",
    "options": [
        {"option_text": "Citi o carte sau să stai la soare", "score": {"Tom": 2, "Jerry": 4, "Bugs Bunny": 1, "Tweety": 3}},
        {"option_text": "Explorarea unor noi aventuri și descoperirea lucrurilor amuzante", "score": {"Tom": 4, "Jerry": 1, "Bugs Bunny": 3, "Tweety": 2}},
        {"option_text": "Bucurarea de natură și a animalelor", "score": {"Tom": 1, "Jerry": 3, "Bugs Bunny": 2, "Tweety": 4}},
        {"option_text": "Relaxarea și contemplarea peisajului", "score": {"Tom": 3, "Jerry": 2, "Bugs Bunny": 1, "Tweety": 4}}
    ]
},
{
    "question_text": "Care dintre aceste expresii te reprezintă cel mai bine?",
    "options": [
        {"option_text": "Curios și mereu în mișcare", "score": {"Tom": 2, "Jerry": 4, "Bugs Bunny": 1, "Tweety": 3}},
        {"option_text": "Planificat și pus mereu la cale", "score": {"Tom": 4, "Jerry": 1, "Bugs Bunny": 3, "Tweety": 2}},
        {"option_text": "Relaxat și plin de umor", "score": {"Tom": 1, "Jerry": 3, "Bugs Bunny": 2, "Tweety": 4}},
        {"option_text": "Dulce și adorabil", "score": {"Tom": 3, "Jerry": 2, "Bugs Bunny": 1, "Tweety": 4}}
    ]
}
]

description_cartoons_quiz = {
    "Tom": {"description": "Tom este un motan gri care încearcă mereu să captureze șoarecii, dar deseori sfârșește printr-o situație comică."},
    "Jerry": {"description": "Jerry este un șoricel inteligent și dibaci, mereu pregătit să evadeze din încercările lui Tom."},
    "Bugs Bunny": {"description": "Bugs Bunny este un iepure amuzant și abil, cunoscut pentru replicile sale inteligente și situțiile comice."},
    "Tweety": {"description": "Tweety este un canar mic și galben, mereu pus în pericol de Sylvester, dar reușește să iasă mereu cu bine din situații."}
}

questions_hungergames_quiz = [

    {
        "question_text": "Care este abilitatea ta preferată?",
        "options": [
            {"option_text": "Să trag cu arcul", "score": {"Katniss": 3, "Peeta": 2, "Gale": 4, "Effie": 1, "Haymitch": 2, "Finnick": 3, "Prim": 1}},
            {"option_text": "Să negociez", "score": {"Katniss": 2, "Peeta": 3, "Gale": 1, "Effie": 4, "Haymitch": 3, "Finnick": 2, "Prim": 4}},
            {"option_text": "Supraviețuire în sălbăticie", "score": {"Katniss": 4, "Peeta": 1, "Gale": 3, "Effie": 2, "Haymitch": 1, "Finnick": 4, "Prim": 2}},
            {"option_text": "Planificare strategică", "score": {"Katniss": 1, "Peeta": 4, "Gale": 2, "Effie": 3, "Haymitch": 4, "Finnick": 1, "Prim": 3}}
        ]
    },
    {
        "question_text": "Ce tip de alianță preferi în arenă?",
        "options": [
            {"option_text": "Aliații puternici", "score": {"Katniss": 3, "Peeta": 2, "Gale": 4, "Effie": 1, "Haymitch": 2, "Finnick": 3, "Prim": 1}},
            {"option_text": "Aliații inteligenți", "score": {"Katniss": 2, "Peeta": 3, "Gale": 1, "Effie": 4, "Haymitch": 3, "Finnick": 2, "Prim": 4}},
            {"option_text": "Aliații de încredere", "score": {"Katniss": 4, "Peeta": 1, "Gale": 3, "Effie": 2, "Haymitch": 1, "Finnick": 4, "Prim": 2}},
            {"option_text": "Să fiu singur", "score": {"Katniss": 1, "Peeta": 4, "Gale": 2, "Effie": 3, "Haymitch": 4, "Finnick": 1, "Prim": 3}}
        ]
    },

{
    "question_text": "Ce strategie preferi în lupta din arenă?",
    "options": [
        {"option_text": "Evitare și ascundere", "score": {"Katniss": 3, "Peeta": 2, "Gale": 4, "Effie": 1, "Haymitch": 2, "Finnick": 3, "Prim": 1}},
        {"option_text": "Atac rapid și agresiv",  "score": {"Katniss": 2, "Peeta": 3, "Gale": 1, "Effie": 4, "Haymitch": 3, "Finnick": 2, "Prim": 4}},
        {"option_text": "Colaborare cu alte tributuri", "score": {"Katniss": 4, "Peeta": 1, "Gale": 3, "Effie": 2, "Haymitch": 1, "Finnick": 4, "Prim": 2}},
        {"option_text": "Dependență de echipament și tehnologie", "score": {"Katniss": 1, "Peeta": 4, "Gale": 2, "Effie": 3, "Haymitch": 4, "Finnick": 1, "Prim": 3}}
    ]
},
{
    "question_text": "Ce calități apreciezi cel mai mult la un aliat în arenă?",
    "options": [
        {"option_text": "Loialitatea", "image_url": "../static/images/hungergames_quiz/question_4/loialitate.jpg", "score": {"Katniss": 3, "Peeta": 2, "Gale": 4, "Effie": 1, "Haymitch": 2, "Finnick": 3, "Prim": 1}},
        {"option_text": "Inteligența", "image_url": "../static/images/hungergames_quiz/question_4/inteligenta.jpg", "score": {"Katniss": 2, "Peeta": 3, "Gale": 1, "Effie": 4, "Haymitch": 3, "Finnick": 2, "Prim": 4}},
        {"option_text": "Puterea fizică",   "score": {"Katniss": 4, "Peeta": 1, "Gale": 3, "Effie": 2, "Haymitch": 1, "Finnick": 4, "Prim": 2}},
        {"option_text": "Abilități de supraviețuire", "score": {"Katniss": 1, "Peeta": 4, "Gale": 2, "Effie": 3, "Haymitch": 4, "Finnick": 1, "Prim": 3}}
    ]
},
{
    "question_text": "Cum ai descrie abilitățile tale sociale?",
    "options": [
        {"option_text": "Extrem de sociabil",  "score": {"Katniss": 1, "Peeta": 4, "Gale": 2, "Effie": 3, "Haymitch": 1, "Finnick": 4, "Prim": 3}},
        {"option_text": "Moderat sociabil", "score": {"Katniss": 2, "Peeta": 3, "Gale": 1, "Effie": 4, "Haymitch": 3, "Finnick": 2, "Prim": 4}},
        {"option_text": "Rezervat", "score": {"Katniss": 4, "Peeta": 1, "Gale": 3, "Effie": 2, "Haymitch": 1, "Finnick": 4, "Prim": 2}},
        {"option_text": "Singuratic",  "score": {"Katniss": 3, "Peeta": 2, "Gale": 4, "Effie": 1, "Haymitch": 2, "Finnick": 3, "Prim": 1}}
    ]
},
{
    "question_text": "Ce importanță acorzi regulilor într-un mediu de competiție?",
    "options": [
        {"option_text": "Urmez întotdeauna regulile",  "score": {"Katniss": 2, "Peeta": 3, "Gale": 1, "Effie": 4, "Haymitch": 3, "Finnick": 2, "Prim": 4}},
        {"option_text": "Le încalc uneori pentru a supraviețui",  "score": {"Katniss": 4, "Peeta": 1, "Gale": 3, "Effie": 2, "Haymitch": 1, "Finnick": 4, "Prim": 2}},
        {"option_text": "Le adaptez în funcție de situație",  "score": {"Katniss": 3, "Peeta": 2, "Gale": 4, "Effie": 1, "Haymitch": 2, "Finnick": 3, "Prim": 1}},
        {"option_text": "Nu acord importanță regulilor", "score": {"Katniss": 1, "Peeta": 4, "Gale": 2, "Effie": 3, "Haymitch": 4, "Finnick": 1, "Prim": 3}}
    ]
},{
    "question_text": "Cum reacționezi în fața provocărilor neașteptate?",
    "options": [
        {"option_text": "Mă adaptez rapid și găsesc soluții", "image_url": "../static/images/hungergames_quiz/question_7/adaptare.jpg", "score": {"Katniss": 2, "Peeta": 3, "Gale": 1, "Effie": 4, "Haymitch": 3, "Finnick": 2, "Prim": 4}},
        {"option_text": "Rămân calm și gândesc strategic", "image_url": "../static/images/hungergames_quiz/question_7/strategie.jpg", "score": {"Katniss": 4, "Peeta": 1, "Gale": 3, "Effie": 2, "Haymitch": 1, "Finnick": 4, "Prim": 2}},
        {"option_text": "Caut sprijin în echipă", "image_url": "../static/images/hungergames_quiz/question_7/sprijin_echipa.jpg", "score": {"Katniss": 3, "Peeta": 2, "Gale": 4, "Effie": 1, "Haymitch": 2, "Finnick": 3, "Prim": 1}},
        {"option_text": "Simt o presiune intensă, dar mă descurc", "image_url": "../static/images/hungergames_quiz/question_7/presiune.jpg", "score": {"Katniss": 1, "Peeta": 4, "Gale": 2, "Effie": 3, "Haymitch": 4, "Finnick": 1, "Prim": 3}}
    ]
},
{
    "question_text": "Ce rol preferi într-un grup de supraviețuire?",
    "options": [
        {"option_text": "Lider", "score": {"Katniss": 4, "Peeta": 1, "Gale": 3, "Effie": 2, "Haymitch": 1, "Finnick": 4, "Prim": 2}},
        {"option_text": "Erou protector", "score": {"Katniss": 3, "Peeta": 2, "Gale": 4, "Effie": 1, "Haymitch": 2, "Finnick": 3, "Prim": 1}},
        {"option_text": "Strateg", "score": {"Katniss": 2, "Peeta": 3, "Gale": 1, "Effie": 4, "Haymitch": 3, "Finnick": 2, "Prim": 4}},
        {"option_text": "Sprijin moral", "score": {"Katniss": 1, "Peeta": 4, "Gale": 2, "Effie": 3, "Haymitch": 4, "Finnick": 1, "Prim": 3}}
    ]
}
]

# 2. descrieri pentru rezultatele Hunger Games quiz
description_hungergames_quiz = {
    "Katniss": {"description": "Ești ca Katniss - puternic(ă), capabil(ă) să tragi cu arcul și să supraviețuiești în condiții dificile."},
    "Peeta": {"description": "Ești ca Peeta - abil(ă) în negociere și planificare strategică, cu o atitudine cooperativă."},
    "Gale": {"description": "Ești ca Gale - puternic(ă) și capabil(ă) să se descurce în sălbăticie, dar poate mai retras(ă)."},
    "Effie": {"description": "Ești ca Effie - inteligent(ă), sociabil(ă) și cu abilități în negociere."},
    "Haymitch": {"description": "Ești ca Haymitch - strategic(ă), cu o abilitate de a supraviețui în orice situație."},
    "Finnick": {"description": "Ești ca Finnick - abil(ă) în luptă și priceput(ă) în utilizarea armelor tradiționale."},
    "Prim": {"description": "Ești ca Prim - altruist(ă), grijuliu(ă), și adesea orientat(ă) către ajutorarea altora."}
}

questions_outfit_quiz = [
  {
      "question_text": "Alege un top:",
      "options": [
        {"option_text": "1", "image_url": "https://5.imimg.com/data5/ECOM/Default/2022/11/CD/VA/SJ/61819412/y2k-aesthetic-lace-crop-top-cosmique-studio-2-85917-1647518600-500x500.png" , "score": {"ICONIC": 2, "oof": 1, "Haotic": 3, "Plin de succes": 2}},
        {"option_text": "2","image_url": "https://d2bzx2vuetkzse.cloudfront.net/fit-in/0x450/unshoppable_producs/8c4de4b2-4f84-4ff8-b710-8219cf348c65.png", "score": {"ICONIC": 1, "oof": 3, "Haotic": 2, "Plin de succes": 4}},
        {"option_text": "3","image_url": "https://image.pngaaa.com/35/2415035-middle.png", "score": {"ICONIC": 3, "oof": 2, "Haotic": 4, "Plin de succes": 1}},
        {"option_text": "4","image_url": "https://m.media-amazon.com/images/I/A13usaonutL._AC_CLa%7C2140%2C2000%7C91BD5Sd0sXL.png%7C0%2C0%2C2140%2C2000%2B0.0%2C0.0%2C2140.0%2C2000.0_UY1000_.png", "score": {"ICONIC": 4, "oof": 1, "Haotic": 3, "Plin de succes": 2}}
      ]
    },
        {
      "question_text": "Alege pantaloni sau fustă:",
      "options": [
        {"option_text": "1","image_url": "https://i.pinimg.com/originals/2c/07/97/2c0797cbc75e01dcc6dde00a0db4a259.jpg", "score": {"ICONIC": 2, "oof": 1, "Haotic": 3, "Plin de succes": 2}},
        {"option_text": "2","image_url": "https://i.pinimg.com/736x/50/9a/5c/509a5c2d5a7be721bdfcee8d18c35c26.jpg", "score": {"ICONIC": 1, "oof": 3, "Haotic": 2, "Plin de succes": 4}},
        {"option_text": "3","image_url": "https://w7.pngwing.com/pngs/710/614/png-transparent-denim-jeans-shorts-paper-jeans-textile-fashion-active-shorts.png", "score": {"ICONIC": 3, "oof": 2, "Haotic": 4, "Plin de succes": 1}},
        {"option_text": "4","image_url": "https://i.pinimg.com/originals/4a/f1/8a/4af18ac0cd41d1f4b230a5dc0d11408c.jpg", "score": {"ICONIC": 4, "oof": 1, "Haotic": 3, "Plin de succes": 2}}
      ]
    },
    {
      "question_text": "Alege un accesoriu:",
      "options": [
        {"option_text": "1","image_url": "https://ih1.redbubble.net/image.5181136823.2094/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg", "score": {"ICONIC": 1, "oof": 3, "Haotic": 2, "Plin de succes": 1}},
        {"option_text": "2","image_url": "https://www.pngitem.com/pimgs/m/184-1848969_star-moon-necklace-png-transparent-png.png", "score": {"ICONIC": 2, "oof": 1, "Haotic": 4, "Plin de succes": 3}},
        {"option_text": "3","image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgKxOZWKG4MJxxMgqdn9YoE5j9IC9ROex8u5bKYEnBL2kcvFH__FH2-ctk8hxbg_pKFSA&usqp=CAU", "score": {"ICONIC": 4, "oof": 2, "Haotic": 1, "Plin de succes": 2}},
        {"option_text": "4","image_url": "https://e7.pngegg.com/pngimages/618/607/png-clipart-watch-strap-watch-strap-titan-company-titan-men-s-wear-men-s-watch-thumbnail.png", "score": {"ICONIC": 3, "oof": 1, "Haotic": 2, "Plin de succes": 4}}
      ]
    },
    {
      "question_text": "Alege o geantă:",
      "options": [
        {"option_text": "1","image_url": "https://atlas-content-cdn.pixelsquid.com/stock-images/men-s-bag-black-messenger-o0LwWx7-600.jpg", "score": {"ICONIC": 2, "oof": 1, "Haotic": 3, "Plin de succes": 2}},
        {"option_text": "2","image_url": "https://cdn.webshopapp.com/shops/217/files/360539708/1652x2313x2/tote-bag-puppies.jpg", "score": {"ICONIC": 1, "oof": 3, "Haotic": 2, "Plin de succes": 4}},
        {"option_text": "3","image_url": "https://64.media.tumblr.com/4fdff3f91fcff61f7ff090b7ef3ec83c/59c440826fd5386e-40/s500x750/a550898c07ff4f949df897dc6209ed4ba7464340.png", "score": {"ICONIC": 3, "oof": 2, "Haotic": 4, "Plin de succes": 1}},
        {"option_text": "4","image_url": "https://png.pngtree.com/png-vector/20201127/ourmid/pngtree-fashion-female-bag-png-image_2393134.jpg", "score": {"ICONIC": 4, "oof": 1, "Haotic": 3, "Plin de succes": 2}}
      ]
    },
    {
      "question_text": "Alege o jachetă:",
      "options": [
        {"option_text": "1","image_url": "https://i.pinimg.com/originals/0a/b8/f3/0ab8f3fa2c8081dd572f1e2260abdaa7.png", "score": {"ICONIC": 1, "oof": 3, "Haotic": 2, "Plin de succes": 1}},
        {"option_text": "2","image_url": "https://i.pinimg.com/originals/02/fd/1f/02fd1f7fdd2f3d9d092a9fb6ed5cf797.png", "score": {"ICONIC": 2, "oof": 1, "Haotic": 4, "Plin de succes": 3}},
        {"option_text": "3","image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFnDU0ZBT7HcnE3FTkuXsu_X-45GDVW-46ca_6hvOlvZCUZMCCGeI8ye3qgxpLAAaka-0&usqp=CAU", "score": {"ICONIC": 4, "oof": 2, "Haotic": 1, "Plin de succes": 2}},
        {"option_text": "4","image_url": "https://m.media-amazon.com/images/I/41yaEOKIlEL._SR240,220_.jpg", "score": {"ICONIC": 3, "oof": 1, "Haotic": 2, "Plin de succes": 4}}
      ]
    },
    {
      "question_text": "Alege pantofi:",
      "options": [
        {"option_text": "1","image_url": "https://i.pinimg.com/originals/59/50/16/595016a51c9c2577c2d0f04e6334aa60.png", "score": {"ICONIC": 2, "oof": 1, "Haotic": 3, "Plin de succes": 2}},
        {"option_text": "2","image_url": "https://i.pinimg.com/474x/41/b0/5c/41b05c5f7f5fe08a52ac66aa76182b97.jpg", "score": {"ICONIC": 1, "oof": 3, "Haotic": 2, "Plin de succes": 4}},
        {"option_text": "3","image_url": "https://w7.pngwing.com/pngs/311/412/png-transparent-dr-martens-combat-boot-shoe-footwear-boot.png", "score": {"ICONIC": 3, "oof": 2, "Haotic": 4, "Plin de succes": 1}},
        {"option_text": "4","image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSujqS4Z8fahjHWQrpfUh7KxgM-EU_tOy9jgyhcHl0ZnVVWh7MNHNAvOLVMPRcWddefVAI&usqp=CAU", "score": {"ICONIC": 4, "oof": 1, "Haotic": 3, "Plin de succes": 2}}
      ]
    }

]
# 4. description for the princess quiz results
description_outfit_quiz = {
  "ICONIC" : {"description": "În 2024, vei emana un aer iconic, manifestând eleganță și rafinament. Garderoba ta va conține piese statement, iar prezența ta va rămâne întipărită în memoria celor din jur. Ești un simbol al stilului și eleganței contemporane."},
  "oof" : {"description": "Anul 2024 poate aduce și momente amuzante, dar asta nu îți afectează autenticitatea și umorul. Cu o atitudine relaxată și un strop de haz, vei străluci mereu în orice împrejurare."},
  "Haotic" : {"description": "Pentru tine, anul 2024 înseamnă o explozie de culoare și texturi. Garderoba ta reflectă energia creativă și haotică. Nu te sfiești să experimentezi combinații îndrăznețe, exprimându-ți individualitatea în moduri inovatoare."},
  "Plin de succes" : {"description": "Anul 2024 îți aduce succes și siguranță, reflectate și în alegerile tale vestimentare. Garderoba ta abundă în piese elegante și sofisticate, potrivite pentru orice ocazie. Ai găsit echilibrul perfect între stil și profesionalism"}
}

questions_pjo_quiz = [
{
"question_text": "Care dintre următoarele atribute te definesc cel mai bine?",
"options": [
{"option_text": "Inspirat și creativ", "score": {"Zeus": 1, "Poseidon": 2, "Athena": 3, "Apollo": 4}},
{"option_text": "Curajos și încrezător", "score": {"Zeus": 3, "Poseidon": 4, "Athena": 2, "Apollo": 1}},
{"option_text": "Rational și strategic", "score": {"Zeus": 2, "Poseidon": 1, "Athena": 4, "Apollo": 3}},
{"option_text": "Empatic și în armonie cu arta", "score": {"Zeus": 4, "Poseidon": 3, "Athena": 1, "Apollo": 2}}
]
},
{
"question_text": "Ce tip de călătorie ai prefera să faci?",
"options": [
{"option_text": "O călătorie plină de aventuri și descoperiri", "score": {"Zeus": 1, "Poseidon": 2, "Athena": 3, "Apollo": 4}},
{"option_text": "O călătorie pe mare, explorând adâncurile", "score": {"Zeus": 3, "Poseidon": 4, "Athena": 2, "Apollo": 1}},
{"option_text": "O călătorie strategică pentru a învăța și a câștiga cunoștințe", "score": {"Zeus": 2, "Poseidon": 1, "Athena": 4, "Apollo": 3}},
{"option_text": "O călătorie plină de inspirație artistică", "score": {"Zeus": 4, "Poseidon": 3, "Athena": 1, "Apollo": 2}}
]
},
{
"question_text": "Ce fel de muzică te atrage cel mai mult?",
"options": [
{"option_text": "Muzică plină de energie și putere", "score": {"Zeus": 1, "Poseidon": 2, "Athena": 3, "Apollo": 4}},
{"option_text": "Sunete ale naturii și ale oceanului", "score": {"Zeus": 3, "Poseidon": 4, "Athena": 2, "Apollo": 1}},
{"option_text": "Melodii clasice și armonice", "score": {"Zeus": 2, "Poseidon": 1, "Athena": 4, "Apollo": 3}},
{"option_text": "Muzică plină de creativitate și expresivitate", "score": {"Zeus": 4, "Poseidon": 3, "Athena": 1, "Apollo": 2}}
]
},
{
"question_text": "Cum ai descrie relația ta cu cunoașterea și învățarea?",
"options": [
{"option_text": "Îmi place să descopăr mereu lucruri noi", "score": {"Zeus": 1, "Poseidon": 2, "Athena": 3, "Apollo": 4}},
{"option_text": "Înțelegerea și explorarea adâncurilor necunoscute", "score": {"Zeus": 3, "Poseidon": 4, "Athena": 2, "Apollo": 1}},
{"option_text": "Abordarea pragmatică și strategică a cunoașterii", "score": {"Zeus": 2, "Poseidon": 1, "Athena": 4, "Apollo": 3}},
{"option_text": "Explorarea creativă și artistică a cunoașterii", "score": {"Zeus": 4, "Poseidon": 3, "Athena": 1, "Apollo": 2}}
]
},
{
"question_text": "Ce tip de putere preferi să deții?",
"options": [
{"option_text": "Puterea asupra fulgerelor și a vremii", "score": {"Zeus": 4, "Poseidon": 1, "Athena": 2, "Apollo": 3}},
{"option_text": "Controlul asupra apelor și al mărilor", "score": {"Zeus": 3, "Poseidon": 4, "Athena": 1, "Apollo": 2}},
{"option_text": "Puterea inteligenței și a strategiei", "score": {"Zeus": 2, "Poseidon": 3, "Athena": 4, "Apollo": 1}},
{"option_text": "Puterea creativității și a artei", "score": {"Zeus": 1, "Poseidon": 2, "Athena": 3, "Apollo": 4}}
]
},
{
"question_text": "Cum te vezi implicându-te într-o luptă sau conflict?",
"options": [
{"option_text": "Cu inspirație și conducând cu exemplul", "score": {"Zeus": 1, "Poseidon": 2, "Athena": 3, "Apollo": 4}},
{"option_text": "Cu puterea și controlul asupra elementelor", "score": {"Zeus": 3, "Poseidon": 4, "Athena": 1, "Apollo": 2}},
{"option_text": "Cu inteligența și planificarea strategică", "score": {"Zeus": 2, "Poseidon": 1, "Athena": 4, "Apollo": 3}},
{"option_text": "Prin exprimarea artistică și influențarea emoțională", "score": {"Zeus": 4, "Poseidon": 3, "Athena": 1, "Apollo": 2}}
]
},
{
"question_text": "Cum te descurci în situații de presiune și stres?",
"options": [
{"option_text": "Mă inspir și găsesc soluții creative", "score": {"Zeus": 1, "Poseidon": 2, "Athena": 3, "Apollo": 4}},
{"option_text": "Mă adaptez și acționez calm în fața provocărilor", "score": {"Zeus": 3, "Poseidon": 4, "Athena": 1, "Apollo": 2}},
{"option_text": "Gândesc strategic și iau decizii raționale", "score": {"Zeus": 2, "Poseidon": 1, "Athena": 4, "Apollo": 3}},
{"option_text": "Mă exprim artistic și canalizez stresul în creație", "score": {"Zeus": 4, "Poseidon": 3, "Athena": 1, "Apollo": 2}}
]
},
{
"question_text": "Ce activitate artistică te atrage cel mai mult?",
"options": [
{"option_text": "Sculptură și lucrul cu materiale solide", "score": {"Zeus": 1, "Poseidon": 2, "Athena": 3, "Apollo": 4}},
{"option_text": "Pictură și exprimare vizuală", "score": {"Zeus": 3, "Poseidon": 4, "Athena": 1, "Apollo": 2}},
{"option_text": "Scrierea și exprimarea prin cuvinte", "score": {"Zeus": 2, "Poseidon": 1, "Athena": 4, "Apollo": 3}},
{"option_text": "Muzică și exprimare auditivă", "score": {"Zeus": 4, "Poseidon": 3, "Athena": 1, "Apollo": 2}}
]
}
]



description_pjo_quiz = {
"Zeus": {"description": "Zeus, regele zeilor, stăpânul cerului și al fulgerelor, este cunoscut pentru puterea și inspirația sa."},
"Poseidon": {"description": "Poseidon, stăpânul mărilor și al valurilor, controlează apele și este cunoscut pentru forța sa."},
"Athena": {"description": "Athena, zeița înțelepciunii și a războiului strategic, este cunoscută pentru inteligența și planificarea sa."},
"Apollo": {"description": "Apollo, zeul artelor și al luminii, este cunoscut pentru creativitatea și influența sa artistică."}
}

questions_hp_quiz = [
    {
        "question_text": "Ce calitate te definește cel mai bine?",
        "options": [
            {"option_text": "Curajos și hotărât", "score": {"Gryffindor": 4, "Hufflepuff": 2, "Ravenclaw": 1, "Slytherin": 3}},
            {"option_text": "Loial și dornic de prietenii", "score": {"Gryffindor": 2, "Hufflepuff": 4, "Ravenclaw": 3, "Slytherin": 1}},
            {"option_text": "Inteligent și înțelept", "score": {"Gryffindor": 1, "Hufflepuff": 3, "Ravenclaw": 4, "Slytherin": 2}},
            {"option_text": "Ambițios și gata să facă orice pentru a-și atinge scopul", "score": {"Gryffindor": 3, "Hufflepuff": 1, "Ravenclaw": 2, "Slytherin": 4}}
        ]
    },
    {
        "question_text": "Ce materie ți-ar plăcea cel mai mult la școală?",
        "options": [
            {"option_text": "Vrăjitorii și vrăjitoarele celebre din trecut", "score": {"Gryffindor": 1, "Hufflepuff": 3, "Ravenclaw": 4, "Slytherin": 2}},
            {"option_text": "Atelierele de creaturi magice", "score": {"Gryffindor": 2, "Hufflepuff": 4, "Ravenclaw": 1, "Slytherin": 3}},
            {"option_text": "Studiul obiectelor fermecate", "score": {"Gryffindor": 3, "Hufflepuff": 1, "Ravenclaw": 2, "Slytherin": 4}},
            {"option_text": "Leacuri și poțiuni magice", "score": {"Gryffindor": 4, "Hufflepuff": 2, "Ravenclaw": 3, "Slytherin": 1}}
        ]
    },
    {
        "question_text": "Care ar fi casa ta preferată pentru vacanța de la școală?",
        "options": [
            {"option_text": "Explorarea pădurii și a naturii", "score": {"Gryffindor": 3, "Hufflepuff": 4, "Ravenclaw": 2, "Slytherin": 1}},
            {"option_text": "Petrecerea timpului cu prietenii și familia", "score": {"Gryffindor": 2, "Hufflepuff": 3, "Ravenclaw": 1, "Slytherin": 4}},
            {"option_text": "Cititul și învățarea într-un mediu liniștit", "score": {"Gryffindor": 1, "Hufflepuff": 2, "Ravenclaw": 4, "Slytherin": 3}},
            {"option_text": "Explorarea zonelor misterioase și interzise", "score": {"Gryffindor": 4, "Hufflepuff": 1, "Ravenclaw": 3, "Slytherin": 2}}
        ]
    },
    {
        "question_text": "Cum te-ai descrie într-un cuvânt?",
        "options": [
            {"option_text": "Curajos", "score": {"Gryffindor": 4, "Hufflepuff": 2, "Ravenclaw": 1, "Slytherin": 3}},
            {"option_text": "Loial", "score": {"Gryffindor": 2, "Hufflepuff": 4, "Ravenclaw": 3, "Slytherin": 1}},
            {"option_text": "Inteligență", "score": {"Gryffindor": 1, "Hufflepuff": 3, "Ravenclaw": 4, "Slytherin": 2}},
            {"option_text": "Ambițios", "score": {"Gryffindor": 3, "Hufflepuff": 1, "Ravenclaw": 2, "Slytherin": 4}}
        ]
    },
    {
        "question_text": "Ce calitate apreciezi cel mai mult la ceilalți?",
        "options": [
            {"option_text": "Curajul", "score": {"Gryffindor": 4, "Hufflepuff": 2, "Ravenclaw": 1, "Slytherin": 3}},
            {"option_text": "Loialitatea", "score": {"Gryffindor": 2, "Hufflepuff": 4, "Ravenclaw": 3, "Slytherin": 1}},
            {"option_text": "Inteligența", "score": {"Gryffindor": 1, "Hufflepuff": 3, "Ravenclaw": 4, "Slytherin": 2}},
            {"option_text": "Ambiția", "score": {"Gryffindor": 3, "Hufflepuff": 1, "Ravenclaw": 2, "Slytherin": 4}}
        ]
    },
    {
        "question_text": "Care dintre aceste animale fantastice îți place cel mai mult?",
        "options": [
            {"option_text": "Dragonul", "score": {"Gryffindor": 3, "Hufflepuff": 2, "Ravenclaw": 1, "Slytherin": 4}},
            {"option_text": "Hipogrif", "score": {"Gryffindor": 4, "Hufflepuff": 3, "Ravenclaw": 2, "Slytherin": 1}},
            {"option_text": "Phoenix", "score": {"Gryffindor": 2, "Hufflepuff": 1, "Ravenclaw": 3, "Slytherin": 4}},
            {"option_text": "Basilisc", "score": {"Gryffindor": 1, "Hufflepuff": 4, "Ravenclaw": 3, "Slytherin": 2}}
        ]
    },
        {
      "question_text": "Dacă ai avea un animal de companie magic, ce ai alege?",
      "options": [
        {"option_text": "Bufniță", "score": {"Gryffindor": 2, "Slytherin": 1, "Ravenclaw": 4, "Hufflepuff": 3}},
        {"option_text": "Șarpe", "score": {"Gryffindor": 1, "Slytherin": 4, "Ravenclaw": 3, "Hufflepuff": 2}},
        {"option_text": "Dragon", "score": {"Gryffindor": 3, "Slytherin": 2, "Ravenclaw": 1, "Hufflepuff": 4}},
        {"option_text": "Hippogriff", "score": {"Gryffindor": 4, "Slytherin": 1, "Ravenclaw": 2, "Hufflepuff": 3}}
      ]
    },
    {
      "question_text": "Care ar fi obiectul tău magic preferat?",
      "options": [
        {"option_text": "Bagheta", "score": {"Gryffindor": 2, "Slytherin": 1, "Ravenclaw": 4, "Hufflepuff": 3}},
        {"option_text": "Inelul Puterii", "score": {"Gryffindor": 1, "Slytherin": 4, "Ravenclaw": 3, "Hufflepuff": 2}},
        {"option_text": "Pergamentul Invisibil", "score": {"Gryffindor": 3, "Slytherin": 2, "Ravenclaw": 1, "Hufflepuff": 4}},
        {"option_text": "Pietrele Filozofale", "score": {"Gryffindor": 4, "Slytherin": 1, "Ravenclaw": 2, "Hufflepuff": 3}}
      ]
    }
]

description_hp_quiz = {
    "Gryffindor": {"description": "Casa Gryffindor este cunoscută pentru curajul, hotărârea și spiritul de aventură."},
    "Hufflepuff": {"description": "Hufflepuff este casa loialității, prieteniei și muncii asidue."},
    "Ravenclaw": {"description": "Ravenclaw își prețuiește inteligența, creativitatea și căutarea cunoașterii."},
    "Slytherin": {"description": "Slytherin este casa celor ambițioși, determinați și dornici de putere."}
}

questions_spirit_animal_quiz = [
{
    "question_text": "Care cuvânt te descrie cel mai bine?",
    "options": [
        {"option_text": "Energic", "score": {"Lup": 3, "Bufnita": 2, "Delfin": 1, "Vulpe": 4}},
        {"option_text": "Prietenoasă", "score": {"Lup": 2, "Bufnita": 3, "Delfin": 4, "Vulpe": 1}},
        {"option_text": "Înțeleaptă", "score": {"Lup": 1, "Bufnita": 4, "Delfin": 3, "Vulpe": 2}},
        {"option_text": "Agilă", "score": {"Lup": 4, "Bufnita": 1, "Delfin": 2, "Vulpe": 3}}
    ]
},
{
    "question_text": "Ce mediu preferi?",
    "options": [
        {"option_text": "Pădure", "score": {"Lup": 3, "Bufnita": 2, "Delfin": 1, "Vulpe": 4}},
        {"option_text": "Cerul senin", "score": {"Lup": 2, "Bufnita": 3, "Delfin": 4, "Vulpe": 1}},
        {"option_text": "Oceanul", "score": {"Lup": 1, "Bufnita": 4, "Delfin": 3, "Vulpe": 2}},
        {"option_text": "Zonă cu multe ascunzători", "score": {"Lup": 4, "Bufnita": 1, "Delfin": 2, "Vulpe": 3}}
    ]
},
{
    "question_text": "Ce calități apreciezi la ceilalți?",
    "options": [
        {"option_text": "Curaj", "score": {"Lup": 3, "Bufnita": 2, "Delfin": 1, "Vulpe": 4}},
        {"option_text": "Înțelepciune", "score": {"Lup": 2, "Bufnita": 3, "Delfin": 4, "Vulpe": 1}},
        {"option_text": "Jucăușenie", "score": {"Lup": 1, "Bufnita": 4, "Delfin": 3, "Vulpe": 2}},
        {"option_text": "Agilitate", "score": {"Lup": 4, "Bufnita": 1, "Delfin": 2, "Vulpe": 3}}
    ]
},
{
    "question_text": "Ce activitate preferi?",
    "options": [
        {"option_text": "Vânătoare", "score": {"Lup": 3, "Bufnita": 2, "Delfin": 1, "Vulpe": 4}},
        {"option_text": "Citit", "score": {"Lup": 2, "Bufnita": 3, "Delfin": 4, "Vulpe": 1}},
        {"option_text": "Înot", "score": {"Lup": 1, "Bufnita": 4, "Delfin": 3, "Vulpe": 2}},
        {"option_text": "Explorare", "score": {"Lup": 4, "Bufnita": 1, "Delfin": 2, "Vulpe": 3}}
    ]
},
{
    "question_text": "Care este hobby-ul tău preferat?",
    "options": [
        {"option_text": "Alergat sau sportul în aer liber", "score": {"Lup": 4, "Bufnita": 1, "Delfin": 2, "Vulpe": 3}},
        {"option_text": "Citirea cărților sau învațarea lucrurilor noi", "score": {"Lup": 2, "Bufnita": 3, "Delfin": 4, "Vulpe": 1}},
        {"option_text": "Socializarea cu prietenii", "score": {"Lup": 1, "Bufnita": 4, "Delfin": 3, "Vulpe": 2}},
        {"option_text": "Descoperirea unor locuri noi și necunoscute", "score": {"Lup": 3, "Bufnita": 2, "Delfin": 1, "Vulpe": 4}}
    ]
},
{
    "question_text": "Ce superputere ți-ai dori să ai?",
    "options": [
        {"option_text": "Viteză și forță extraordinară", "score": {"Lup": 4, "Bufnita": 1, "Delfin": 2, "Vulpe": 3}},
        {"option_text": "Invizibilitate și citirea minților", "score": {"Lup": 2, "Bufnita": 3, "Delfin": 4, "Vulpe": 1}},
        {"option_text": "Vindecare rapidă și conexiune cu natura", "score": {"Lup": 1, "Bufnita": 4, "Delfin": 3, "Vulpe": 2}},
        {"option_text": "Abilitatea de a schimba formele", "score": {"Lup": 3, "Bufnita": 2, "Delfin": 1, "Vulpe": 4}}
    ]
},
{
    "question_text": "Ce fel de călătorie ți-ar plăcea cel mai mult?",
    "options": [
        {"option_text": "O aventură într-o pădure sălbatică", "score": {"Lup": 3, "Bufnita": 2, "Delfin": 1, "Vulpe": 4}},
        {"option_text": "O călătorie la un muzeu de artă sau știință", "score": {"Lup": 2, "Bufnita": 3, "Delfin": 4, "Vulpe": 1}},
        {"option_text": "O relaxare la plajă cu prietenii", "score": {"Lup": 1, "Bufnita": 4, "Delfin": 3, "Vulpe": 2}},
        {"option_text": "O explorare a unor orașe necunoscute", "score": {"Lup": 4, "Bufnita": 1, "Delfin": 2, "Vulpe": 3}}
    ]
},
{
    "question_text": "Cum îți petreci timpul liber obișnuit?",
    "options": [
        {"option_text": "Practic sport sau activități fizice", "score": {"Lup": 4, "Bufnita": 1, "Delfin": 2, "Vulpe": 3}},
        {"option_text": "Citesc sau învat în liniște", "score": {"Lup": 2, "Bufnita": 3, "Delfin": 4, "Vulpe": 1}},
        {"option_text": "Petrec timp cu prietenii și familia", "score": {"Lup": 1, "Bufnita": 4, "Delfin": 3, "Vulpe": 2}},
        {"option_text": "Explorez locuri noi și îndepărtate", "score": {"Lup": 3, "Bufnita": 2, "Delfin": 1, "Vulpe": 4}}
    ]
}
]

description_spirit_animal_quiz = {
    "Lup": {"description": "Animalul tau spiritual este Lupul. Ești cunoscut pentru loialitate și putere."},
    "Bufnita": {"description": "Animalul tau spiritual este Bufnița. Ești înțelept și observator."},
    "Delfin": {"description": "Animalul tau spiritual este Delfinul. Ești jucăuș și prietenos."},
    "Vulpe": {"description": "Animalul tau spiritual este Vulpea. Ești agil și plin de surprize."}
}
questions_teacher_quiz = [
    {
        "question_text": "Cum ti-ai petrece o zi de vineri?",
        "options": [
            {"option_text": "Dezlantuindu-ma", "score": {"RD": 4, "Negrescu": 3, "Lumi": 3, "Ghiu": 1, "Rosner": 4, "Balan": 1}},
            {"option_text": "Self-care si somn la ora 9", "score": {"RD": 1, "Negrescu": 2, "Lumi": 3, "Ghiu": 2, "Rosner": 1, "Balan": 4}},
            {"option_text": "Facand oamenii sa sufere", "score": {"RD": 1, "Negrescu": 2, "Lumi": 4, "Ghiu": 4, "Rosner": 3, "Balan": 2}},
            {"option_text": "Plangand pana adorm", "score": {"RD": 1, "Negrescu": 4, "Lumi": 2, "Ghiu": 4, "Rosner": 3, "Balan": 1}}
        ]
    },
    {
        "question_text": "Cine e modelul tau in viata?",
        "options": [
            {"option_text": "Elon Musk", "score": {"RD": 4, "Negrescu": 3, "Lumi": 1, "Ghiu": 2, "Rosner": 4, "Balan": 1}},
            {"option_text": "Britney Spears", "score": {"RD": 3, "Negrescu": 2, "Lumi": 4, "Ghiu": 1, "Rosner": 2, "Balan": 2}},
            {"option_text": "Regina Elisabeta 2", "score": {"RD": 1, "Negrescu": 2, "Lumi": 1, "Ghiu": 3, "Rosner": 3, "Balan": 4}},
            {"option_text": "Alexandru Negrescu", "score": {"RD": 1, "Negrescu": 4, "Lumi": 4, "Ghiu": 2, "Rosner": 3, "Balan": 1}}
        ]
    },
    {
        "question_text": "Cat de pasionat esti de moda?",
        "options": [
            {"option_text": "E VIATA MEA", "score": {"RD": 3, "Negrescu": 3, "Lumi": 4, "Ghiu": 1, "Rosner": 1, "Balan": 3}},
            {"option_text": "incerc", "score": {"RD": 3, "Negrescu": 3, "Lumi": 3, "Ghiu": 1, "Rosner": 3, "Balan": 4}},
            {"option_text": "ce e aia moda", "score": {"RD": 1, "Negrescu": 1, "Lumi": 1, "Ghiu": 4, "Rosner": 3, "Balan": 1}},
            {"option_text": "trag un tricou pe mine dimineata si plec", "score": {"RD": 2, "Negrescu": 1, "Lumi": 1, "Ghiu": 4, "Rosner": 3, "Balan": 1}}
        ]
    },
        {
        "question_text": "Ce parere ai despre copii?",
        "options": [
            {"option_text": "Scorpii", "score": {"RD": 2, "Negrescu": 2, "Lumi": 4, "Ghiu": 4, "Rosner": 2, "Balan": 1}},
            {"option_text": "ADORABILI", "score": {"RD": 3, "Negrescu": 2, "Lumi": 1, "Ghiu": 1, "Rosner": 1, "Balan": 4}},
            {"option_text": "wdym eu sunt un copil", "score": {"RD": 4, "Negrescu": 4, "Lumi": 1, "Ghiu": 1, "Rosner": 1, "Balan": 1}},
            {"option_text": "ii vreau pentru alocatie", "score": {"RD": 2, "Negrescu": 3, "Lumi": 3, "Ghiu": 4, "Rosner": 4, "Balan": 1}}
        ]
    },
    {
        "question_text": "La ce te gandesti inainte sa adormi?",
        "options": [
            {"option_text": "bani", "score": {"RD": 4, "Negrescu": 2, "Lumi": 3, "Ghiu": 1, "Rosner": 4, "Balan": 2}},
            {"option_text": "moduri de tortura", "score": {"RD": 1, "Negrescu": 2, "Lumi": 3, "Ghiu": 4, "Rosner": 3, "Balan": 1}},
            {"option_text": "gagici!", "score": {"RD": 4, "Negrescu": 3, "Lumi": 4, "Ghiu": 1, "Rosner": 4, "Balan": 1}},
            {"option_text": "cat de scurta sa fie fusta mea maine", "score": {"RD": 3, "Negrescu": 2, "Lumi": 4, "Ghiu": 3, "Rosner": 1, "Balan": 2}}
        ]
    },
    {
        "question_text": "Ce meserie ai alege?",
        "options": [
            {"option_text": "ACTOR!", "score": {"RD": 3, "Negrescu": 4, "Lumi": 4, "Ghiu": 1, "Rosner": 2, "Balan": 1}},
            {"option_text": "participant la IUMOR", "score": {"RD": 4, "Negrescu": 3, "Lumi": 2, "Ghiu": 1, "Rosner": 2, "Balan": 1}},
            {"option_text": "criminal", "score": {"RD": 2, "Negrescu": 3, "Lumi": 1, "Ghiu": 4, "Rosner": 4, "Balan": 2}},
            {"option_text": "icon", "score": {"RD": 4, "Negrescu": 4, "Lumi": 4, "Ghiu": 3, "Rosner": 1, "Balan": 4}}
        ]
    }
]
# 6. Informații despre supereroi Marvel
description_teacher_quiz = {
    "RD": {"description": "Esti o persoana energica si foarte misto. Nu te omori dupa ce crede lumea dar pare ca ai fost clovnul clasei in generala."},
    "Negrescu": {"description": "You're a child trapped in an old man's body with a baby face. Foarte funny, dar ai grija la ce glume spui si ce leaks din viata de zi cu zi dai."},
    "Lumi": {"description": "You are an iconic b***h. Iti place sa torturezi putin lumea, dar o faci cu stil."},
    "Ghiu": {"description": "Esti un tip cam ciudat, misogin, care are dubiosul obicei de a scrie pe pereti. Iti place sa torturezi oamenii. Probabil asta ascunde niste traume din copilarie. Te-ai intrebat vreodata daca ai mommy issues?"},
    "Rosner": {"description": "Nu esti un om, esti AI. Te rog vorbeste mai incet ca nu esti amuzant chiar daca incerci sa fii. Also nu toata lumea vrea sa fie corporatist."},
    "Balan": {"description": "Ai un zambet de milioane. Nu am vazut persoana care sa aiba viata mai put together. Pui suflet in tot ce faci si esti super pasionat de interesele tale. You go girl!"}
}

@app.before_request
def init_menu():
    g.menu_pages = menu_pages
    g.user_data = user_data
    g.questions_princess_quiz = questions_princess_quiz
    g.questions_marvel_quiz = questions_marvel_quiz
    g.questions_hungergames_quiz = questions_hungergames_quiz
    g.questions_cartoon_quiz = questions_cartoon_quiz
    g.questions_outfit_quiz = questions_outfit_quiz
    g.questions_hp_quiz = questions_hp_quiz
    g.questions_spirit_animal_quiz = questions_spirit_animal_quiz
    g.questions_teacher_quiz = questions_teacher_quiz
    # g.scores = scores

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
  # return render_template("princess_quiz_results.html", active_page="princess_quiz", scores=scores)

@app.route("/princess_quiz_result", methods=["POST"])
def princess_quiz_results():
  return render_template("princess_quiz_results.html", active_page="princess_quiz")


@app.route("/marvel_quiz", methods=["GET", "POST"])
def marvel_quiz():
    global scores
    scores = {"Iron Man": 0, "Spider-Man": 0, "Captain America": 0, "Thor": 0}
    if request.method == "POST":
        # Afișează toate răspunsurile posibile din formular
        for i, question in enumerate(questions_marvel_quiz):
            selected_answer = request.form.get(f"question_{i}")
            print(f"Răspunsul selectat pentru întrebarea {i} este: {selected_answer}")
            if selected_answer:
                for option in question["options"]:
                    if option["option_text"] == selected_answer:
                        for character, score in option["score"].items():
                            scores[character] += score

        max_hero = max(scores, key=scores.get)
        max_hero_description = marvel_hero_info[max_hero]["description"]

        if scores[max_hero] == 0:
            return render_template("marvel_quiz_results.html", active_page="marvel_quiz", scores=scores, max_hero="Nimeni", max_hero_description="Nu ai răspuns la nicio întrebare.")

        return render_template("marvel_quiz_results.html", active_page="marvel_quiz", scores=scores, max_hero=max_hero, max_hero_description=max_hero_description)

    return render_template("marvel_quiz.html", active_page="marvel_quiz", questions=questions_marvel_quiz)

# Route-ul pentru rezultatele testului Marvel
@app.route("/marvel_quiz_result", methods=["POST"])
def marvel_quiz_results():
    return render_template("marvel_quiz_results.html", active_page="marvel_quiz")

@app.route("/cartoon_quiz", methods=["GET", "POST"])
def cartoon_quiz():
    global scores
    scores = {"Tom": 0, "Jerry": 0, "Bugs Bunny": 0, "Tweety": 0}
    if request.method == "POST":
        for i, question in enumerate(questions_cartoon_quiz):
            selected_answer = request.form.get(f"question_{i}")
            print(f"Răspunsul selectat pentru întrebarea {i} este: {selected_answer}")
            if selected_answer:
                for option in question["options"]:
                    if option["option_text"] == selected_answer:
                        for character, score in option["score"].items():
                            scores[character] += score
        max_character = max(scores, key=scores.get)
        max_character_description = description_cartoons_quiz[max_character]["description"]
        if scores[max_character] == 0:
            return render_template("cartoon_quiz_results.html", active_page="cartoon_quiz", scores=scores, max_character="Nimeni", max_character_description="Nu ai răspuns la nicio întrebare.")
        return render_template("cartoon_quiz_results.html", active_page="cartoon_quiz", scores=scores, max_character=max_character, max_character_description=max_character_description)
    return render_template("cartoon_quiz.html", active_page="cartoon_quiz", questions=questions_cartoon_quiz)

@app.route("/cartoon_quiz_results", methods=["POST"])
def cartoon_quiz_results():
    return render_template("cartoon_quiz_results.html", active_page="cartoon_quiz")

@app.route("/hungergames_quiz", methods=["GET", "POST"])
def hungergames_quiz():
    global scores
    scores = {"Katniss": 0, "Peeta": 0, "Gale": 0, "Effie": 0, "Haymitch": 0, "Finnick": 0, "Prim": 0}
    if request.method == "POST":
        for i, question in enumerate(questions_hungergames_quiz):
            selected_answer = request.form.get(f"question_{i}")
            print(f"Răspunsul selectat pentru întrebarea {i} este: {selected_answer}")
            if selected_answer:
                for option in question["options"]:
                    if option["option_text"] == selected_answer:
                        for character, score in option["score"].items():
                            scores[character] += score
        max_character = max(scores, key=scores.get)
        max_character_description = description_hungergames_quiz[max_character]["description"]
        if scores[max_character] == 0:
            return render_template("hungergames_quiz_results.html", active_page="hungergames_quiz", scores=scores, max_character="Nimeni", max_character_description="Nu ai răspuns la nicio întrebare.")
        return render_template("hungergames_quiz_results.html", active_page="hungergames_quiz", scores=scores, max_character=max_character, max_character_description=max_character_description)
    return render_template("hungergames_quiz.html", active_page="hungergames_quiz", questions=questions_hungergames_quiz)

@app.route("/hungergames_quiz_results", methods=["POST"])
def hungergames_quiz_results():
    return render_template("hungergames_quiz_results.html", active_page="hungergames_quiz")

@app.route("/outfit_quiz", methods=["GET", "POST"])
def outfit_quiz():
    global scores
    scores = {"ICONIC": 0, "oof": 0, "Haotic": 0, "Plin de succes": 0}
    if request.method == "POST":
        for i, question in enumerate(questions_outfit_quiz):
            selected_answer = request.form.get(f"question_{i}")
            print(f"Răspunsul selectat pentru întrebarea {i} este: {selected_answer}")
            if selected_answer:
                for option in question["options"]:
                    if option["option_text"] == selected_answer:
                        for character, score in option["score"].items():
                            scores[character] += score
        max_result = max(scores, key=scores.get)
        max_result_description = description_outfit_quiz[max_result]["description"]
        if scores[max_result] == 0:
            return render_template("outfit_quiz_results.html", active_page="outfit_quiz", scores=scores, max_result="Nimeni", max_result_description="Nu ai răspuns la nicio întrebare.")
        return render_template("outfit_quiz_results.html", active_page="outfit_quiz", scores=scores, max_result=max_result, max_result_description=max_result_description)
    return render_template("outfit_quiz.html", active_page="outfit_quiz", questions=questions_outfit_quiz)

@app.route("/outfit_quiz_results", methods=["POST"])
def outfit_quiz_results():
    return render_template("outfit_quiz_results.html", active_page="outfit_quiz")

@app.route("/pjo_quiz", methods=["GET", "POST"])
def pjo_quiz():
    global scores
    scores = {"Zeus": 0, "Poseidon": 0, "Athena": 0, "Apollo": 0}
    if request.method == "POST":
        # Afișează toate răspunsurile posibile din formular
        for i, question in enumerate(questions_pjo_quiz):
            selected_answer = request.form.get(f"question_{i}")
            print(f"Răspunsul selectat pentru întrebarea {i} este: {selected_answer}")
            if selected_answer:
                for option in question["options"]:
                    if option["option_text"] == selected_answer:
                        for character, score in option["score"].items():
                            scores[character] += score

        max_hero = max(scores, key=scores.get)
        max_hero_description = description_pjo_quiz[max_hero]["description"]

        if scores[max_hero] == 0:
            return render_template("pjo_quiz_results.html", active_page="pjo_quiz", scores=scores, max_hero="Nimeni", max_hero_description="Nu ai răspuns la nicio întrebare.")

        return render_template("pjo_quiz_results.html", active_page="pjo_quiz", scores=scores, max_hero=max_hero, max_hero_description=max_hero_description)

    return render_template("pjo_quiz.html", active_page="pjo_quiz", questions=questions_pjo_quiz)

# Route-ul pentru rezultatele testului Marvel
@app.route("/pjo_quiz_result", methods=["POST"])
def pjo_quiz_results():
    return render_template("pjo_quiz_results.html", active_page="pjo_quiz")

@app.route("/hp_quiz", methods=["GET", "POST"])
def hp_quiz():
    global scores
    scores = {"Gryffindor": 0, "Hufflepuff": 0, "Slytherin": 0, "Ravenclaw": 0}
    if request.method == "POST":
        # Afișează toate răspunsurile posibile din formular
        for i, question in enumerate(questions_hp_quiz):
            selected_answer = request.form.get(f"question_{i}")
            print(f"Răspunsul selectat pentru întrebarea {i} este: {selected_answer}")
            if selected_answer:
                for option in question["options"]:
                    if option["option_text"] == selected_answer:
                        for character, score in option["score"].items():
                            scores[character] += score

        max_hero = max(scores, key=scores.get)
        max_hero_description = description_hp_quiz[max_hero]["description"]

        if scores[max_hero] == 0:
            return render_template("hp_quiz_results.html", active_page="hp_quiz", scores=scores, max_hero="Nimeni", max_hero_description="Nu ai răspuns la nicio întrebare.")

        return render_template("hp_quiz_results.html", active_page="hp_quiz", scores=scores, max_hero=max_hero, max_hero_description=max_hero_description)

    return render_template("hp_quiz.html", active_page="hp_quiz", questions=questions_hp_quiz)

# Route-ul pentru rezultatele testului Marvel
@app.route("/hp_quiz_result", methods=["POST"])
def hp_quiz_results():
    return render_template("hp_quiz_results.html", active_page="hp_quiz")


@app.route("/spirit_animal_quiz", methods=["GET", "POST"])
def spirit_animal_quiz():
    global scores
    scores = {"Lup": 0, "Bufnita": 0, "Delfin": 0, "Vulpe": 0}
    if request.method == "POST":
        # Afișează toate răspunsurile posibile din formular
        for i, question in enumerate(questions_spirit_animal_quiz):
            selected_answer = request.form.get(f"question_{i}")
            print(f"Răspunsul selectat pentru întrebarea {i} este: {selected_answer}")
            if selected_answer:
                for option in question["options"]:
                    if option["option_text"] == selected_answer:
                        for character, score in option["score"].items():
                            scores[character] += score

        max_hero = max(scores, key=scores.get)
        max_hero_description = description_spirit_animal_quiz[max_hero]["description"]

        if scores[max_hero] == 0:
            return render_template("spirit_animal_quiz_results.html", active_page="spirit_animal_quiz", scores=scores, max_hero="Nimeni", max_hero_description="Nu ai răspuns la nicio întrebare.")

        return render_template("spirit_animal_quiz_results.html", active_page="spirit_animal_quiz", scores=scores, max_hero=max_hero, max_hero_description=max_hero_description)

    return render_template("spirit_animal_quiz.html", active_page="spirit_animal_quiz", questions=questions_spirit_animal_quiz)

# Route-ul pentru rezultatele testului Marvel
@app.route("/spirit_animal_quiz_result", methods=["POST"])
def spirit_animal_quiz_results():
    return render_template("spirit_animal_quiz_results.html", active_page="spirit_animal_quiz")

@app.route("/teacher_quiz", methods=["GET", "POST"])
def teacher_quiz():
    global scores
    scores = {"RD": 0, "Negrescu": 0, "Lumi": 0, "Ghiu": 0, "Rosner": 0, "Balan": 0}
    if request.method == "POST":
        # Afișează toate răspunsurile posibile din formular
        for i, question in enumerate(questions_teacher_quiz):
            selected_answer = request.form.get(f"question_{i}")
            print(f"Răspunsul selectat pentru întrebarea {i} este: {selected_answer}")
            if selected_answer:
                for option in question["options"]:
                    if option["option_text"] == selected_answer:
                        for character, score in option["score"].items():
                            scores[character] += score

        max_hero = max(scores, key=scores.get)
        max_hero_description = description_teacher_quiz[max_hero]["description"]

        if scores[max_hero] == 0:
            return render_template("teacher_quiz_results.html", active_page="teacher_quiz", scores=scores, max_hero="Nimeni", max_hero_description="Nu ai răspuns la nicio întrebare.")

        return render_template("teacher_quiz_results.html", active_page="teacher_quiz", scores=scores, max_hero=max_hero, max_hero_description=max_hero_description)

    return render_template("teacher_quiz.html", active_page="teacher_quiz", questions=questions_teacher_quiz)

# Route-ul pentru rezultatele testului Marvel
@app.route("/teacher_quiz_result", methods=["POST"])
def teacher_quiz_results():
    return render_template("teacher_quiz_results.html", active_page="teacher_quiz")

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
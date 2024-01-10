# Quiz-Web-App

Titlu scurt al proiectului : Quiz Web App

## Echipa

- Banu Daria
- Iordache Ioana
- Mihai Alexia
- Rusu Carla

## Descriere proiect

Descrierea funcționalității minime + dorite :

- mai multe quiz-uri (stil buzzfeed si poate mbti)
- dupa ce utilizatorul termina quiz-ul poate sa primeasca rezultatul intr-un pdf sau poate si pe mail

Componentele arhitecturale :

- backend : flask cel mai probabil -> we did that
- frontend : html si css -> we did that
- transformare in pdf : reportlab (python) -> we did that
- trimitere mail : smtplib si/ sau Yagmail -> nu se mai poate in aplicatii necomerciale
- fisiere pentru quiz-uri : cel mai probabil json-uri -> we did that

## Nivel de experienta : toate suntem incepatoare in python si avem un minim de experienta in html

## Soft Deadline : 9.01.2024

## Implementare

### Backend

Am folosit flask pentru a lega frontend-ul de backend. Am creat un server care
primeste request-uri de la frontend si trimite raspunsuri inapoi.

Am folosit dictionare json pentru a stoca intrebarile si raspunsurile. Pe langa
acestea, mai avem si descrierile pentru rezultatele quiz-ului.

Mai "special" este quiz-ul de personalitate, pentru care am folosit si
componente din ce am putea numi machine learning. Am folosit un model (link : [5Personalities](https://github.com/thenithinbalaji/5Personalities)) pentru a prezice rezultatul in functie de raspunsurile utilizatorului.
Modelul este unul simplut, dar care functioneaza destul de bine.

Pentru a crea atmosfera autentica a unui quiz de personalitate, am folosit si
reportlab pentru a avea un ghid de interpretare a rezultatului. Acesta este un
element nelipsit din majoritatea site-urilor de acest gen. Nici PDF-ul nu este
cel mai complex, dar este suficient pentru a demonstra capabiliatea de a crea un
ghid de personalitate cu sfaturi generalizate si care sa fie usor de citit.

### Frontend

Am folosit html si css pentru a crea interfata grafica a aplicatiei. Am folosit
si Jinja2 pentru a putea face template-uri pentru paginile html.

A fost foarte folositor pentru quiz-uri deoarece ne-a permis sa facem un
template pentru a afisa intrebarile si raspunsurile, dar sa pastram
personalitatea fiecarui quiz intacta (in sensul in care aproape fiecare quiz are
alta tematica cromatica).

Am folosit si un pic de javascript pentru a asigura ca utilizatorul vede clar ce
raspuns a ales (evident, alta culoare de highlight si select la fiecare quiz -
pentru ca asa e frumos).

### Dificultati intampinate

Am avut o mica problema cu Jinja2 cand trebuia sa afiseze intrebarile si
raspunsurile si sincer am rezolvat-o cu CTRL+C si CTRL+V. Am incercat sa
reporduc problema si nu am reusit, deci nu stiu exact ce s-a intamplat.
### Partea de react 
1) Asigura-te ca ai Nodejs instalat. Mai jos gasesti niste tutoriale utile:
<br>
https://www.youtube.com/watch?v=PNAnLczSBmQ&t=0s
<br>
Daca lucrati pe WSL/Linux/Mac :
<br>
https://www.youtube.com/watch?v=R73JI8rwkKc

2) Inapoi in proiect rulati urm :
<br>
(Daca aveti folderul node_modules stergeti-l nu dati commit cu el ca o ia razna git)
<br><br>
```
cd bitcoin_quizz
npm install 
npm start
```
<br><br>
Trebuie sa ii dati npm start ca sa il vada si flasku. Apoi
```
cd ..
python3 app.py
```
Si selectati din site quizul
<H4>De ce nu am folosit react build pt deployment?</H4>
<br>
Nu merge comanda

```
serve -h
```  
chiar daca l-am instalat.
<br>

## Instuctiuni rulare/folosire

Pentru a deschide pagina web cu quizurile, se ruleaza comanda python3 app.py
in folderul Quiz-Web-App.
Quizul 'bitcoin_quizz' se ruleaza separat:

- din folderul bitcoin_quizz se dau comenzile npm install si npm start
- se ruleaza python3 app.py

## Contributii individuale

- Banu Daria
  - partile de React

- Iordache Ioana
  - frontend - intregul proiect

- Mihai Alexia
  - implementarea unor quizuri (backend)

- Rusu Carla
  - implementarea unor quizuri (backend)
  - functionalitatile legate de reportlab
  - quiz-ul de personalitate (Machine Learning)

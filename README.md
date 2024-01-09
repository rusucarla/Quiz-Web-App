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
componente din ce am putea numi machine learning. Am folosit un model (gasit :
TODO) pentru a prezice rezultatul in functie de raspunsurile utilizatorului.
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

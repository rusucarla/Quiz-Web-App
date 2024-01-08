# Quiz-Web-App

Titlu scurt al proiectului : Quiz Web App

## Echipa

- Banu
- Iordache
- Mihai
- Rusu

## Descriere proiect

Descrierea funcționalității minime + dorite :

- mai multe quiz-uri (stil buzzfeed si poate mbti)
- dupa ce utilizatorul termina quiz-ul poate sa primeasca rezultatul intr-un pdf sau poate si pe mail

Componentele arhitecturale :

- backend : flask cel mai probabil
- frontend : html si css
- transformare in pdf : reportlab (python)
- trimitere mail : smtplib si/ sau Yagmail
- fisiere pentru quiz-uri : cel mai probabil json-uri

## Nivel de experienta : toate suntem incepatoare in python si avem un minim de experienta in html

## Soft Deadline : 9.01.2024

## Pentru partea de react:

Ca sa functioneze si bitcoin quizz faceti asa:

1) Instalati nodejs
https://www.youtube.com/watch?v=PNAnLczSBmQ&t=0s
<br>
Daca lucrati pe WSL/Linux/Mac :
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
Si selectati din site quizul ca for some reason doar asa imi afiseaza imaginile din background 
<H3>De ce nu am folosit react build pt deployment?</H3>
<br>
Nu merge comanda

```
serve -h
```  
chiar daca l-am instalat.
<br>

import os

# Obține și afișează directorul curent de lucru
current_directory = os.getcwd()
print("Directorul curent:", current_directory)

# Verifică din nou pentru a te asigura că schimbarea a avut loc
print("Noul director de lucru:", os.getcwd())

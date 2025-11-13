from sklearn.tree import DecisionTreeClassifier
import pandas as pd

from tabulate import tabulate

import csv
from datetime import datetime



# Citirea datelor
df = pd.read_csv("student_data.csv")

# Verificăm coloanele
print("Coloanele disponibile în CSV:", df.columns)

# Folosim doar coloanele disponibile
X = df[["Nota", "Timp_studiu"]]

# Creăm un target simplu pentru test: promovare dacă Nota >= 5
y = (df["Nota"] >= 5).astype(str)  # "True" sau "False"

# Crearea și antrenarea modelului
model = DecisionTreeClassifier()
model.fit(X, y)

# Interacțiune cu utilizatorul
try:
    nota = float(input("Introdu Nota studentului: "))
    timp_studiu = float(input("Introdu Timpul de studiu : "))
except ValueError:
    print("Te rog să introduci doar numere!")
    exit()

student_nou = [[nota, timp_studiu]]
rezultat_pred = model.predict(student_nou)

print(f"Predicția pentru studentul cu Nota={nota} și Timp_de_studiu={timp_studiu} este: {rezultat_pred[0]}")

# Salvăm datele și rezultatul în jurnalul CSV
with open("predictii_studenti.csv", mode="a", newline="") as fisier:
    writer = csv.writer(fisier)
    writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nota, timp_studiu, rezultat_pred])
print("🗂️ Datele și predicția au fost salvate în 'predictii_studenti.csv'.")

# Pregătim tabelul pentru afișare
tabel = [["Nota", "Timp de studiu ", "Predicție"],
         [nota, timp_studiu, rezultat_pred]]

# Afișare tabel frumos
print("\n📄 Mini-raport student:")
print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))


from sklearn.tree import DecisionTreeClassifier
import pandas as pd

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
    timp = float(input("Introdu Timpul de studiu (ore): "))
except ValueError:
    print("Te rog să introduci doar numere!")
    exit()

student_nou = [[nota, timp]]
rezultat = model.predict(student_nou)

print(f"Predicția pentru studentul cu Nota={nota} și Timp_de_studiu={timp} este: {rezultat[0]}")


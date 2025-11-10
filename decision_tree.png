# decision_tree.py

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# --- 1. Citim datele ---
df = pd.read_csv("student.csv")  # Asigură-te că student.csv este în același folder

# --- 2. Pregătim variabilele ---
X = df[["Nota", "Timp_de_studiu"]]
y = df["Promovat"]

# --- 3. Creăm modelul ---
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X, y)

# --- 4. Afișăm arborele ---
plt.figure(figsize=(10,5))
tree.plot_tree(model, feature_names=["Nota", "Timp_de_studiu"], class_names=["Nu", "Da"], filled=True)
plt.show()

# --- 5. Predicție pentru un nou student ---
# Exemplu: Nota=7, Timp_de_studiu=5 ore
new_student = [[7, 5]]
prediction = model.predict(new_student)
print(f"Predicția pentru studentul cu Nota={new_student[0][0]} și Timp_de_studiu={new_student[0][1]} este: {prediction[0]}")


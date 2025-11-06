import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 1️⃣ Citim datele
df = pd.read_csv("student.csv")
df.columns = df.columns.str.replace(" ", "_")  # elimină spațiile, preventiv

# 2️⃣ Pregătim datele (variabilele de intrare și ieșire)
X = df[["Varsta", "Nota", "Timp_de_studiu"]]
y = df["Promovat"]

# 3️⃣ Împărțim în set de antrenare și testare
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4️⃣ Creăm modelul
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

# 5️⃣ Calculăm importanța caracteristicilor
importances = model.feature_importances_

# 6️⃣ Afișăm în terminal
print("\n📊 Importanța caracteristicilor:")
for name, value in zip(X.columns, importances):
    print(f"{name}: {value:.3f}")

# 7️⃣ Vizualizăm grafic
plt.bar(X.columns, importances, color="skyblue")
plt.title("Importanța caracteristicilor în modelul ML")
plt.xlabel("Caracteristică")
plt.ylabel("Importanță")
plt.show()

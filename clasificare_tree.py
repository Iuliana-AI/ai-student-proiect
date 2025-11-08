import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Încarcă baza de date
data = pd.read_csv("student_data.csv")

# Separăm variabilele de intrare (X) și variabila țintă (y)
X = data[["Varsta", "Nota", "Timp_de_studiu"]]
y = data["Rezultat"]

# Împărțim datele în train și test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Antrenăm modelul
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Preziceri pe setul de test
y_pred = model.predict(X_test)

# Evaluare
print("📊 Acuratețea modelului:", accuracy_score(y_test, y_pred))
print("\n📄 Raport de clasificare:\n", classification_report(y_test, y_pred))

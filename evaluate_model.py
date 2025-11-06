import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Citim datele
df = pd.read_csv("student.csv")
df.columns = df.columns.str.replace(" ", "_")

# 2️⃣ Pregătim datele
X = df[["Varsta", "Nota", "Timp_de_studiu"]]
y = df["Promovat"]

# 3️⃣ Împărțim în set de antrenare și testare
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4️⃣ Antrenăm modelul
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

# 5️⃣ Facem predicții
y_pred = model.predict(X_test)

# 6️⃣ Evaluăm performanța
acc = accuracy_score(y_test, y_pred)
print(f"📊 Acuratețea modelului: {acc:.2f}")

print("\n📄 Raport de clasificare:")
print(classification_report(y_test, y_pred))

print("\n🧩 Matricea de confuzie:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# 7️⃣ Vizualizare grafică a matricei de confuzie
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Nu", "Da"],
    yticklabels=["Nu", "Da"],
)
plt.xlabel("Predicții")
plt.ylabel("Etichete reale")
plt.title("Matricea de confuzie")
plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Citim datele
df = pd.read_csv("student_data.csv")

# Creăm o coloană nouă: "A_promovat" (1 = da, 0 = nu)
df["A_promovat"] = df["Nota"].apply(lambda x: 1 if x >= 5 else 0)

# Alegem variabilele de intrare (features) și ieșirea (target)
X = df[["Varsta", "Timp_studiu", "Nota"]]
y = df["A_promovat"]

# Împărțim datele în set de antrenare și testare (80% / 20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Creăm modelul
model = DecisionTreeClassifier(max_depth=3, random_state=42)

# Antrenăm modelul
model.fit(X_train, y_train)

# Verificăm acuratețea
accuracy = model.score(X_test, y_test)
print(f"✅ Acuratețea modelului: {accuracy:.2f}")

# === VIZUALIZARE ===
plt.figure(figsize=(10, 6))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Nu a promovat", "A promovat"],
    filled=True,
    rounded=True,
)
plt.title("🌳 Arbore de decizie - Clasificare Studenți")
plt.show()

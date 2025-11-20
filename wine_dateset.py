from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Încarcă datele
wine = load_wine()
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = wine.target

# 2️⃣ Split train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3️⃣ Creează și antrenează Random Forest
model = RandomForestClassifier(
    n_estimators=100,
    max_features='sqrt',
    random_state=42
)
model.fit(X_train, y_train)

# 4️⃣ Predicții și evaluare
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 5️⃣ Importanța feature-urilor
importances = model.feature_importances_
feature_names = X.columns

# Sortare descrescătoare pentru vizualizare
sorted_idx = importances.argsort()[::-1]

# Vizualizare
plt.figure(figsize=(10,6))
plt.bar(range(len(importances)), importances[sorted_idx])
plt.xticks(range(len(importances)), feature_names[sorted_idx], rotation=90)
plt.title("Importanța feature-urilor - Wine Dataset")
plt.show()

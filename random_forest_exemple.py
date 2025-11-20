# ===== 1️⃣ Import librării =====
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ===== 2️⃣ Generare dataset fictiv =====
np.random.seed(42)  # pentru reproducibilitate
X = pd.DataFrame({
    'feature1': np.random.rand(100),
    'feature2': np.random.rand(100),
    'feature3': np.random.rand(100),
    'feature4': np.random.rand(100)
})
y = np.random.randint(0, 2, 100)  # țintă binară 0/1

# ===== 3️⃣ Split train/test =====
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===== 4️⃣ Creare și antrenare Random Forest =====
model = RandomForestClassifier(
    n_estimators=100,      # număr arbori
    max_features='sqrt',   # subset aleator de feature-uri la fiecare split
    random_state=42
)
model.fit(X_train, y_train)

# ===== 5️⃣ Predicții =====
y_pred = model.predict(X_test)
print("Predicții pentru datele de test:", y_pred)

# ===== 6️⃣ Evaluare =====
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# ===== 7️⃣ Importanța feature-urilor =====
importances = model.feature_importances_
for feature, importance in zip(X.columns, importances):
    print(f"{feature}: {importance:.3f}")

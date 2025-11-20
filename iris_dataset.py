# ===== 1️⃣ Import librării =====
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# ===== 2️⃣ Încarcă date reale (Iris) =====
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target  # 0,1,2 -> clasele florilor

# ===== 3️⃣ Split train/test =====
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===== 4️⃣ Creează și antrenează Random Forest =====
model = RandomForestClassifier(
    n_estimators=100,
    max_features='sqrt',
    random_state=42
)
model.fit(X_train, y_train)

# ===== 5️⃣ Predicții și evaluare =====
y_pred = model.predict(X_test)
print("Predicții:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))

# ===== 6️⃣ Importanța feature-urilor =====
importances = model.feature_importances_
for feature, importance in zip(X.columns, importances):
    print(f"{feature}: {importance:.3f}")

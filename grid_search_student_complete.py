# grid_search_student_complete.py
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold
import matplotlib.pyplot as plt
import joblib

# ===============================
# 1️⃣ Incarcare CSV
# ===============================
df = pd.read_csv("student.csv")

X = df[["Nota", "Timp_de_studiu"]]
y = df["Promovat"]

# ===============================
# 2️⃣ Determinam cate fold-uri putem folosi
# ===============================
min_class_count = min(y.value_counts())
n_splits = min(5, min_class_count)
print(f"Folosim {n_splits} fold-uri (cea mai mica clasa are {min_class_count} exemple)")

cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

# ===============================
# 3️⃣ Decision Tree GridSearch
# ===============================
dt = DecisionTreeClassifier(random_state=42)
param_grid_dt = {'max_depth': [2, 3, 4, 5, 6, None]}

gs_dt = GridSearchCV(dt, param_grid_dt, scoring='accuracy', cv=cv)
gs_dt.fit(X, y)

print("\n✅ DECISION TREE")
print("Best max_depth:", gs_dt.best_params_['max_depth'])
print("CV mean accuracy:", round(gs_dt.best_score_, 4))

# ===============================
# 4️⃣ Random Forest GridSearch
# ===============================
rf = RandomForestClassifier(random_state=42)
param_grid_rf = {
    'n_estimators': [50, 100],
    'max_depth': [None, 3, 5, 10]
}

gs_rf = GridSearchCV(rf, param_grid_rf, scoring='accuracy', cv=cv)
gs_rf.fit(X, y)

print("\n✅ RANDOM FOREST")
print("Best params:", gs_rf.best_params_)
print("CV mean accuracy:", round(gs_rf.best_score_, 4))

# ===============================
# 5️⃣ Salvam modelele antrenate
# ===============================
joblib.dump(gs_dt.best_estimator_, "decision_tree_model.pkl")
joblib.dump(gs_rf.best_estimator_, "random_forest_model.pkl")
print("\nModelele au fost salvate in 'decision_tree_model.pkl' si 'random_forest_model.pkl'")

# ===============================
# 6️⃣ Vizualizare arbore Decision Tree
# ===============================
plt.figure(figsize=(12,6))
plot_tree(gs_dt.best_estimator_, feature_names=X.columns, class_names=['Ne-promovat','Promovat'], filled=True)
plt.title("Decision Tree")
plt.show()

# ===============================
# 7️⃣ Vizualizare feature importance Random Forest
# ===============================
importances = gs_rf.best_estimator_.feature_importances_
plt.figure(figsize=(8,4))
plt.bar(X.columns, importances)
plt.title("Feature Importance - Random Forest")
plt.show()

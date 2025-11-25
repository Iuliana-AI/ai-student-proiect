# grid_search_student_final.py
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import accuracy_score

# 1️⃣ Încarcă datele tale
df = pd.read_csv("student.csv")

# 2️⃣ Definește X și y
X = df[["Nota", "Timp_de_studiu"]]
y = df["Promovat"]

# 3️⃣ Determină numărul maxim de fold-uri pentru CV
min_class_count = min(y.value_counts())
n_splits = min(5, min_class_count)  # max 5 fold-uri, sau mai puțin dacă dataset mic

cv_strategy = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

print(f"🔹 Folosim {n_splits} fold-uri în StratifiedKFold (minim exemple din fiecare clasă: {min_class_count})")

# 4️⃣ Decision Tree - GridSearch pe max_depth
dt = DecisionTreeClassifier(random_state=42)
param_grid_dt = {'max_depth': [2, 3, 4, 5, 6, None]}  # poți ajusta

gs_dt = GridSearchCV(dt, param_grid_dt, cv=cv_strategy, scoring='accuracy', n_jobs=-1)
gs_dt.fit(X, y)

best_dt = gs_dt.best_estimator_
dt_cv_score = gs_dt.best_score_

print("\n✅ Decision Tree")
print("Best max_depth:", gs_dt.best_params_['max_depth'])
print("CV mean accuracy:", round(dt_cv_score, 4))

# 5️⃣ Random Forest - GridSearch pe max_depth și n_estimators
rf = RandomForestClassifier(random_state=42, n_jobs=-1)
param_grid_rf = {
    'n_estimators': [50, 100],
    'max_depth': [None, 3, 5, 10]
}

gs_rf = GridSearchCV(rf, param_grid_rf, cv=cv_strategy, scoring='accuracy', n_jobs=-1)
gs_rf.fit(X, y)

best_rf = gs_rf.best_estimator_
rf_cv_score = gs_rf.best_score_

print("\n✅ Random Forest")
print("Best params:", gs_rf.best_params_)
print("CV mean accuracy:", round(rf_cv_score, 4))

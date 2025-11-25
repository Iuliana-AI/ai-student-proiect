# grid_search_student_cv.py
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, accuracy_score

# 1️⃣ Încarcă datele tale reale
df = pd.read_csv("student.csv")

# 2️⃣ Definește X și y
X = df[["Nota", "Timp_de_studiu"]]
y = df["Promovat"]

# 3️⃣ Decision Tree - GridSearch pe max_depth cu CV
dt = DecisionTreeClassifier(random_state=42)
param_grid_dt = {'max_depth': [2, 3, 4, 5, 6, None]}  # poți ajusta

gs_dt = GridSearchCV(dt, param_grid_dt, cv=min(5, len(df)), scoring='accuracy', n_jobs=-1)
gs_dt.fit(X, y)

best_dt = gs_dt.best_estimator_
dt_cv_score = gs_dt.best_score_

print("✅ Decision Tree - Best max_depth:", gs_dt.best_params_['max_depth'])
print("✅ Decision Tree - CV mean accuracy:", round(dt_cv_score, 4))

# 4️⃣ Random Forest - GridSearch pe max_depth și n_estimators cu CV
rf = RandomForestClassifier(random_state=42, n_jobs=-1)
param_grid_rf = {
    'n_estimators': [50, 100],
    'max_depth': [None, 3, 5, 10]
}

gs_rf = GridSearchCV(rf, param_grid_rf, cv=min(5, len(df)), scoring='accuracy', n_jobs=-1)
gs_rf.fit(X, y)

best_rf = gs_rf.best_estimator_
rf_cv_score = gs_rf.best_score_

print("✅ Random Forest - Best params:", gs_rf.best_params_)
print("✅ Random Forest - CV mean accuracy:", round(rf_cv_score, 4))

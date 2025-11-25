import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold

# Incarcam CSV-ul
df = pd.read_csv("student.csv")

X = df[["Nota", "Timp_de_studiu"]]
y = df["Promovat"]

# Determinam cate folduri putem folosi
min_class_count = min(y.value_counts())
n_splits = min(5, min_class_count)

print(f"Folosing {n_splits} fold-uri (cea mai mica clasa are {min_class_count} exemple)")

cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

# Decision Tree GridSearch
dt = DecisionTreeClassifier(random_state=42)
param_grid_dt = {'max_depth': [2, 3, 4, 5, 6, None]}

gs_dt = GridSearchCV(dt, param_grid_dt, scoring='accuracy', cv=cv)
gs_dt.fit(X, y)

print("\n=== DECISION TREE ===")
print("Best max_depth:", gs_dt.best_params_)
print("CV accuracy:", round(gs_dt.best_score_, 4))

# Random Forest GridSearch
rf = RandomForestClassifier(random_state=42)
param_grid_rf = {
    'n_estimators': [50, 100],
    'max_depth': [None, 3, 5, 10]
}

gs_rf = GridSearchCV(rf, param_grid_rf, scoring='accuracy', cv=cv)
gs_rf.fit(X, y)

print("\n=== RANDOM FOREST ===")
print("Best params:", gs_rf.best_params_)
print("CV accuracy:", round(gs_rf.best_score_, 4))


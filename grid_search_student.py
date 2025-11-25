# grid_search_student.py
import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1️⃣ Încarcă datele tale reale
df = pd.read_csv("student.csv")

# 2️⃣ Definește X și y
X = df[["Nota", "Timp_de_studiu"]]
y = df["Promovat"]

# 3️⃣ Split date în train și test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4️⃣ Decision Tree - GridSearch pe max_depth
dt = DecisionTreeClassifier(random_state=42)
param_grid_dt = {'max_depth': [2, 3, 4, 5, 6, None]}  # poți ajusta
gs_dt = GridSearchCV(dt, param_grid_dt, cv=5, scoring='accuracy', n_jobs=-1)
gs_dt.fit(X_train, y_train)

best_dt = gs_dt.best_estimator_
dt_pred = best_dt.predict(X_test)
print("Decision Tree - Best max_depth:", gs_dt.best_params_['max_depth'])
print("Decision Tree - Test accuracy:", accuracy_score(y_test, dt_pred))

# 5️⃣ Random Forest - GridSearch pe max_depth și n_estimators
rf = RandomForestClassifier(random_state=42, n_jobs=-1)
param_grid_rf = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 3, 5, 10]
}
gs_rf = GridSearchCV(rf, param_grid_rf, cv=5, scoring='accuracy', n_jobs=-1)
gs_rf.fit(X_train, y_train)

best_rf = gs_rf.best_estimator_
rf_pred = best_rf.predict(X_test)
print("Random Forest - Best params:", gs_rf.best_params_)
print("Random Forest - Test accuracy:", accuracy_score(y_test, rf_pred))

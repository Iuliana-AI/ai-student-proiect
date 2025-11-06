import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1️⃣ Citim datele
df = pd.read_csv("student_data.csv")

# 2️⃣ Definim variabilele (input / output)
X = df[["Varsta", "Timp_studiu"]]  # variabile independente
y = df["Nota"]  # variabila dependentă

# 3️⃣ Împărțim datele în antrenare și test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4️⃣ Creăm modelul
model = LinearRegression()

# 5️⃣ Antrenăm modelul
model.fit(X_train, y_train)

# 6️⃣ Facem predicții
y_pred = model.predict(X_test)

# 7️⃣ Evaluăm performanța
mse = mean_squared_error(y_test, y_pred)
print(f"✅ Model antrenat cu succes!")
print(f"🔹 Eroare pătratică medie (MSE): {mse:.2f}")

# 8️⃣ Testăm o predicție nouă
varsta_noua = 21
timp_studiu_nou = 3
nota_prevazuta = model.predict([[varsta_noua, timp_studiu_nou]])
print(
    f"🎯 Predicție: un student de {varsta_noua} ani care învață {timp_studiu_nou} ore/zi ar putea avea nota {nota_prevazuta[0]:.2f}"
)

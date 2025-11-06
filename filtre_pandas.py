import pandas as pd

# Citim fișierul CSV
df = pd.read_csv("student.csv")

# 1️⃣ Filtrăm studenții cu note peste 9
peste_9 = df[df["Nota"] > 9]
print("\nStudenți cu note peste 9:")
print(peste_9)

# 2️⃣ Sortăm după notă (descrescător)
df_sorted = df.sort_values(by="Nota", ascending=False)
print("\nStudenți sortați descrescător după notă:")
print(df_sorted)

# 3️⃣ Salvăm rezultatele într-un fișier nou
peste_9.to_csv("studenti_peste_9.csv", index=False)
print("\n✅ Fișierul 'studenti_peste_9.csv' a fost generat cu succes!")
# 4️⃣ Statistici generale
print("\n=== Statistici generale ===")
print(df.describe())  # Afișează: medie, deviație standard, minim, maxim etc.

# 5️⃣ Media notelor
media_nota = df["Nota"].mean()
print(f"\n📊 Media generală a notelor este: {media_nota:.2f}")

# 6️⃣ Studenți peste media generală
peste_medie = df[df["Nota"] > media_nota]
print("\n🎯 Studenți peste media generală:")
print(peste_medie)

# Salvăm rezultatul într-un fișier nou
peste_medie.to_csv("studenti_peste_medie.csv", index=False)
print("\n✅ Fișierul 'studenti_peste_medie.csv' a fost generat!")

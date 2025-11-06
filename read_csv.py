import pandas as pd  # importăm biblioteca pandas

# 1️⃣ Citim fișierul CSV
df = pd.read_csv("student.csv")

# Număr total studenți
total_students = len(df)

# Media notelor
media_note = df["Nota"].mean()

# Vârsta medie
varsta_medie = df["Varsta"].mean()

# Studenți cu nota peste 8
students_above_8 = df[df["Nota"] > 8]

# Afișăm raportul
print("\n=== Raport final studenți ===")
print(f"Număr total studenți: {total_students}")
print(f"Media notelor: {media_note:.2f}")
print(f"Vârsta medie: {varsta_medie:.1f} ani")
print("\nStudenți cu nota peste 8:")
print(students_above_8)


# 2️⃣ Afișăm primele rânduri din fișier
print("=== Datele din fișier ===")
print(df)

# 3️⃣ Afișăm media notelor
media_note = df["Nota"].mean()
print(f"\nMedia notelor este: {media_note:.2f}")

# 4️⃣ Afișăm vârsta medie
varsta_medie = df["Varsta"].mean()
print(f"Vârsta medie este: {varsta_medie:.1f} ani")

# 5️⃣ Afișăm doar studenții cu nota > 8
print("\n=== Studenți cu nota peste 8 ===")
print(df[df["Nota"] > 8])

# Filtrăm studenții cu nota peste 8
students_above_8 = df[df["Nota"] > 8]

print("\n=== Studenți cu nota peste 8 ===")
print(students_above_8)

# Media notelor
media_note = df["Nota"].mean()
print(f"\nMedia notelor este: {media_note:.2f}")

# Vârsta medie
varsta_medie = df["Varsta"].mean()
print(f"Vârsta medie este: {varsta_medie:.1f} ani")

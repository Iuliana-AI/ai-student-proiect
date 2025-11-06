import pandas as pd

# 1️⃣ Citim datele
df = pd.read_csv("student.csv")

print("\n=== Datele originale ===")
print(df)

# 2️⃣ Pivot table simplu: media notelor pe vârstă
pivot1 = df.pivot_table(index="Varsta", values="Nota", aggfunc="mean")

print("\n=== Media notelor pe vârstă ===")
print(pivot1)

# 3️⃣ Pivot table cu mai multe funcții: media și numărul de studenți
pivot2 = df.pivot_table(index="Varsta", values="Nota", aggfunc=["mean", "count"])

print("\n=== Media și numărul de studenți pe vârstă ===")
print(pivot2)

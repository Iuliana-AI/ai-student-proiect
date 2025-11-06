import pandas as pd
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

# === Citire fișier CSV ===
csv_file = input("Introdu numele fișierului CSV (ex: student.csv): ")

try:
    df = pd.read_csv(csv_file)
    print("\n✅ Fișierul a fost citit cu succes!\n")
except FileNotFoundError:
    print("❌ Eroare: fișierul specificat nu a fost găsit.")
    exit()

# === Prelucrare date ===
numar_randuri = len(df)
media = df.mean(numeric_only=True)
peste_medie = df[df["Nota"] > media["Nota"]]

# === Creare raport text ===
print("=== RAPORT STATISTIC ===")
print(f"Număr total de rânduri: {numar_randuri}")
print("\n📊 Media coloanelor numerice:")
print(media)
print("\n🎯 Studenți cu note peste medie:")
print(peste_medie)

# === Salvare CSV raport ===
raport_csv = pd.DataFrame(
    {
        "Numar randuri": [numar_randuri],
        "Media varsta": [media["Varsta"]],
        "Media nota": [media["Nota"]],
    }
)
raport_csv.to_csv("raport.csv", index=False)
print("\n💾 Raportul a fost salvat și în 'raport.csv'.")

# === Creare fișier PDF ===
pdf_file = "raport.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Titlu și dată
titlu = Paragraph("<b>Raport Statistic Studenți</b>", styles["Title"])
data = Paragraph(
    f"Generat la: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}", styles["Normal"]
)
elements.extend([titlu, data, Spacer(1, 12)])

# Secțiune: statistici generale
elements.append(Paragraph("<b>Statistici generale</b>", styles["Heading2"]))
table_data = [
    ["Număr rânduri", numar_randuri],
    ["Media vârstă", round(media["Varsta"], 2)],
    ["Media notă", round(media["Nota"], 2)],
]
table = Table(table_data)
table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ]
    )
)
elements.append(table)
elements.append(Spacer(1, 20))

# Secțiune: studenți peste medie
elements.append(Paragraph("<b>Studenți cu note peste medie</b>", styles["Heading2"]))
if peste_medie.empty:
    elements.append(
        Paragraph("Niciun student nu are notă peste medie.", styles["Normal"])
    )
else:
    t_data = [peste_medie.columns.to_list()] + peste_medie.values.tolist()
    t = Table(t_data)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ]
        )
    )
    elements.append(t)

# Salvare PDF
doc.build(elements)
print(f"\n📄 Raportul PDF a fost generat cu succes: {pdf_file}")

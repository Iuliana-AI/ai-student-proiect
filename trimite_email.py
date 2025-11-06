import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# === Setări email ===
from_email = "adresa_ta@gmail.com"
to_email = "destinatar@gmail.com"
subject = "Raport complet studenți"
body = "Salut! Atașat găsești raportul complet generat automat."

# === Alegem fișierul PDF de trimis ===
# Folosește ultimul raport generat
folder = os.getcwd()
pdf_files = [f for f in os.listdir(folder) if f.endswith(".pdf")]
pdf_files.sort(reverse=True)
pdf_file = pdf_files[0]  # cel mai recent PDF

# === Creare mesaj email ===
msg = MIMEMultipart()
msg["From"] = from_email
msg["To"] = to_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Atașare PDF
with open(pdf_file, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename= {pdf_file}")
msg.attach(part)

# === Trimitere email ===
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(from_email, "PAROLA_DE_APLICATIE")  # parola aplicație Gmail
text = msg.as_string()
server.sendmail(from_email, to_email, text)
server.quit()

print(f"✅ Email trimis cu {pdf_file}")

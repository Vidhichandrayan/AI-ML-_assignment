import pandas as pd
import sqlite3

df = pd.read_csv("names_emails.csv")

conn = sqlite3.connect("names_emails.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")

for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (row["Name"], row["Email"])
    )

conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("\nUsers stored in database:\n")
for row in rows:
    print(row)

conn.close()

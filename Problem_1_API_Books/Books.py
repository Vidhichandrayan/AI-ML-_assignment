import requests
import sqlite3

url = "https://www.googleapis.com/books/v1/volumes?q=data+science"
response = requests.get(url)
data = response.json()

connection = sqlite3.connect("books.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    published_year TEXT
)
""")

for item in data["items"][:5]:
    volume = item["volumeInfo"]
    title = volume.get("title", "N/A")
    authors = volume.get("authors", ["N/A"])
    published_year = volume.get("publishedDate", "N/A")[:4]

    cursor.execute("""
    INSERT INTO books (title, author, published_year)
    VALUES (?, ?, ?)
    """, (title, ", ".join(authors), published_year))

connection.commit()

print("\nBooks stored in database:\n")
print("-" * 90)
print(f"{'Title':40} | {'Author':30} | {'Year'}")
print("-" * 90)

cursor.execute("SELECT title, author, published_year FROM books")
rows = cursor.fetchall()

for title, author, year in rows:
    print(f"{title[:40]:40} | {author[:30]:30} | {year}")

print("-" * 90)
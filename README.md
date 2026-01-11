# AccuKnox AI/ML Assignment 
This repository contains my submission for the AccuKnox AI/ML Trainee assignment. It demonstrates working with REST APIs, CSV files, SQLite databases, and data visualization. ---

 ## Task 1 – 
  Books API to SQLite books.py fetches book data from the Google Books REST API, stores the title, author, and published year into a SQLite database, and displays the stored records. Run:
bash
python books.py
## Task 2 – 
Student Scores API and Visualization

A Kaggle dataset (Students Performance in Exams) is exposed as a REST API using FastAPI (student_api.py).
Student_Scores.py fetches this data from the API, calculates the average score, and displays a bar chart showing student performance.

Run:
uvicorn student_api:app --reload
python Student_Scores.py

## Task 3 – 
CSV to SQLite
csv_data_db.py reads user names and email addresses from a CSV file and inserts them into a SQLite database, then displays the stored records.

Run:
python csv_data_db.py

Setup
Create and activate virtual environment:
python -m venv venv
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt
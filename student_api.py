from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("studentsPerformance.csv")

@app.get("/scores")
def get_scores():
    df["average_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)

    
    return df[["gender", "average_score"]].to_dict(orient="records")

from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")


@app.get("/")
def root():
    return {"status": "API running"}


@app.get("/versions")
def get_versions():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("SELECT model_name, version, deployed_at FROM versions;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return {"versions": rows}
    except Exception as e:
        return {"error": str(e)}

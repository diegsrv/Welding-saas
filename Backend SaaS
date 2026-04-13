from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import uuid

app = FastAPI()

# =========================
# DB SIMPLE
# =========================

conn = sqlite3.connect("welding.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
id TEXT,
email TEXT,
password TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS projects (
id TEXT,
user_id TEXT,
data TEXT
)
""")

conn.commit()

# =========================
# MODELS
# =========================

class User(BaseModel):
    email: str
    password: str

class Project(BaseModel):
    user_id: str
    data: str

# =========================
# AUTH
# =========================

@app.post("/register")
def register(user: User):
    uid = str(uuid.uuid4())
    c.execute("INSERT INTO users VALUES (?, ?, ?)", (uid, user.email, user.password))
    conn.commit()
    return {"user_id": uid}

@app.post("/login")
def login(user: User):
    res = c.execute("SELECT id FROM users WHERE email=? AND password=?",
                    (user.email, user.password)).fetchone()

    if res:
        return {"user_id": res[0]}
    return {"error": "invalid credentials"}

# =========================
# PROJECT SAVE
# =========================

@app.post("/save_project")
def save_project(p: Project):
    pid = str(uuid.uuid4())
    c.execute("INSERT INTO projects VALUES (?, ?, ?)", (pid, p.user_id, p.data))
    conn.commit()
    return {"project_id": pid}

@app.get("/projects/{user_id}")
def get_projects(user_id: str):
    res = c.execute("SELECT data FROM projects WHERE user_id=?", (user_id,)).fetchall()
    return {"projects": res}

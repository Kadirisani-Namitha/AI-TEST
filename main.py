import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

# SQLite setup
conn = sqlite3.connect('memory.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prompt TEXT NOT NULL
)
''')
conn.commit()

app = FastAPI()

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
def read_root():
    base_dir = os.path.dirname(os.path.abspath(_file_))  # backend/
    index_path = os.path.abspath(os.path.join(base_dir, "..", "frontend", "index.html"))

    if not os.path.exists(index_path):
        raise RuntimeError(f"File not found: {index_path}")

    return FileResponse(index_path)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

OPENFABRIC_API_URL = "https://api.openfabric.ai/v1/apps"
TEXT_TO_IMAGE_APP_ID = "f0997a01-d6d3-a5fe-53d8-561300318557"
IMAGE_TO_3D_APP_ID = "69543f29-4d41-4afc-7f29-3d51591f11eb"

@app.post("/process")
async def process_prompt(prompt_req: PromptRequest):
    prompt = prompt_req.prompt

    interpretation = f"Interpreted prompt: {prompt}"
    image_url = "https://images.unsplash.com/photo-1651343726891-85961742da51?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Q3JlYXRlJTIwYSUyMHJvYm90JTIwd2l0aCUyMHdpbmdzfGVufDB8fDB8fHww"
    model_3d_url = "https://example.com/fake-model.glb"

    cursor.execute("INSERT INTO memory (prompt) VALUES (?)", (prompt,))
    conn.commit()

    cursor.execute("SELECT prompt FROM memory")
    memory = [row[0] for row in cursor.fetchall()]

    return {
        "original_prompt": prompt,
        "text_interpretation": interpretation,
        "image_url": image_url,
        "3d_model": model_3d_url,
        "memory": memory
    }
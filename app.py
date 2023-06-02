from fastapi import FastAPI
import solara.server.fastapi
from dotenv import load_dotenv
import os

load_dotenv()  # Memuat variabel lingkungan dari file .env

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.mount("/solara/", app=solara.server.fastapi.app)

# if __name__ == "__main__":
    # solara_app = os.getenv("SOLARA_APP")
    # command = f"SOLARA_APP=sol.py uvicorn app:app"
    # os.system(command)

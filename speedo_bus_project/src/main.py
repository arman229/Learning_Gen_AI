from src.openai_api_fun import run_conversation

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(prompt: str) -> str:
    return run_conversation(prompt)

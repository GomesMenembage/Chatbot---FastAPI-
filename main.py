from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as gemini

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Pergunta(BaseModel):
    prompt: str

gemini.configure(api_key='AIzaSyBSvCe6OXLOMlz8pOwpK4R-q8YAP9piZeY')

@app.post("/bot/")
async def chatbot(pergunta: Pergunta):
    modelo = gemini.GenerativeModel("gemini-1.5-flash")
    response = modelo.generate_content(pergunta.prompt)

    return {"resposta": response.text}

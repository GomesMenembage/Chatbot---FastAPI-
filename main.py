from fastapi import FastAPI 
from pydantic import BaseModel 
import google.generativeai as gemini

app = FastAPI()

class Pergunta(BaseModel):
    prompt : str
    
gemini.configure(api_key='AIzaSyBSvCe6OXLOMlz8pOwpK4R-q8YAP9piZeY')
@app.post("/bot/")
async def chatbot(pergunta: Pergunta):
    modelo = gemini.GenerativeModel("gemini-1.5-flash")
    response = modelo.generate_content(pergunta.prompt)
    
    return {"resposta": response.text}
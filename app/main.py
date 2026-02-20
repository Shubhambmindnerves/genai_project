from fastapi import FastAPI

app = FastAPI()

# Placeholder for chat router

@app.get("/chat")
async def read_chat():
    return "Chat endpoint"

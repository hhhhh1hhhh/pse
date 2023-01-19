from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login")
async def login(username: str = Form(default={})):
    print(username)
    return {"username": username}

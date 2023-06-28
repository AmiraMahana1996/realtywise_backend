from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
print('amira')
from router import user
from auth.auth import router

app = FastAPI()
origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins='http://localhost:3000',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router, tags=['Auth'], prefix='/api/auth')
app.include_router(router, tags=['Users'], prefix='/api/users')


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}


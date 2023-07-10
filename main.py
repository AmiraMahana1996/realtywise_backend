from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
print('amira')
from routers import property, user

from authentication import auth

app = FastAPI()
origins = [
    settings.CLIENT_ORIGIN,
]


app.add_middleware(
    CORSMiddleware,
    allow_origins='http://localhost:4200',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(property.router, tags=['Properties'], prefix='/api/properties')
app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')

@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}


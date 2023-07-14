from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings

from routers import property, user, TFIDF, connection

from authentication import auth

app = FastAPI()
origins = [
    settings.CLIENT_ORIGIN,
]

origins = [

    'http://localhost:4200',
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(property.router, tags=[
                   'Properties'], prefix='/api/properties')
app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(TFIDF.router, tags=['TFIDF'], prefix='/api/tfidf')
app.include_router(connection.router, tags=[
                   'Connect'], prefix='/api/connection')


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}

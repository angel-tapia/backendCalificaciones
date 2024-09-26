from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import routes
import uvicorn


app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",  # React app running on localhost:3000
    "https://cambio-calificaciones.vercel.app",  # Production app
    "https://angel-tapia.github.io/cambio-calificaciones" # Github pages
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

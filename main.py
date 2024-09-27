from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import routes
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

app.include_router(routes.app)

@app.get("/")
def read_root():
    return "Healthy!"


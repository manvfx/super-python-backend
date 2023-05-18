from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.auth import authRoute
from app.routes.user import userRoute

app = FastAPI(
    title="Super Backend",
    version="1.0.0",
)

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/", tags=["Root"])
async def read_root():
    return {
        "message": "Welcome to this app!",
    }

app.include_router(authRoute, prefix='/api/v1',tags = ['Auth'])
app.include_router(userRoute, prefix='/api/v1',tags = ['Users'])
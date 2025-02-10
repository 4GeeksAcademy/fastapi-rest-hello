"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from .utils import APIException, generate_sitemap
from .admin import setup_admin
from .models import Base, User

app = FastAPI()

# # Database configuration
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db").replace("postgres://", "postgresql://")

if "sqlite" in SQLALCHEMY_DATABASE_URL:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware for handling exceptions
@app.middleware("http")
async def add_process_time_header(request, call_next):
    try:
        response = await call_next(request)
    except APIException as e:
        return JSONResponse(status_code=e.status_code, content=e.to_dict())
    return response

# Setup admin
@app.on_event("startup")
async def on_startup():
    await setup_admin(app)

# Generate sitemap with all your endpoints
@app.get("/")
def sitemap():
    return generate_sitemap(app)

@app.get("/user")
def handle_hello():
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }
    return JSONResponse(content=response_body)

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    import uvicorn
    PORT = int(os.environ.get('PORT', 3000))
    uvicorn.run(app, host='0.0.0.0', port=PORT)
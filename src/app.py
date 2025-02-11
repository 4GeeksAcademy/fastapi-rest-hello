"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles
from sqladmin import Admin
from fastapi.responses import FileResponse
from .utils import APIException, generate_sitemap
from .admin import register_admin_views
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

# setup the admin interface
admin = Admin(app, engine)
register_admin_views(admin)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Generate the sitemap
@app.get("/sitemap")
async def sitemap():
    # return a list of all the routes in the app
    return JSONResponse(content=generate_sitemap(app))
    

# Serve the index file
@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

@app.get("/user")
def handle_hello():
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }
    return JSONResponse(content=response_body, status_code=200)

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    import uvicorn
    PORT = int(os.environ.get('PORT', 3000))
    uvicorn.run(app, host='0.0.0.0', port=PORT)
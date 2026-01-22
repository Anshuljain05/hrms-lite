import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()

# Import models to register them with SQLAlchemy
import models
from database import Base, engine
from routes.employees import router as employee_router
from routes.attendance import router as attendance_router

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="HRMS Lite API",
    description="A lightweight HR Management System API",
    version="1.0.0"
)

# Production CORS settings
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(employee_router)
app.include_router(attendance_router)


@app.get("/")
def read_root():
    """Root endpoint - API is running"""
    return {
        "message": "HRMS Lite API is running",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

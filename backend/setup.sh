#!/bin/bash
# HRMS Lite - Backend Setup Script for Mac/Linux

echo ""
echo "========================================"
echo "HRMS Lite - Backend Setup"
echo "========================================"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run server
echo ""
echo "========================================"
echo "Setup complete! Starting server..."
echo "========================================"
echo ""
echo "Backend will run at: http://localhost:8000"
echo "API Docs at: http://localhost:8000/docs"
echo ""

python -m uvicorn main:app --host 0.0.0.0 --port 8000

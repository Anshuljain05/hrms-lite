#!/bin/bash
# HRMS Lite - Frontend Setup Script for Mac/Linux

echo ""
echo "========================================"
echo "HRMS Lite - Frontend Setup"
echo "========================================"
echo ""

# Install npm dependencies
echo "Installing npm dependencies..."
npm install

# Run development server
echo ""
echo "========================================"
echo "Setup complete! Starting server..."
echo "========================================"
echo ""
echo "Frontend will run at: http://localhost:5173"
echo ""

npm run dev

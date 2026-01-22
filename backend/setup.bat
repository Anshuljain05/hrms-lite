@echo off
REM HRMS Lite - Backend Setup Script for Windows

echo.
echo ===============================================
echo HRMS Lite - Backend Setup
echo ===============================================
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Create database and run
echo.
echo ===============================================
echo Setup complete! Starting server...
echo ===============================================
echo.
echo Backend will run at: http://localhost:8000
echo API Docs at: http://localhost:8000/docs
echo.

python -m uvicorn main:app --host 0.0.0.0 --port 8000

pause

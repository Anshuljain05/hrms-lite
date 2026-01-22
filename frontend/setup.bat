@echo off
REM HRMS Lite - Frontend Setup Script for Windows

echo.
echo ===============================================
echo HRMS Lite - Frontend Setup
echo ===============================================
echo.

REM Install npm dependencies
echo Installing npm dependencies...
npm install

REM Run development server
echo.
echo ===============================================
echo Setup complete! Starting server...
echo ===============================================
echo.
echo Frontend will run at: http://localhost:5173
echo.

npm run dev

pause

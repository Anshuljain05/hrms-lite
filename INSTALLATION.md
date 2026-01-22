# HRMS Lite - Installation & Setup Guide

## Prerequisites

Before you begin, ensure you have the following installed:

### Required Software
- **Python 3.10+** ([Download](https://www.python.org/downloads/))
- **Node.js 16+** ([Download](https://nodejs.org/))
- **npm** (comes with Node.js)
- **Git** (optional, [Download](https://git-scm.com/))

### Verify Installation
```bash
# Check Python
python --version

# Check Node.js
node --version

# Check npm
npm --version
```

## Installation Steps

### Method 1: Using Setup Scripts (Recommended for Windows)

#### Backend Setup (Windows)
```bash
cd backend
setup.bat
```

#### Frontend Setup (Windows)
```bash
cd frontend
setup.bat
```

---

### Method 2: Using Setup Scripts (Mac/Linux)

#### Backend Setup (Mac/Linux)
```bash
cd backend
chmod +x setup.sh
./setup.sh
```

#### Frontend Setup (Mac/Linux)
```bash
cd frontend
chmod +x setup.sh
./setup.sh
```

---

### Method 3: Manual Setup

#### Step 1: Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create and activate virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Create and activate virtual environment (Mac/Linux)
python -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Run the backend server
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

**Expected Output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

#### Step 2: Frontend Setup (Open New Terminal)

```bash
# Navigate to frontend directory
cd frontend

# Install npm dependencies
npm install

# Run the development server
npm run dev
```

**Expected Output:**
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  press h to show help
```

---

## Verify Installation

### Backend Verification
Open your browser or use curl:
```bash
curl http://localhost:8000/health
# Expected response: {"status":"healthy"}
```

Visit API docs:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Frontend Verification
Open your browser:
- **Frontend**: http://localhost:5173

You should see the HRMS Lite application with:
- Employee Management tab
- Attendance tab
- Clean, professional UI

---

## Quick Test After Installation

### Test Employee Management
1. Open http://localhost:5173
2. Go to **Employee Management** tab
3. Click **Add New Employee**
4. Fill in the form:
   ```
   Employee ID: EMP001
   Full Name: John Doe
   Email: john@example.com
   Department: Engineering
   ```
5. Click **Add Employee**
6. Should see success message and employee appears in list

### Test Attendance Management
1. Go to **Attendance** tab
2. Select the employee you just created
3. Select today's date
4. Select "Present"
5. Click **Mark Attendance**
6. Should see success message and record appears in table

---

## Troubleshooting

### Python Not Found
```
Error: 'python' is not recognized
```
**Solution**: 
- Reinstall Python and ensure "Add Python to PATH" is checked
- Use `python3` instead of `python` on Mac/Linux

### Port Already in Use
```
Error: Address already in use (port 8000)
```
**Solution**:
```bash
# Find process using port 8000
# Windows: netstat -ano | findstr :8000
# Mac/Linux: lsof -i :8000

# Kill the process or use a different port
python -m uvicorn main:app --port 8001
```

### npm Install Fails
```
Error: npm ERR! ERESOLVE unable to resolve dependency tree
```
**Solution**:
```bash
npm install --legacy-peer-deps
```

### Frontend Can't Connect to Backend
**Solution**:
1. Ensure backend is running on http://localhost:8000
2. Check `.env` file in frontend directory has correct API URL
3. Check browser console for CORS errors
4. Verify backend CORS is enabled (it is by default)

### Module Not Found (Python)
```
ModuleNotFoundError: No module named 'fastapi'
```
**Solution**:
```bash
# Ensure virtual environment is activated
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Virtual Environment Issues
```bash
# Deactivate and remove venv
deactivate
rm -rf venv  # Mac/Linux
rmdir /s venv  # Windows

# Create fresh virtual environment
python -m venv venv
```

---

## Environment Configuration

### Backend Configuration
**File**: `backend/database.py`

Change database if needed:
```python
# SQLite (default)
DATABASE_URL = "sqlite:///./hrms.db"

# PostgreSQL example (not tested)
# DATABASE_URL = "postgresql://user:password@localhost/hrms_lite"
```

### Frontend Configuration
**File**: `frontend/.env`

Change API URL if backend is running elsewhere:
```
VITE_API_URL=http://localhost:8000
```

For production:
```
VITE_API_URL=https://api.your-domain.com
```

---

## File Locations

### Important Files
- Backend database: `backend/hrms.db` (auto-created)
- Environment file (frontend): `frontend/.env`
- Python dependencies: `backend/requirements.txt`
- Node dependencies: `frontend/package.json`

### Logs
- Backend logs: Console output (unless redirected)
- Frontend build errors: Console output

---

## Running in Production

### Backend Production Deployment
```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

### Frontend Production Build
```bash
# Create optimized build
npm run build

# Build output in `dist/` folder
# Deploy `dist/` folder to static hosting (Netlify, Vercel, AWS S3, etc.)
```

---

## Database Reset

### Reset SQLite Database
```bash
# Delete the database file
rm backend/hrms.db  # Mac/Linux
del backend\hrms.db  # Windows

# Restart the backend
# New database will be created automatically
```

---

## Additional Help

### Check Port Availability
```bash
# Windows
netstat -ano | findstr :PORT_NUMBER

# Mac/Linux
lsof -i :PORT_NUMBER
```

### View Running Processes
```bash
# Find Python processes
# Windows: tasklist | findstr python
# Mac/Linux: ps aux | grep python
```

### Clear npm Cache
```bash
npm cache clean --force
```

### Update Dependencies
```bash
# Backend
pip install --upgrade -r requirements.txt

# Frontend
npm update
```

---

## Still Having Issues?

1. Check that all prerequisites are installed
2. Ensure both frontend and backend are running in separate terminals
3. Check console for error messages
4. Verify network connectivity to localhost
5. Try a fresh installation (backup `.env` files first)
6. Check if ports 8000 and 5173 are available

---

**For more information, see:**
- [Main README](./README.md)
- [Backend README](./backend/README.md)
- [Frontend README](./frontend/README.md)

# HRMS Lite - Full-Stack HR Management System

A lightweight web-based HR Management System for managing employees and tracking daily attendance. Built with React.js frontend and Python FastAPI backend.

## 🎯 Project Overview

HRMS Lite is a minimal HR management system designed for a single admin user to:
- **Manage Employees**: Add, view, and delete employee records
- **Track Attendance**: Mark and view daily attendance for employees

## 🧱 Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | React.js 18 (Vite) |
| **Backend** | Python 3.10, FastAPI |
| **Database** | SQLite |
| **API** | REST API (JSON) |
| **Styling** | CSS3 |

## 📋 Features Implemented

### Employee Management ✅
- ✓ Add new employees with validation
- ✓ View list of all employees
- ✓ Delete employees (with confirmation)
- ✓ Unique employee ID enforcement
- ✓ Email validation
- ✓ Required field validation

### Attendance Management ✅
- ✓ Mark attendance for employees (Present/Absent)
- ✓ View attendance records per employee
- ✓ Date-based attendance tracking
- ✓ Duplicate entry prevention (unique employee + date)
- ✓ Employee existence validation

### Backend Features ✅
- ✓ RESTful API endpoints
- ✓ Proper HTTP status codes (200, 201, 400, 404, 409)
- ✓ Comprehensive error messages
- ✓ Data validation with Pydantic
- ✓ CORS enabled for frontend integration
- ✓ Database persistence with SQLAlchemy ORM

### Frontend Features ✅
- ✓ Responsive UI design
- ✓ Loading states
- ✓ Error handling and messages
- ✓ Empty state handling
- ✓ Form validation
- ✓ Clean navigation between sections
- ✓ Professional styling

## 📁 Project Structure

```
Ethara AI/
├── backend/
│   ├── main.py                 # FastAPI application entry point
│   ├── database.py             # SQLAlchemy database configuration
│   ├── requirements.txt         # Python dependencies
│   ├── models/
│   │   ├── employee.py         # Employee ORM model
│   │   └── attendance.py        # Attendance ORM model
│   ├── schemas/
│   │   ├── employee.py         # Employee validation schemas
│   │   └── attendance.py        # Attendance validation schemas
│   ├── routes/
│   │   ├── employees.py        # Employee API endpoints
│   │   └── attendance.py        # Attendance API endpoints
│   ├── hrms.db                 # SQLite database (auto-created)
│   └── README.md               # Backend documentation
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx             # Main app component
│   │   ├── App.css             # Global styles
│   │   ├── main.jsx            # Entry point
│   │   ├── pages/
│   │   │   ├── Employees.jsx   # Employee management page
│   │   │   └── Attendance.jsx   # Attendance tracking page
│   │   └── components/         # Reusable components (future)
│   ├── index.html              # HTML template
│   ├── vite.config.js          # Vite configuration
│   ├── package.json            # npm dependencies
│   ├── .env                    # Environment variables
│   ├── .gitignore              # Git ignore rules
│   └── README.md               # Frontend documentation
│
└── README.md                   # This file
```

## 🚀 Quick Start

### Prerequisites
- Node.js 16+ and npm
- Python 3.10+
- SQLite (included with Python)

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Create virtual environment (Mac/Linux)
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

Backend runs at: `http://localhost:8000`
API Docs: `http://localhost:8000/docs`

### Frontend Setup

```bash
# Navigate to frontend directory (new terminal)
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend runs at: `http://localhost:5173`

## 🔌 API Endpoints

### Employees
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/employees/` | Create new employee |
| `GET` | `/api/employees/` | Get all employees |
| `GET` | `/api/employees/{id}` | Get specific employee |
| `DELETE` | `/api/employees/{id}` | Delete employee |

### Attendance
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/attendance/` | Mark attendance |
| `GET` | `/api/attendance/` | Get all records |
| `GET` | `/api/attendance/employee/{id}` | Get records for employee |

## 📊 Data Models

### Employee
```
{
  "employeeId": "string (unique, required)",
  "fullName": "string (required)",
  "email": "string (valid email, unique, required)",
  "department": "string (required)"
}
```

### Attendance
```
{
  "id": "string (UUID, unique)",
  "employeeId": "string (FK to Employee)",
  "date": "date (YYYY-MM-DD)",
  "status": "Present | Absent"
}
```

## ✅ Validation Rules

### Employee Registration
- ✓ `employeeId` must be unique
- ✓ `email` must be valid and unique
- ✓ All fields are required
- ✓ Cannot create duplicate employee IDs or emails
- Returns `409 Conflict` for duplicates

### Attendance Marking
- ✓ Employee must exist
- ✓ Status must be "Present" or "Absent"
- ✓ Cannot mark same employee twice for same date
- ✓ All fields are required
- Returns `409 Conflict` for duplicate dates
- Returns `404 Not Found` if employee doesn't exist

## 🛠️ HTTP Status Codes

| Code | Meaning | Use Case |
|------|---------|----------|
| `200` | OK | Successful GET |
| `201` | Created | Successful POST |
| `204` | No Content | Successful DELETE |
| `400` | Bad Request | Validation error |
| `404` | Not Found | Resource not found |
| `409` | Conflict | Duplicate entry/uniqueness violation |

## 🚫 What's NOT Included (By Design)

This is HRMS **Lite** - not HRMS Pro. Intentionally excluded:
- ❌ User authentication & roles
- ❌ Payroll management
- ❌ Leave management
- ❌ Performance reviews
- ❌ Multiple departments with permissions
- ❌ Complex reporting
- ❌ Data exports
- ❌ Advanced filtering beyond date

## 📝 Usage Example

### Adding an Employee via API
```bash
curl -X POST "http://localhost:8000/api/employees/" \
  -H "Content-Type: application/json" \
  -d '{
    "employeeId": "EMP001",
    "fullName": "John Doe",
    "email": "john@example.com",
    "department": "Engineering"
  }'
```

### Marking Attendance via API
```bash
curl -X POST "http://localhost:8000/api/attendance/" \
  -H "Content-Type: application/json" \
  -d '{
    "employeeId": "EMP001",
    "date": "2026-01-22",
    "status": "Present"
  }'
```

## 🧪 Testing the Application

### Test Employee Flow
1. Go to **Employee Management** tab
2. Click **Add New Employee**
3. Fill in the form with:
   - Employee ID: `EMP001`
   - Full Name: `John Doe`
   - Email: `john@example.com`
   - Department: `Engineering`
4. Click **Add Employee**
5. Verify employee appears in the list
6. Try deleting the employee

### Test Attendance Flow
1. Go to **Attendance** tab
2. Select an employee from dropdown
3. Select today's date
4. Choose "Present" or "Absent"
5. Click **Mark Attendance**
6. Verify record appears in the table below

### Test Error Handling
1. Try adding duplicate employee ID
2. Try invalid email format
3. Try marking attendance twice for same date
4. Observe appropriate error messages

## 🔧 Environment Configuration

### Frontend `.env`
```
VITE_API_URL=http://localhost:8000
```

### Backend Configuration
Modify in `backend/database.py`:
```python
DATABASE_URL = "sqlite:///./hrms.db"  # SQLite
```

## 📦 Dependencies

### Backend (`requirements.txt`)
- `fastapi==0.104.1` - Web framework
- `uvicorn==0.24.0` - ASGI server
- `sqlalchemy==2.0.23` - ORM
- `pydantic==1.10.13` - Data validation
- `python-multipart==0.0.6` - Form parsing

### Frontend (`package.json`)
- `react==18.2.0` - UI library
- `react-dom==18.2.0` - DOM rendering
- `vite==5.1.0` - Build tool
- `@vitejs/plugin-react==4.2.1` - React plugin

## 🔍 Database

SQLite database file: `backend/hrms.db`

### Tables
1. **employees**
   - employeeId (PK)
   - fullName
   - email (UNIQUE)
   - department

2. **attendance**
   - id (PK, UUID)
   - employeeId (FK)
   - date
   - status
   - Unique constraint: (employeeId, date)

## ⚠️ Limitations & Assumptions

1. **Single User**: No authentication; assumes single admin access
2. **SQLite**: Suitable for development; use PostgreSQL for production
3. **No Data Export**: Reports are not implemented
4. **No Pagination**: Lists show all records (OK for small datasets)
5. **Date Format**: Uses ISO 8601 (YYYY-MM-DD)
6. **Time Zone**: UTC assumed; no timezone handling
7. **No Bulk Operations**: One-by-one operations only
8. **CORS**: Allows all origins (configure in production)

## 🚀 Production Deployment

### Backend Deployment
```bash
# Using Gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

### Frontend Deployment
```bash
# Build for production
npm run build

# Deploy `dist/` folder to static hosting (Netlify, Vercel, AWS S3, etc.)
```

### Environment Configuration
- Update `VITE_API_URL` to production backend URL
- Use environment variables for sensitive data
- Enable proper CORS on backend
- Use HTTPS in production
- Consider using PostgreSQL instead of SQLite

## 📖 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Vite Documentation](https://vitejs.dev/)

## 📝 Notes

- Database is created automatically on first run
- Backend generates Swagger API documentation at `/docs`
- All timestamps stored in UTC
- Email validation uses Pydantic EmailStr
- Passwords are NOT stored (not implemented per requirements)

## ✨ Future Enhancements (Out of Scope)

- User authentication & authorization
- Payroll calculations
- Leave management system
- Performance reviews
- Advanced reporting & analytics
- Bulk import/export
- Multi-timezone support
- Mobile app version

---

**Project Status**: Complete ✅  
**Last Updated**: January 22, 2026  
**Version**: 1.0.0

# HRMS Lite Frontend

A lightweight React-based frontend for the HRMS Lite HR Management System.

## Setup

### 1. Install dependencies
```bash
npm install
```

### 2. Configure API URL
Edit `.env` file and set the API base URL:
```
VITE_API_URL=http://localhost:8000
```

### 3. Run development server
```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

### 4. Build for production
```bash
npm run build
```

## Features

- Employee Management (Add, View, Delete)
- Attendance Tracking (Mark and View)
- Clean, responsive UI
- Real-time error handling
- Loading states

## Environment Variables

- `VITE_API_URL` - Backend API URL (default: http://localhost:8000)

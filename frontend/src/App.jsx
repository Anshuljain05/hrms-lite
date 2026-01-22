import './App.css'
import { useState } from 'react'
import Employees from './pages/Employees'
import Attendance from './pages/Attendance'

function App() {
  const [currentPage, setCurrentPage] = useState('employees')

  return (
    <div className="app">
      <header className="header">
        <h1>HRMS Lite</h1>
        <p>Lightweight HR Management System</p>
      </header>

      <nav className="navbar">
        <button 
          className={`nav-btn ${currentPage === 'employees' ? 'active' : ''}`}
          onClick={() => setCurrentPage('employees')}
        >
          Employee Management
        </button>
        <button 
          className={`nav-btn ${currentPage === 'attendance' ? 'active' : ''}`}
          onClick={() => setCurrentPage('attendance')}
        >
          Attendance
        </button>
      </nav>

      <main className="main-content">
        {currentPage === 'employees' && <Employees />}
        {currentPage === 'attendance' && <Attendance />}
      </main>
    </div>
  )
}

export default App

import './App.css'
import { useState, useEffect } from 'react'
import Employees from './pages/Employees'
import Attendance from './pages/Attendance'
import Dashboard from './pages/Dashboard'

function App() {
  const [currentPage, setCurrentPage] = useState('employees')
  const [isDarkMode, setIsDarkMode] = useState(() => {
    const saved = localStorage.getItem('theme')
    if (saved) return saved === 'dark'
    return window.matchMedia('(prefers-color-scheme: dark)').matches
  })

  useEffect(() => {
    const theme = isDarkMode ? 'dark' : 'light'
    document.documentElement.setAttribute('data-theme', theme)
    localStorage.setItem('theme', theme)
  }, [isDarkMode])

  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode)
  }

  return (
    <div className="app">
      <header className="header">
        <div className="header-content">
          <div>
            <h1>HRMS Lite</h1>
            <p>Lightweight HR Management System</p>
          </div>
          <button 
            className="theme-toggle" 
            onClick={toggleTheme}
            aria-label={`Switch to ${isDarkMode ? 'light' : 'dark'} theme`}
            title={`${isDarkMode ? 'Light' : 'Dark'} Mode`}
          >
            {isDarkMode ? '🌙 Dark' : '☀️ Light'}
          </button>
        </div>
      </header>

      <nav className="navbar">
        <button 
          className={`nav-btn ${currentPage === 'dashboard' ? 'active' : ''}`}
          onClick={() => setCurrentPage('dashboard')}
        >
          Dashboard
        </button>
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
        {currentPage === 'dashboard' && <Dashboard />}
        {currentPage === 'employees' && <Employees />}
        {currentPage === 'attendance' && <Attendance />}
      </main>
    </div>
  )
}

export default App

import React, { useState, useEffect } from 'react'
import { API_URL } from '../config'

export default function Dashboard() {
  const [dashboard, setDashboard] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetchDashboard()
  }, [])

  const fetchDashboard = async () => {
    setLoading(true)
    setError(null)
    try {
      const response = await fetch(`${API_URL}/api/dashboard/summary`)
      if (!response.ok) throw new Error('Failed to fetch dashboard summary')
      const data = await response.json()
      setDashboard(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  if (loading) return <div className="loading">📊 Loading dashboard...</div>
  if (error) return <div className="error">❌ Error: {error}</div>
  if (!dashboard) return <div className="empty-state">No data available</div>

  return (
    <div className="dashboard-container">
      <h2>📊 Organization Dashboard</h2>
      
      <div className="stats-grid">
        <div className="stat-card primary">
          <div className="stat-label">Total Employees</div>
          <div className="stat-value">{dashboard.total_employees}</div>
          <div className="stat-description">Active employees</div>
        </div>

        <div className="stat-card success">
          <div className="stat-label">Attendance Rate</div>
          <div className="stat-value">{dashboard.attendance_rate}%</div>
          <div className="stat-description">{dashboard.present} present</div>
        </div>

        <div className="stat-card warning">
          <div className="stat-label">Total Records</div>
          <div className="stat-value">{dashboard.total_attendance}</div>
          <div className="stat-description">Attendance entries</div>
        </div>

        <div className="stat-card info">
          <div className="stat-label">Departments</div>
          <div className="stat-value">{dashboard.total_departments}</div>
          <div className="stat-description">Organization units</div>
        </div>
      </div>

      <div className="breakdown-section">
        <h3>📈 Attendance Breakdown</h3>
        <div className="breakdown-cards">
          <div className="breakdown-card present">
            <div className="breakdown-label">Present</div>
            <div className="breakdown-value">{dashboard.present}</div>
          </div>
          <div className="breakdown-card absent">
            <div className="breakdown-label">Absent</div>
            <div className="breakdown-value">{dashboard.absent}</div>
          </div>
        </div>
      </div>

      <div className="department-section">
        <h3>🏢 Employees by Department</h3>
        <div className="department-list">
          {Object.entries(dashboard.employees_by_department).map(([dept, count]) => (
            <div key={dept} className="department-item">
              <span className="dept-name">{dept}</span>
              <span className="dept-count">{count}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

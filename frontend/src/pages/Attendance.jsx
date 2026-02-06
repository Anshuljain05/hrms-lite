import React, { useState, useEffect } from 'react'
import { API_URL } from '../config'

export default function Attendance() {
  const [employees, setEmployees] = useState([])
  const [selectedEmployee, setSelectedEmployee] = useState('')
  const [attendanceRecords, setAttendanceRecords] = useState([])
  const [summary, setSummary] = useState(null)
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState(null)
  const [filterStartDate, setFilterStartDate] = useState('')
  const [filterEndDate, setFilterEndDate] = useState('')
  const [filterApplied, setFilterApplied] = useState(false)
  const [formData, setFormData] = useState({
    employee_id: '',
    date: new Date().toISOString().split('T')[0],
    status: 'Present'
  })

  // Auto-dismiss messages after 3 seconds
  useEffect(() => {
    if (message) {
      const timer = setTimeout(() => setMessage(null), 3000)
      return () => clearTimeout(timer)
    }
  }, [message])

  useEffect(() => {
    fetchEmployees()
  }, [])

  useEffect(() => {
    if (selectedEmployee) {
      fetchAttendanceRecords(selectedEmployee)
      fetchSummary(selectedEmployee)
    }
  }, [selectedEmployee])

  const fetchEmployees = async () => {
    try {
      const response = await fetch(`${API_URL}/api/employees/`)
      if (!response.ok) throw new Error('Failed to fetch employees')
      const data = await response.json()
      setEmployees(data.employees)
    } catch (error) {
      setMessage({ type: 'error', text: error.message })
    }
  }

  const fetchSummary = async (employeeId) => {
    try {
      const response = await fetch(`${API_URL}/api/attendance/employee/${employeeId}/summary`)
      if (!response.ok) throw new Error('Failed to fetch summary')
      const data = await response.json()
      setSummary(data)
    } catch (error) {
      setSummary(null)
    }
  }

  const fetchAttendanceRecords = async (employeeId, startDate = '', endDate = '') => {
    setLoading(true)
    try {
      let url = `${API_URL}/api/attendance/employee/${employeeId}`
      const params = new URLSearchParams()
      if (startDate) params.append('start_date', startDate)
      if (endDate) params.append('end_date', endDate)
      if (params.toString()) url += '?' + params.toString()

      const response = await fetch(url)
      if (!response.ok) throw new Error('Failed to fetch attendance records')
      const data = await response.json()
      setAttendanceRecords(data.records)
    } catch (error) {
      setMessage({ type: 'error', text: error.message })
      setAttendanceRecords([])
    } finally {
      setLoading(false)
    }
  }

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({ ...prev, [name]: value }))
  }

  const handleEmployeeChange = (e) => {
    const employeeId = e.target.value
    setSelectedEmployee(employeeId)
    setFormData(prev => ({ ...prev, employee_id: employeeId }))
    setFilterStartDate('')
    setFilterEndDate('')
    setFilterApplied(false)
  }

  const handleApplyFilter = () => {
    if (selectedEmployee) {
      setFilterApplied(true)
      fetchAttendanceRecords(selectedEmployee, filterStartDate, filterEndDate)
    }
  }

  const handleClearFilter = () => {
    setFilterStartDate('')
    setFilterEndDate('')
    setFilterApplied(false)
    if (selectedEmployee) {
      fetchAttendanceRecords(selectedEmployee, '', '')
    }
  }

  const handleMarkAttendance = async (e) => {
    e.preventDefault()

    if (!formData.employee_id) {
      setMessage({ type: 'error', text: 'Please select an employee' })
      return
    }

    setLoading(true)
    try {
      const response = await fetch(`${API_URL}/api/attendance/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          employee_id: formData.employee_id,
          date: formData.date,
          status: formData.status
        })
      })

      if (!response.ok) {
        const error = await response.json()
        throw new Error(error.detail || 'Failed to mark attendance')
      }

      setMessage({ type: 'success', text: 'Attendance marked successfully!' })
      setFormData({
        employee_id: selectedEmployee,
        date: new Date().toISOString().split('T')[0],
        status: 'Present'
      })
      fetchAttendanceRecords(selectedEmployee, filterStartDate, filterEndDate)
      fetchSummary(selectedEmployee)
    } catch (error) {
      setMessage({ type: 'error', text: error.message })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page">
      <h2 className="section-title">Attendance Management</h2>

      {message && (
        <div 
          role="alert" 
          aria-live="polite" 
          aria-atomic="true"
          className={`message message-${message.type}`}
        >
          {message.text}
        </div>
      )}

      <div className="form-container">
        <h3>Mark Attendance</h3>
        <form onSubmit={handleMarkAttendance}>
          <div className="form-row">
            <div className="form-group">
              <label className="form-label" htmlFor="employeeId">Select Employee</label>
              <select
                id="employeeId"
                name="employeeId"
                className="form-select"
                value={selectedEmployee}
                onChange={handleEmployeeChange}
                required
              >
                <option value="">-- Choose an employee --</option>
                {employees.map(emp => (
                  <option key={emp.employee_id} value={emp.employee_id}>
                    {emp.full_name} ({emp.employee_id})
                  </option>
                ))}
              </select>
            </div>
            <div className="form-group">
              <label className="form-label" htmlFor="date">Date</label>
              <input
                id="date"
                type="date"
                name="date"
                className="form-input"
                value={formData.date}
                onChange={handleInputChange}
                required
              />
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label className="form-label" htmlFor="status">Status</label>
              <select
                id="status"
                name="status"
                className="form-select"
                value={formData.status}
                onChange={handleInputChange}
                required
              >
                <option value="Present">Present</option>
                <option value="Absent">Absent</option>
              </select>
            </div>
          </div>

          <button type="submit" className="btn-primary" disabled={loading}>
            {loading ? <span><span className="spinner" aria-label="Loading"></span>Marking...</span> : 'Mark Attendance'}
          </button>
        </form>
      </div>

      {selectedEmployee && (
        <>
          {/* Summary Card */}
          {summary && (
            <div className="attendance-summary">
              <h3 className="section-title" style={{ marginBottom: '1rem' }}>
                📊 Attendance Summary for {employees.find(e => e.employee_id === selectedEmployee)?.full_name}
              </h3>
              <div className="summary-cards">
                <div className="summary-card present-card">
                  <div className="summary-label">Present</div>
                  <div className="summary-value">{summary.present}</div>
                </div>
                <div className="summary-card absent-card">
                  <div className="summary-label">Absent</div>
                  <div className="summary-value">{summary.absent}</div>
                </div>
                <div className="summary-card total-card">
                  <div className="summary-label">Total Records</div>
                  <div className="summary-value">{summary.total_records}</div>
                </div>
                <div className="summary-card percentage-card">
                  <div className="summary-label">Attendance %</div>
                  <div className="summary-value">{summary.attendance_percentage}%</div>
                </div>
              </div>
            </div>
          )}

          {/* Date Filter */}
          <div className="filter-container">
            <h3 style={{ marginBottom: '1rem' }}>🔍 Filter Records</h3>
            <div className="filter-row">
              <div className="filter-group">
                <label className="form-label">From Date</label>
                <input
                  type="date"
                  className="form-input"
                  value={filterStartDate}
                  onChange={(e) => setFilterStartDate(e.target.value)}
                />
              </div>
              <div className="filter-group">
                <label className="form-label">To Date</label>
                <input
                  type="date"
                  className="form-input"
                  value={filterEndDate}
                  onChange={(e) => setFilterEndDate(e.target.value)}
                />
              </div>
              <div className="filter-buttons">
                <button className="btn-secondary" onClick={handleApplyFilter}>
                  Apply Filter
                </button>
                <button className="btn-outline" onClick={handleClearFilter}>
                  Clear
                </button>
              </div>
            </div>
            {filterApplied && (
              <div className="filter-info">
                ✓ Showing records {filterStartDate && `from ${filterStartDate}`} {filterStartDate && filterEndDate && 'to'} {filterEndDate && `${filterEndDate}`}
              </div>
            )}
          </div>

          <h3 className="section-title" style={{ marginTop: '2rem' }}>
            Attendance Records
          </h3>

          {loading && !attendanceRecords.length ? (
            <div className="loading" role="status" aria-live="polite">
              <span className="spinner" aria-label="Loading attendance records"></span> Loading records...
            </div>
          ) : attendanceRecords.length === 0 ? (
            <div className="empty-state">
              <div className="empty-state-icon">📅</div>
              <p>No attendance records found for this employee.</p>
            </div>
          ) : (
            <div className="table-container">
              <table>
                <thead>
                  <tr>
                    <th>Date</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody>
                  {attendanceRecords.map(record => (
                    <tr key={record.id}>
                      <td>{new Date(record.date).toLocaleDateString()}</td>
                      <td>
                        <span style={{
                          padding: '0.25rem 0.75rem',
                          borderRadius: '4px',
                          backgroundColor: record.status === 'Present' ? '#dcfce7' : '#fee2e2',
                          color: record.status === 'Present' ? '#166534' : '#991b1b',
                          fontWeight: 500
                        }}>
                          {record.status}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </>
      )}
    </div>
  )
}

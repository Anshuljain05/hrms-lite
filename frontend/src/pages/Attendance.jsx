import React, { useState, useEffect } from 'react'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export default function Attendance() {
  const [employees, setEmployees] = useState([])
  const [selectedEmployee, setSelectedEmployee] = useState('')
  const [attendanceRecords, setAttendanceRecords] = useState([])
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState(null)
  const [formData, setFormData] = useState({
    employee_id: '',
    date: new Date().toISOString().split('T')[0],
    status: 'Present'
  })

  useEffect(() => {
    fetchEmployees()
  }, [])

  useEffect(() => {
    if (selectedEmployee) {
      fetchAttendanceRecords(selectedEmployee)
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

  const fetchAttendanceRecords = async (employeeId) => {
    setLoading(true)
    try {
      const response = await fetch(`${API_URL}/api/attendance/employee/${employeeId}`)
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
      fetchAttendanceRecords(selectedEmployee)
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
        <div className={`message message-${message.type}`}>
          {message.text}
        </div>
      )}

      <div className="form-container">
        <h3>Mark Attendance</h3>
        <form onSubmit={handleMarkAttendance}>
          <div className="form-row">
            <div className="form-group">
              <label className="form-label">Select Employee</label>
              <select
                name="employeeId"
                className="form-select"
                value={selectedEmployee}
                onChange={handleEmployeeChange}
                required
              >
                <option value="">-- Choose an employee --</option>
                {employees.map(emp => (
                  <option key={emp.employeeId} value={emp.employeeId}>
                    {emp.fullName} ({emp.employeeId})
                  </option>
                ))}
              </select>
            </div>
            <div className="form-group">
              <label className="form-label">Date</label>
              <input
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
              <label className="form-label">Status</label>
              <select
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
            {loading ? <span><span className="spinner"></span>Marking...</span> : 'Mark Attendance'}
          </button>
        </form>
      </div>

      {selectedEmployee && (
        <>
          <h3 className="section-title" style={{ marginTop: '2rem' }}>
            Attendance Records for {employees.find(e => e.employeeId === selectedEmployee)?.fullName}
          </h3>

          {loading && !attendanceRecords.length ? (
            <div className="loading">
              <span className="spinner"></span> Loading records...
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

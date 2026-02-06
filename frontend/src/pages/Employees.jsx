import React, { useState, useEffect } from 'react'
import { API_URL } from '../config'

export default function Employees() {
  const [employees, setEmployees] = useState([])
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState(null)
  const [showForm, setShowForm] = useState(false)
  const [formData, setFormData] = useState({
    employee_id: '',
    full_name: '',
    email: '',
    department: ''
  })

  useEffect(() => {
    fetchEmployees()
  }, [])

  // Auto-dismiss messages after 3 seconds
  useEffect(() => {
    if (message) {
      const timer = setTimeout(() => setMessage(null), 3000)
      return () => clearTimeout(timer)
    }
  }, [message])

  const fetchEmployees = async () => {
    setLoading(true)
    try {
      const response = await fetch(`${API_URL}/api/employees/`)
      if (!response.ok) throw new Error('Failed to fetch employees')
      const data = await response.json()
      setEmployees(data.employees)
    } catch (error) {
      setMessage({ type: 'error', text: error.message })
    } finally {
      setLoading(false)
    }
  }

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({ ...prev, [name]: value }))
  }

  const handleAddEmployee = async (e) => {
    e.preventDefault()
    setLoading(true)

    try {
      const response = await fetch(`${API_URL}/api/employees/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      })

      if (!response.ok) {
        const error = await response.json()
        throw new Error(error.detail || 'Failed to add employee')
      }

      setMessage({ type: 'success', text: 'Employee added successfully!' })
      setFormData({ employee_id: '', full_name: '', email: '', department: '' })
      setShowForm(false)
      fetchEmployees()
    } catch (error) {
      setMessage({ type: 'error', text: error.message })
    } finally {
      setLoading(false)
    }
  }

  const handleDeleteEmployee = async (employeeId) => {
    if (!window.confirm('Are you sure you want to delete this employee?')) return

    setLoading(true)
    try {
      const response = await fetch(`${API_URL}/api/employees/${employeeId}`, {
        method: 'DELETE'
      })

      if (!response.ok) throw new Error('Failed to delete employee')

      setMessage({ type: 'success', text: 'Employee deleted successfully!' })
      fetchEmployees()
    } catch (error) {
      setMessage({ type: 'error', text: error.message })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page">
      <h2 className="section-title">Employee Management</h2>

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

      <button className="btn-primary" onClick={() => setShowForm(!showForm)}>
        {showForm ? 'Cancel' : 'Add New Employee'}
      </button>

      {showForm && (
        <div className="form-container">
          <h3>Add New Employee</h3>
          <form onSubmit={handleAddEmployee}>
            <div className="form-row">
              <div className="form-group">
                <label className="form-label" htmlFor="employeeId">Employee ID</label>
                <input
                  id="employeeId"
                  type="text"
                  name="employee_id"
                  className="form-input"
                  value={formData.employee_id}
                  onChange={handleInputChange}
                  placeholder="e.g., EMP001"
                  required
                />
              </div>
              <div className="form-group">
                <label className="form-label" htmlFor="fullName">Full Name</label>
                <input
                  id="fullName"
                  type="text"
                  name="full_name"
                  className="form-input"
                  value={formData.full_name}
                  onChange={handleInputChange}
                  placeholder="Enter full name"
                  required
                />
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label className="form-label" htmlFor="email">Email</label>
                <input
                  id="email"
                  type="email"
                  name="email"
                  className="form-input"
                  value={formData.email}
                  onChange={handleInputChange}
                  placeholder="email@example.com"
                  required
                />
              </div>
              <div className="form-group">
                <label className="form-label" htmlFor="department">Department</label>
                <input
                  id="department"
                  type="text"
                  name="department"
                  className="form-input"
                  value={formData.department}
                  onChange={handleInputChange}
                  placeholder="e.g., Engineering"
                  required
                />
              </div>
            </div>

            <button type="submit" className="btn-primary" disabled={loading}>
              {loading ? <span><span className="spinner" aria-label="Loading"></span>Adding...</span> : 'Add Employee'}
            </button>
          </form>
        </div>
      )}

      {loading && !showForm ? (
        <div className="loading" role="status" aria-live="polite">
          <span className="spinner" aria-label="Loading employees"></span> Loading employees...
        </div>
      ) : employees.length === 0 ? (
        <div className="empty-state">
          <div className="empty-state-icon">📋</div>
          <p>No employees found. Add one to get started!</p>
        </div>
      ) : (
        <div className="table-container">
          <table>
            <thead>
              <tr>
                <th>Employee ID</th>
                <th>Full Name</th>
                <th>Email</th>
                <th>Department</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {employees.map(emp => (
                <tr key={emp.employee_id}>
                  <td><strong>{emp.employee_id}</strong></td>
                  <td>{emp.full_name}</td>
                  <td>{emp.email}</td>
                  <td>{emp.department}</td>
                  <td>
                    <div className="action-buttons">
                      <button
                        className="btn-danger btn-small"
                        onClick={() => handleDeleteEmployee(emp.employee_id)}
                        disabled={loading}
                      >
                        Delete
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  )
}

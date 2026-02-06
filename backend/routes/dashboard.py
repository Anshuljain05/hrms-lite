from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
from models.employee import Employee
from models.attendance import Attendance
from schemas.dashboard import DashboardSummary

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


@router.get("/summary", response_model=DashboardSummary)
def get_dashboard_summary(db: Session = Depends(get_db)):
    """
    Get organization-wide dashboard summary with statistics.
    Returns total employees, attendance metrics, and breakdown by department.
    """
    # Get total number of employees
    total_employees = db.query(Employee).count()

    # Get total attendance records
    total_attendance = db.query(Attendance).count()

    # Get present and absent counts
    present_count = db.query(Attendance).filter(
        Attendance.status == "Present"
    ).count()
    absent_count = db.query(Attendance).filter(
        Attendance.status == "Absent"
    ).count()

    # Calculate attendance rate
    attendance_rate = (
        (present_count / total_attendance * 100) if total_attendance > 0 else 0
    )

    # Get employee count by department
    dept_counts = db.query(
        Employee.department,
        func.count(Employee.id).label("count")
    ).group_by(Employee.department).all()

    employees_by_department = {
        dept: count for dept, count in dept_counts
    }

    return {
        "total_employees": total_employees,
        "total_attendance": total_attendance,
        "present": present_count,
        "absent": absent_count,
        "attendance_rate": round(attendance_rate, 2),
        "total_departments": len(employees_by_department),
        "employees_by_department": employees_by_department
    }

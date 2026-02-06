from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from datetime import date
from typing import Optional
from database import get_db
from models.employee import Employee
from models.attendance import Attendance
from schemas.attendance import AttendanceCreate, AttendanceResponse, AttendanceList, AttendanceSummary

router = APIRouter(prefix="/api/attendance", tags=["attendance"])


@router.post("/", response_model=AttendanceResponse, status_code=status.HTTP_201_CREATED)
def mark_attendance(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    """
    Mark attendance for an employee.
    Returns 201 on success, 404 if employee doesn't exist, 409 if duplicate entry exists.
    """
    # Check if employee exists
    employee = db.query(Employee).filter(Employee.employee_id == attendance.employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID '{attendance.employee_id}' not found"
        )

    # Check if attendance already exists for this employee and date
    existing_attendance = db.query(Attendance).filter(
        (Attendance.employee_id == attendance.employee_id) & (Attendance.date == attendance.date)
    ).first()

    if existing_attendance:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Attendance record already exists for employee '{attendance.employee_id}' on {attendance.date}"
        )

    try:
        db_attendance = Attendance(
            employee_id=attendance.employee_id,
            date=attendance.date,
            status=attendance.status
        )
        db.add(db_attendance)
        db.commit()
        db.refresh(db_attendance)
        return db_attendance
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Duplicate attendance entry"
        )


@router.get("/employee/{employee_id}", response_model=AttendanceList)
def get_employee_attendance(
    employee_id: str,
    start_date: Optional[date] = Query(None, description="Filter records from this date (YYYY-MM-DD)"),
    end_date: Optional[date] = Query(None, description="Filter records until this date (YYYY-MM-DD)"),
    db: Session = Depends(get_db)
):
    """
    Retrieve attendance records for a specific employee.
    Optionally filter by date range using start_date and end_date query parameters.
    Returns 404 if employee doesn't exist.
    Example: /api/attendance/employee/EMP001?start_date=2026-02-01&end_date=2026-02-28
    """
    # Check if employee exists
    employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID '{employee_id}' not found"
        )

    # Build query with optional date filtering
    query = db.query(Attendance).filter(Attendance.employee_id == employee_id)
    
    if start_date:
        query = query.filter(Attendance.date >= start_date)
    
    if end_date:
        query = query.filter(Attendance.date <= end_date)
    
    records = query.all()
    return {
        "records": records,
        "total": len(records)
    }


@router.get("/employee/{employee_id}/summary", response_model=AttendanceSummary)
def get_attendance_summary(employee_id: str, db: Session = Depends(get_db)):
    """
    Get attendance summary for a specific employee.
    Returns total records, present count, absent count, and attendance percentage.
    """
    # Check if employee exists
    employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID '{employee_id}' not found"
        )

    # Get all attendance records for this employee
    total_records = db.query(Attendance).filter(Attendance.employee_id == employee_id).count()
    present_count = db.query(Attendance).filter(
        (Attendance.employee_id == employee_id) & (Attendance.status == "Present")
    ).count()
    absent_count = db.query(Attendance).filter(
        (Attendance.employee_id == employee_id) & (Attendance.status == "Absent")
    ).count()
    
    # Calculate attendance percentage
    attendance_percentage = (
        (present_count / total_records * 100) if total_records > 0 else 0
    )

    return {
        "employee_id": employee_id,
        "total_records": total_records,
        "present": present_count,
        "absent": absent_count,
        "attendance_percentage": round(attendance_percentage, 2)
    }


@router.get("/", response_model=AttendanceList)
def get_all_attendance(db: Session = Depends(get_db)):
    """
    Retrieve all attendance records.
    """
    records = db.query(Attendance).all()
    return {
        "records": records,
        "total": len(records)
    }

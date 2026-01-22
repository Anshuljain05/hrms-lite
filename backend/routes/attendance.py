from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import date
from uuid import uuid4
from database import get_db
from models.employee import Employee
from models.attendance import Attendance
from schemas.attendance import AttendanceCreate, AttendanceResponse, AttendanceList

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
def get_employee_attendance(employee_id: str, db: Session = Depends(get_db)):
    """
    Retrieve all attendance records for a specific employee.
    Returns 404 if employee doesn't exist.
    """
    # Check if employee exists
    employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID '{employee_id}' not found"
        )

    records = db.query(Attendance).filter(Attendance.employee_id == employee_id).all()
    return {
        "records": records,
        "total": len(records)
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

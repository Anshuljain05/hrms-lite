from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_db
from models.employee import Employee
from schemas.employee import EmployeeCreate, EmployeeResponse, EmployeeList

router = APIRouter(prefix="/api/employees", tags=["employees"])


@router.post("/", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    """
    Create a new employee.
    Returns 201 on success, 409 if employeeId or email already exists.
    """
    # Check if employee already exists
    existing_employee = db.query(Employee).filter(
        (Employee.employee_id == employee.employee_id) | (Employee.email == employee.email)
    ).first()

    if existing_employee:
        if existing_employee.employee_id == employee.employee_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Employee ID '{employee.employee_id}' already exists"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Email '{employee.email}' already exists"
            )

    try:
        db_employee = Employee(**employee.model_dump())
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Duplicate entry detected"
        )


@router.get("/", response_model=EmployeeList)
def get_employees(db: Session = Depends(get_db)):
    """
    Retrieve all employees.
    """
    employees = db.query(Employee).all()
    return {
        "employees": employees,
        "total": len(employees)
    }


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a specific employee by ID.
    Returns 404 if not found.
    """
    employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID '{employee_id}' not found"
        )
    return employee


@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: str, db: Session = Depends(get_db)):
    """
    Delete an employee by ID.
    Returns 404 if not found, 204 on success.
    """
    employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID '{employee_id}' not found"
        )

    db.delete(employee)
    db.commit()
    return None

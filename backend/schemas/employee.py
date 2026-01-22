from pydantic import BaseModel, EmailStr, ConfigDict
from typing import List


class EmployeeCreate(BaseModel):
    employee_id: str
    full_name: str
    email: EmailStr
    department: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "employee_id": "EMP001",
                "full_name": "John Doe",
                "email": "john@example.com",
                "department": "Engineering"
            }
        }
    )


class EmployeeUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    department: str | None = None


class Employee(BaseModel):
    id: int
    employee_id: str
    full_name: str
    email: str
    department: str

    model_config = ConfigDict(from_attributes=True)


class EmployeeResponse(BaseModel):
    id: int
    employee_id: str
    full_name: str
    email: str
    department: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "employee_id": "EMP001",
                "full_name": "John Doe",
                "email": "john@example.com",
                "department": "Engineering"
            }
        }
    )


class EmployeeList(BaseModel):
    employees: List[EmployeeResponse]
    total: int

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "employees": [
                    {
                        "id": 1,
                        "employee_id": "EMP001",
                        "full_name": "John Doe",
                        "email": "john@example.com",
                        "department": "Engineering"
                    }
                ],
                "total": 1
            }
        }
    )

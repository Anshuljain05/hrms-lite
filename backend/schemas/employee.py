from pydantic import BaseModel, EmailStr, ConfigDict, Field
from typing import List


class EmployeeCreate(BaseModel):
    employee_id: str = Field(..., min_length=1, max_length=20, description="Unique employee identifier")
    full_name: str = Field(..., min_length=1, max_length=100, description="Employee full name")
    email: EmailStr = Field(..., description="Valid email address")
    department: str = Field(..., min_length=1, max_length=50, description="Department name")

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
    full_name: str | None = Field(None, min_length=1, max_length=100, description="Employee full name")
    email: EmailStr | None = Field(None, description="Valid email address")
    department: str | None = Field(None, min_length=1, max_length=50, description="Department name")


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

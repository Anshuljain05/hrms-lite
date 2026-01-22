from pydantic import BaseModel, EmailStr
from typing import List


class EmployeeCreate(BaseModel):
    employeeId: str
    fullName: str
    email: EmailStr
    department: str

    class Config:
        schema_extra = {
            "example": {
                "employeeId": "EMP001",
                "fullName": "John Doe",
                "email": "john@example.com",
                "department": "Engineering"
            }
        }


class EmployeeResponse(EmployeeCreate):
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "employeeId": "EMP001",
                "fullName": "John Doe",
                "email": "john@example.com",
                "department": "Engineering"
            }
        }


class EmployeeList(BaseModel):
    employees: List[EmployeeResponse]
    total: int

    class Config:
        schema_extra = {
            "example": {
                "employees": [
                    {
                        "employeeId": "EMP001",
                        "fullName": "John Doe",
                        "email": "john@example.com",
                        "department": "Engineering"
                    }
                ],
                "total": 1
            }
        }

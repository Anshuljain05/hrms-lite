from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import date


class AttendanceCreate(BaseModel):
    employee_id: str
    date: date
    status: str  # "Present" or "Absent"

    class Config:
        schema_extra = {
            "example": {
                "employee_id": "EMP001",
                "date": "2026-01-22",
                "status": "Present"
            }
        }


class Attendance(BaseModel):
    id: int
    employee_id: str
    date: date
    status: str

    model_config = ConfigDict(from_attributes=True)

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "employee_id": "EMP001",
                "date": "2026-01-22",
                "status": "Present"
            }
        }


class AttendanceResponse(BaseModel):
    id: int
    employee_id: str
    date: date
    status: str

    model_config = ConfigDict(from_attributes=True)

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "employee_id": "EMP001",
                "date": "2026-01-22",
                "status": "Present"
            }
        }


class AttendanceList(BaseModel):
    records: List[AttendanceResponse]
    total: int

    class Config:
        schema_extra = {
            "example": {
                "records": [
                    {
                        "id": 1,
                        "employee_id": "EMP001",
                        "date": "2026-01-22",
                        "status": "Present"
                    }
                ],
                "total": 1
            }
        }

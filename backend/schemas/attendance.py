from pydantic import BaseModel
from typing import List
from datetime import date
from enum import Enum


class StatusEnum(str, Enum):
    PRESENT = "Present"
    ABSENT = "Absent"


class AttendanceCreate(BaseModel):
    employeeId: str
    date: date
    status: StatusEnum

    class Config:
        schema_extra = {
            "example": {
                "employeeId": "EMP001",
                "date": "2026-01-22",
                "status": "Present"
            }
        }


class AttendanceResponse(AttendanceCreate):
    id: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "ATT001",
                "employeeId": "EMP001",
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
                        "id": "ATT001",
                        "employeeId": "EMP001",
                        "date": "2026-01-22",
                        "status": "Present"
                    }
                ],
                "total": 1
            }
        }

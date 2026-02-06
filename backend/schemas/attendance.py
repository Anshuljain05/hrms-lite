from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import date
from enum import Enum


class AttendanceStatus(str, Enum):
    PRESENT = "Present"
    ABSENT = "Absent"


class AttendanceCreate(BaseModel):
    employee_id: str
    date: date
    status: AttendanceStatus  # Enforced to "Present" or "Absent"

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "employee_id": "EMP001",
                "date": "2026-02-06",
                "status": "Present"
            }
        }
    )


class Attendance(BaseModel):
    id: int
    employee_id: str
    date: date
    status: AttendanceStatus

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "employee_id": "EMP001",
                "date": "2026-02-06",
                "status": "Present"
            }
        }
    )


class AttendanceResponse(BaseModel):
    id: int
    employee_id: str
    date: date
    status: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "employee_id": "EMP001",
                "date": "2026-02-06",
                "status": "Present"
            }
        }
    )


class AttendanceList(BaseModel):
    records: List[AttendanceResponse]
    total: int

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "records": [
                    {
                        "id": 1,
                        "employee_id": "EMP001",
                        "date": "2026-02-06",
                        "status": "Present"
                    }
                ],
                "total": 1
            }
        }
    )


class AttendanceSummary(BaseModel):
    employee_id: str
    total_records: int
    present: int
    absent: int
    attendance_percentage: float

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "employee_id": "EMP001",
                "total_records": 20,
                "present": 18,
                "absent": 2,
                "attendance_percentage": 90.0
            }
        }
    )

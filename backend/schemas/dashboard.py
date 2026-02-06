from pydantic import BaseModel, ConfigDict
from typing import Dict

class DashboardSummary(BaseModel):
    total_employees: int
    total_attendance: int
    present: int
    absent: int
    attendance_rate: float
    total_departments: int
    employees_by_department: Dict[str, int]

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "total_employees": 10,
                "total_attendance": 150,
                "present": 140,
                "absent": 10,
                "attendance_rate": 93.33,
                "total_departments": 3,
                "employees_by_department": {
                    "Engineering": 5,
                    "HR": 2,
                    "Sales": 3
                }
            }
        }
    )

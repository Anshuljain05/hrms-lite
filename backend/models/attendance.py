from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, ForeignKey("employees.employee_id"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)  # "Present" or "Absent"
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Attendance(employeeId={self.employeeId}, date={self.date}, status={self.status})>"

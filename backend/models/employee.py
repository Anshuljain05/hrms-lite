from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    department = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship with attendance records - using string reference to avoid circular imports at import time
    attendance_records = relationship("Attendance", back_populates="employee", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Employee(employee_id={self.employee_id}, full_name={self.full_name})>"

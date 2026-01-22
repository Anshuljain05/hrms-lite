from sqlalchemy import Column, String, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base


class Employee(Base):
    __tablename__ = "employees"

    employeeId = Column(String, primary_key=True, index=True, unique=True)
    fullName = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    department = Column(String, nullable=False)

    # Relationship with attendance records - using string reference to avoid circular imports at import time
    attendance_records = relationship("Attendance", back_populates="employee", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Employee(employeeId={self.employeeId}, fullName={self.fullName})>"

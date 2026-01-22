from sqlalchemy import Column, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(String, primary_key=True, index=True)
    employeeId = Column(String, ForeignKey("employees.employeeId"), nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)
    status = Column(String, nullable=False)  # "Present" or "Absent"

    # Relationship with employee - using string reference to avoid circular imports
    employee = relationship("Employee", back_populates="attendance_records", foreign_keys=[employeeId])

    # Unique constraint to prevent duplicate attendance entries
    __table_args__ = (UniqueConstraint("employeeId", "date", name="unique_employee_date"),)

    def __repr__(self):
        return f"<Attendance(employeeId={self.employeeId}, date={self.date}, status={self.status})>"

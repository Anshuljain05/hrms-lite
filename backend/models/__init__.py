# Import models to register them with SQLAlchemy
# Note: order matters due to foreign key relationships
from .employee import Employee
from .attendance import Attendance

__all__ = ["Employee", "Attendance"]



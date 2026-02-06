#!/usr/bin/env python
"""
Database migration script for HRMS Lite
This script recreates the database with the updated schema including the unique constraint on attendance
"""
import os
from sqlalchemy import create_engine, text
from database import Base, DATABASE_URL
from models.employee import Employee
from models.attendance import Attendance

def reset_database():
    """Drop all tables and recreate them with updated schema"""
    # Create engine
    engine = create_engine(DATABASE_URL)
    
    # Drop all existing tables
    print("Dropping existing tables...")
    Base.metadata.drop_all(bind=engine)
    
    # Create all tables with new schema
    print("Creating tables with updated schema...")
    Base.metadata.create_all(bind=engine)
    
    print("Database migration completed successfully!")
    print("Tables created:")
    print("  - employees (with employee_id as unique primary key)")
    print("  - attendance (with unique constraint on (employee_id, date))")

if __name__ == "__main__":
    reset_database()

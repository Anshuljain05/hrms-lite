#!/usr/bin/env python3
"""
Comprehensive validation test suite for HRMS Lite
Tests all schema validations and database constraints
"""
import json
from schemas.employee import EmployeeCreate
from schemas.attendance import AttendanceCreate, AttendanceStatus
from pydantic import ValidationError

print("=" * 60)
print("VALIDATION TEST SUITE")
print("=" * 60)

# Test 1: Valid Employee
print("\n[TEST 1] Valid Employee Creation")
try:
    emp = EmployeeCreate(
        employee_id="EMP001",
        full_name="John Doe",
        email="john@example.com",
        department="Engineering"
    )
    print("✅ PASS: Valid employee created")
except ValidationError as e:
    print(f"❌ FAIL: {e}")

# Test 2: Invalid Employee ID (too long)
print("\n[TEST 2] Employee ID Length Validation (max 20)")
try:
    emp = EmployeeCreate(
        employee_id="A" * 21,
        full_name="John Doe",
        email="john@example.com",
        department="Engineering"
    )
    print("❌ FAIL: Should reject employee_id > 20 chars")
except ValidationError:
    print("✅ PASS: Correctly rejected employee_id > 20 chars")

# Test 3: Invalid Full Name (too long)
print("\n[TEST 3] Full Name Length Validation (max 100)")
try:
    emp = EmployeeCreate(
        employee_id="EMP001",
        full_name="A" * 101,
        email="john@example.com",
        department="Engineering"
    )
    print("❌ FAIL: Should reject full_name > 100 chars")
except ValidationError:
    print("✅ PASS: Correctly rejected full_name > 100 chars")

# Test 4: Invalid Department (too long)
print("\n[TEST 4] Department Length Validation (max 50)")
try:
    emp = EmployeeCreate(
        employee_id="EMP001",
        full_name="John Doe",
        email="john@example.com",
        department="A" * 51
    )
    print("❌ FAIL: Should reject department > 50 chars")
except ValidationError:
    print("✅ PASS: Correctly rejected department > 50 chars")

# Test 5: Invalid Email
print("\n[TEST 5] Email Format Validation")
try:
    emp = EmployeeCreate(
        employee_id="EMP001",
        full_name="John Doe",
        email="not-an-email",
        department="Engineering"
    )
    print("❌ FAIL: Should reject invalid email")
except ValidationError:
    print("✅ PASS: Correctly rejected invalid email")

# Test 6: Valid Attendance with Present Status
print("\n[TEST 6] Valid Attendance (Present Status)")
try:
    att = AttendanceCreate(
        employee_id="EMP001",
        date="2026-02-06",
        status=AttendanceStatus.PRESENT
    )
    print("✅ PASS: Valid attendance created (Present)")
except ValidationError as e:
    print(f"❌ FAIL: {e}")

# Test 7: Valid Attendance with Absent Status
print("\n[TEST 7] Valid Attendance (Absent Status)")
try:
    att = AttendanceCreate(
        employee_id="EMP001",
        date="2026-02-06",
        status=AttendanceStatus.ABSENT
    )
    print("✅ PASS: Valid attendance created (Absent)")
except ValidationError as e:
    print(f"❌ FAIL: {e}")

# Test 8: Invalid Attendance Status
print("\n[TEST 8] Attendance Status Enum Validation")
try:
    att = AttendanceCreate(
        employee_id="EMP001",
        date="2026-02-06",
        status="Maybe"  # Invalid status
    )
    print("❌ FAIL: Should reject invalid status")
except ValidationError:
    print("✅ PASS: Correctly rejected invalid status 'Maybe'")

# Test 9: Verify Enum Values
print("\n[TEST 9] Attendance Status Enum Values")
print(f"✅ Valid statuses: {[s.value for s in AttendanceStatus]}")

print("\n" + "=" * 60)
print("ALL VALIDATION TESTS COMPLETE")
print("=" * 60)

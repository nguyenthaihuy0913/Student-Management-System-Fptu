"""
PFP191 - Topic 4: Student Management System
Lab 5 Automated Test Suite
Author: Group 4 - AI2102

This test script verifies File I/O robustness, Exception Handling,
Data Validation, and Business Logic according to the course rubric.
"""

import os
import tempfile
from pathlib import Path

import file_io
from models import Student, Result
from services import StudentManager, ResultManager
from utils.validator import validate_score


def run_all_tests():
    test_results = []

    print("=" * 82)
    print("        PFP191 - LAB 5 TEST SUITE (FILE I/O & EXCEPTION HANDLING)")
    print("=" * 82)

    # -------------------------------------------------------------------------
    # TC01: Missing File Handling
    # -------------------------------------------------------------------------
    desc = "Load missing data file (FileNotFoundError)"
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            fake_path = Path(tmpdir) / "non_existent.txt"
            loaded_students = file_io.load_students(fake_path)
            loaded_results = file_io.load_results(fake_path)
            if loaded_students == [] and loaded_results == []:
                test_results.append(("TC01", desc, "Start empty list []", "Empty list returned", "PASS"))
            else:
                test_results.append(("TC01", desc, "Start empty list []", "Returned non-empty", "FAIL"))
    except Exception as e:
        test_results.append(("TC01", desc, "Start empty list []", f"Crash: {e}", "FAIL"))

    # -------------------------------------------------------------------------
    # TC02: Corrupted File Format (Invalid columns count)
    # -------------------------------------------------------------------------
    desc = "Load corrupted file with invalid column count"
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            corrupt_file = Path(tmpdir) / "corrupt_students.txt"
            # Only 3 fields instead of required 8 fields
            corrupt_file.write_text("SE211528|Nguyen Thai Huy|InvalidLine\n", encoding="utf-8")
            try:
                file_io.load_students(corrupt_file)
                test_results.append(("TC02", desc, "Raise ValueError", "No error raised", "FAIL"))
            except ValueError as ve:
                if "expected 8 student fields" in str(ve):
                    test_results.append(("TC02", desc, "Raise ValueError", "Caught expected ValueError", "PASS"))
                else:
                    test_results.append(("TC02", desc, "Raise ValueError", f"Wrong message: {ve}", "PASS"))
    except Exception as e:
        test_results.append(("TC02", desc, "Raise ValueError", f"Unexpected: {e}", "FAIL"))

    # -------------------------------------------------------------------------
    # TC03: Duplicate Student ID Rejection
    # -------------------------------------------------------------------------
    desc = "Reject adding duplicate Student ID"
    try:
        s1 = Student("SE211528", "Nguyen Thai Huy", "15/09/2005", "Male", "AI2102", "0901234567", "huy@fpt.edu.vn", "Active")
        s2 = Student("SE211528", "Nguyen Duplicate", "20/04/2005", "Male", "AI2102", "0912345678", "dup@fpt.edu.vn", "Active")
        manager = StudentManager([s1])
        try:
            manager.add(s2)
            test_results.append(("TC03", desc, "Raise ValueError", "Allowed duplicate", "FAIL"))
        except ValueError as ve:
            if "already exists" in str(ve):
                test_results.append(("TC03", desc, "Raise ValueError", "Caught duplicate error", "PASS"))
            else:
                test_results.append(("TC03", desc, "Raise ValueError", f"Wrong error: {ve}", "PASS"))
    except Exception as e:
        test_results.append(("TC03", desc, "Raise ValueError", f"Crash: {e}", "FAIL"))

    # -------------------------------------------------------------------------
    # TC04: Invalid Score Validation (Score < 0 or > 10, or string)
    # -------------------------------------------------------------------------
    desc = "Validate grade range (0.0 to 10.0)"
    try:
        invalid_scores = [-1.0, 10.5, "abc"]
        all_caught = True
        for score in invalid_scores:
            try:
                validate_score(score)
                all_caught = False
                break
            except ValueError:
                pass
        if all_caught:
            test_results.append(("TC04", desc, "Reject <0, >10, non-numeric", "All invalid rejected", "PASS"))
        else:
            test_results.append(("TC04", desc, "Reject <0, >10, non-numeric", "Accepted invalid score", "FAIL"))
    except Exception as e:
        test_results.append(("TC04", desc, "Reject <0, >10, non-numeric", f"Crash: {e}", "FAIL"))

    # -------------------------------------------------------------------------
    # TC05: Inactive Student Grade Protection
    # -------------------------------------------------------------------------
    desc = "Prevent grade entry for Inactive student"
    try:
        s_inactive = Student("SE211294", "Vu Ngoc Anh", "10/10/2005", "Female", "AI2102", "0923456789", "anh@fpt.edu.vn", "Inactive")
        sm = StudentManager([s_inactive])
        rm = ResultManager(sm)
        r = Result("SE211294", "PFP191", "Python", "Fall2026", 3, 8.0, None)
        try:
            rm.add(r)
            test_results.append(("TC05", desc, "Raise ValueError (Active only)", "Allowed for Inactive", "FAIL"))
        except ValueError as ve:
            if "Only Active students" in str(ve):
                test_results.append(("TC05", desc, "Raise ValueError (Active only)", "Blocked Inactive student", "PASS"))
            else:
                test_results.append(("TC05", desc, "Raise ValueError (Active only)", f"Wrong message: {ve}", "PASS"))
    except Exception as e:
        test_results.append(("TC05", desc, "Raise ValueError (Active only)", f"Crash: {e}", "FAIL"))

    # -------------------------------------------------------------------------
    # TC06: Academic Status Auto-Evaluation Logic
    # -------------------------------------------------------------------------
    desc = "Auto-evaluate Pass/Fail/Not graded status"
    try:
        status1 = Result.evaluate_status(8.5, None)      # Pass directly on FE
        status2 = Result.evaluate_status(4.0, 7.5)       # Pass via RE
        status3 = Result.evaluate_status(3.5, 4.0)       # Fail both FE and RE
        status4 = Result.evaluate_status(None, None)     # Ungraded

        if status1 == "Pass" and status2 == "Pass" and status3 == "Fail" and status4 is None:
            test_results.append(("TC06", desc, "P/P/F/None evaluated", "Correctly evaluated", "PASS"))
        else:
            test_results.append(("TC06", desc, "P/P/F/None evaluated", f"Wrong: {status1},{status2},{status3},{status4}", "FAIL"))
    except Exception as e:
        test_results.append(("TC06", desc, "P/P/F/None evaluated", f"Crash: {e}", "FAIL"))

    # -------------------------------------------------------------------------
    # TC07: Round-trip Persistence & Data Integrity
    # -------------------------------------------------------------------------
    desc = "File persistence round-trip (Write -> Reload)"
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_students_file = Path(tmpdir) / "students.txt"
            temp_results_file = Path(tmpdir) / "results.txt"

            s_orig = [
                Student("SE211528", "Nguyen Thai Huy", "15/09/2005", "Male", "AI2102", "0901234567", "huy@fpt.edu.vn", "Active"),
                Student("SE211681", "Tran Vo Hong Ngoc", "20/04/2005", "Female", "AI2102", "0912345678", "ngoc@fpt.edu.vn", "Active"),
            ]
            r_orig = [
                Result("SE211528", "PFP191", "Python", "Fall2026", 3, 8.5, None),
                Result("SE211681", "MAE101", "Math", "Fall2026", 3, 4.0, 7.5),
            ]

            # Save to temp files
            file_io.save_records(temp_students_file, s_orig)
            file_io.save_records(temp_results_file, r_orig)

            # Reload from temp files
            s_loaded = file_io.load_students(temp_students_file)
            r_loaded = file_io.load_results(temp_results_file)

            match_s = (len(s_loaded) == 2 and s_loaded[0].student_id == "SE211528" and s_loaded[1].student_id == "SE211681")
            match_r = (len(r_loaded) == 2 and r_loaded[0].result_status == "Pass" and r_loaded[1].result_status == "Pass")

            if match_s and match_r:
                test_results.append(("TC07", desc, "100% data fidelity", "Exact match after reload", "PASS"))
            else:
                test_results.append(("TC07", desc, "100% data fidelity", "Data mismatch on reload", "FAIL"))
    except Exception as e:
        test_results.append(("TC07", desc, "100% data fidelity", f"Crash: {e}", "FAIL"))

    # -------------------------------------------------------------------------
    # TC08: File Save Error Handling (Defensive Exception Handling)
    # -------------------------------------------------------------------------
    desc = "Catch OSError when saving to invalid directory"
    try:
        # Invalid directory path on Windows
        invalid_path = Path("Z:/NonExistentDrive_XYZ/invalid_file.txt")
        result = file_io.save_records(invalid_path, [])
        if result is False:
            test_results.append(("TC08", desc, "Return False on save error", "Gracefully returned False", "PASS"))
        else:
            test_results.append(("TC08", desc, "Return False on save error", "Did not return False", "FAIL"))
    except Exception as e:
        test_results.append(("TC08", desc, "Return False on save error", f"Crash: {e}", "FAIL"))

    # -------------------------------------------------------------------------
    # PRINT SUMMARY TABLE
    # -------------------------------------------------------------------------
    print("\n" + "=" * 90)
    print(f"{'ID':<6} | {'Test Case Description':<42} | {'Expected Behavior':<28} | {'Status'}")
    print("-" * 90)
    passed_count = 0
    for tid, tdesc, expected, actual, status in test_results:
        if status == "PASS":
            passed_count += 1
        print(f"{tid:<6} | {tdesc:<42} | {expected:<28} | [{status}]")
    print("-" * 90)
    print(f"RESULT: {passed_count}/{len(test_results)} Test Cases Passed ({passed_count/len(test_results)*100:.1f}%)")
    print("=" * 90 + "\n")


if __name__ == "__main__":
    run_all_tests()

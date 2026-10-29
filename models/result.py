"""
Result Model
Class representing student course assessment outcomes.
"""


class Result:
    """Represents course evaluation grades for a student, auto-evaluating pass/fail status."""

    def __init__(self, student_id, course_id, grade_fe, grade_re=None, result_status=None):
        self._student_id = student_id
        self._course_id = course_id
        self._grade_fe = self._format_grade(grade_fe)
        self._grade_re = self._format_grade(grade_re)

    @staticmethod
    def _format_grade(grade):
        if grade is None:
            return ""
        return str(grade).strip()

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value

    @property
    def grade_fe(self):
        return self._grade_fe

    @grade_fe.setter
    def grade_fe(self, value):
        self._grade_fe = self._format_grade(value)

    @property
    def grade_re(self):
        return self._grade_re

    @grade_re.setter
    def grade_re(self, value):
        self._grade_re = self._format_grade(value)

    @property
    def result_status(self):
        """
        Dynamically determine academic status according to FPTU assessment criteria:
        - Pass: FE >= 5.0 OR (FE < 5.0 and RE >= 5.0)
        - Fail: FE < 5.0 and (RE is empty or RE < 5.0)
        """
        try:
            fe_val = float(self._grade_fe) if self._grade_fe != "" else 0.0
            if fe_val >= 5.0:
                return "Pass"

            if self._grade_re != "":
                re_val = float(self._grade_re)
                if re_val >= 5.0:
                    return "Pass"
                return "Fail"
            return "Fail"
        except (ValueError, TypeError):
            return "Fail"

    def to_file_line(self):
        """Format course result data into pipe-delimited text line for file persistence."""
        return f"{self._student_id}|{self._course_id}|{self._grade_fe}|{self._grade_re}|{self.result_status}\n"

    def to_dict(self):
        """Convert object attributes to dictionary representation."""
        return {
            "student_id": self._student_id,
            "course_id": self._course_id,
            "grade_fe": self._grade_fe,
            "grade_re": self._grade_re,
            "result_status": self.result_status,
        }

    def __str__(self):
        re_info = f", RE: {self._grade_re}" if self._grade_re else ""
        return f"[{self._student_id}] {self._course_id} - FE: {self._grade_fe}{re_info} => {self.result_status}"

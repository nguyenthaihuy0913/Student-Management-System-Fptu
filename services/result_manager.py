from models import Result
from utils.validator import validate_student_id, validate_course_id, validate_score, validate_text, validate_credits


class ResultManager:
    def __init__(self, student_manager, results=None):
        self._student_manager = student_manager
        self._results = []
        for result in results or []:
            self.add(result, loading=True)

    @property
    def results(self):
        return self._results.copy()

    def find(self, student_id, course_id):
        student_id = validate_student_id(student_id)
        course_id = validate_course_id(course_id)
        for result in self._results:
            if result.student_id == student_id and result.course_id == course_id:
                return result
        return None

    def check_student(self, student_id, require_active=True):
        student = self._student_manager.find(student_id)
        if student is None:
            raise ValueError("Student not found.")
        if require_active and student.status != "Active":
            raise ValueError("Only Active students can have grades added or updated.")

    def add(self, result, loading=False):
        if not isinstance(result, Result):
            raise ValueError("Expected a Result object.")
        if not loading:
            validate_text(result.course_name)
            validate_text(result.semester)
            validate_credits(result.credits)
        self.check_student(result.student_id, require_active=not loading)
        if self.find(result.student_id, result.course_id) is not None:
            raise ValueError("Student/course result already exists.")
        self._results.append(result)

    def update_grades(self, student_id, course_id, grade_fe, grade_re=None):
        self.check_student(student_id)
        result = self.find(student_id, course_id)
        if result is None:
            raise ValueError("Result not found.")
        fe = validate_score(grade_fe)
        re = validate_score(grade_re)
        if fe is None or fe >= 5:
            re = None
        result.grade_fe = fe
        result.grade_re = re

    def update_course_details(self, student_id, course_id, course_name, semester, credits):
        self.check_student(student_id, require_active=False)
        result = self.find(student_id, course_id)
        if result is None:
            raise ValueError("Result not found.")
        name = validate_text(course_name)
        term = validate_text(semester)
        count = validate_credits(credits)
        result.course_name = name
        result.semester = term
        result.credits = count

    def search(self, student_id):
        student_id = validate_student_id(student_id)
        return [r for r in self._results if r.student_id == student_id]

    def sorted_results(self):
        return sorted(self._results, key=lambda r: r.result_status or "", reverse=True)

    def passed_results(self):
        return [r for r in self._results if r.result_status == "Pass"]

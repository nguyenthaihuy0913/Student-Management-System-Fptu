from utils.validator import validate_student_id, validate_course_id, validate_text, validate_score, validate_credits



class Result:

    def __init__(
        self, student_id, course_id, course_name, semester, credits,
        grade_fe=None, grade_re=None,
    ):
        self._student_id = validate_student_id(student_id)
        self._course_id = validate_course_id(course_id)
        self.course_name = course_name
        self.semester = semester
        self.credits = credits
        self.grade_fe = grade_fe
        self.grade_re = grade_re

    @staticmethod
    def _format_grade(grade):
        return validate_score(grade)

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        self._course_name = None if value is None else validate_text(value)

    @property
    def semester(self):
        return self._semester

    @semester.setter
    def semester(self, value):
        self._semester = None if value is None else validate_text(value)

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, value):
        self._credits = None if value is None else validate_credits(value)

    @property
    def student_id(self):
        return self._student_id

    @property
    def course_id(self):
        return self._course_id

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

    @staticmethod
    def evaluate_status(grade_fe, grade_re=None):
        fe = Result._format_grade(grade_fe)
        re = Result._format_grade(grade_re)
        if fe is None:
            return None
        if fe >= 5.0 or (re is not None and re >= 5.0):
            return "Pass"
        return "Fail"

    @property
    def result_status(self):
        return self.evaluate_status(self._grade_fe, self._grade_re)

    def to_file_line(self):
        fe = "" if self._grade_fe is None else str(self._grade_fe)
        re = "" if self._grade_re is None else str(self._grade_re)
        status = self.result_status or ""
        name = self._course_name or ""
        semester = self._semester or ""
        credits = "" if self._credits is None else str(self._credits)
        return f"{self._student_id}|{self._course_id}|{name}|{semester}|{credits}|{fe}|{re}|{status}\n"

    def to_dict(self):
        return {
            "student_id": self._student_id,
            "course_id": self._course_id,
            "course_name": self._course_name,
            "semester": self._semester,
            "credits": self._credits,
            "grade_fe": self._grade_fe,
            "grade_re": self._grade_re,
            "result_status": self.result_status,
        }

    def __str__(self):
        fe_info = "Not graded" if self._grade_fe is None else str(self._grade_fe)
        re_info = f", RE: {self._grade_re}" if self._grade_re is not None else ""
        status = self.result_status or "Not graded"
        name = self._course_name or "[Missing course name]"
        semester = self._semester or "[Missing semester]"
        credits = self._credits if self._credits is not None else "?"
        return f"[{self._student_id}] {self._course_id} - {name} ({semester}, {credits} credits) - FE: {fe_info}{re_info} => {status}"

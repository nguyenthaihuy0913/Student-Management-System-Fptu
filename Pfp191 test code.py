class ResultManagement:
    def __init__(self):
        self.results_db = [
            {"student_id": "SE211528", "course_id": "PFP191", "fe_grade": None, "re_grade": None, "result_status": None},
            {"student_id": "SE211681", "course_id": "PFP191", "fe_grade": None, "re_grade": None, "result_status": None},
            {"student_id": "SE211294", "course_id": "PFP191", "fe_grade": None, "re_grade": None, "result_status": None}
        ]

    def _evaluate_and_save_score(self, student_id, course_id, attempt1_score, attempt2_score=None):
        final_result = "Fail"
        
        if attempt1_score is not None and attempt1_score >= 5.0:
            final_result = "Pass"
        elif attempt2_score is not None and attempt2_score >= 5.0:
            final_result = "Pass"

        record_found = False
        for record in self.results_db:
            if record["student_id"] == student_id and record["course_id"] == course_id:
                record["fe_grade"] = attempt1_score
                record["re_grade"] = attempt2_score
                record["result_status"] = final_result
                record_found = True
                break

        if not record_found:
            print(f"[-] Lỗi: Sinh viên {student_id} chưa đăng ký khóa {course_id}!")
            return False
        else:
            print(f"[+] Thành công! Kết quả học tập của {student_id}: {final_result}")
            return True

    def addCourseGrade(self, student_id, course_id, fe_score, re_score=None):
        self._evaluate_and_save_score(student_id, course_id, fe_score, re_score)

    def updateGradeOrStatus(self, student_id, course_id, new_fe, new_re=None):
        self._evaluate_and_save_score(student_id, course_id, new_fe, new_re)

    def searchEnrollments(self, student_id):
        enrollments = [rec for rec in self.results_db if rec["student_id"] == student_id]
        if not enrollments:
            print("  -> Không tìm thấy dữ liệu.")
        else:
            for rec in enrollments:
                print(f"  -> {rec['course_id']} | FE: {rec['fe_grade']} | RE: {rec['re_grade']} | Status: {rec['result_status']}")

    def displayExamResults(self):
        evaluated_records = [rec for rec in self.results_db if rec["result_status"] is not None]
        sorted_results = sorted(evaluated_records, key=lambda x: x['result_status'], reverse=True)
        for rec in sorted_results:
            print(f"  -> SV: {rec['student_id']} | Môn: {rec['course_id']} | FE: {rec['fe_grade']} | RE: {rec['re_grade']} | Status: {rec['result_status']}")

    def displayPassedStudents(self):
        passed = [rec for rec in self.results_db if rec["result_status"] == "Pass"]
        for rec in passed:
            print(f"  -> SV: {rec['student_id']} | Môn: {rec['course_id']} | Status: Pass")

    def openResultSubMenu(self):
        while True:
            print("\n========== RESULT MANAGEMENT ==========")
            print("1. Add student's course grade")
            print("2. Update student's grade or status")
            print("3. Search enrollments by student ID")
            print("4. Display exam results (sorted by status)")
            print("5. Display passed students")
            print("0. Return to main menu")
            print("=======================================")
            
            choice = input("Enter your choice: ")

            if choice == '1' or choice == '2':
                student_id = input("  Nhập mã sinh viên (Student ID): ")
                course_id = input("  Nhập mã khóa học (Course ID): ")
                
                try:
                    fe_input = input("  Nhập điểm FE (để trống nếu chưa thi): ")
                    fe_score = float(fe_input) if fe_input else None
                    
                    re_input = input("  Nhập điểm RE (để trống nếu không thi lại): ")
                    re_score = float(re_input) if re_input else None
                    
                    if choice == '1':
                        print("\n[Hệ thống] Đang thêm điểm...")
                        self.addCourseGrade(student_id, course_id, fe_score, re_score)
                    else:
                        print("\n[Hệ thống] Đang cập nhật điểm...")
                        self.updateGradeOrStatus(student_id, course_id, fe_score, re_score)
                        
                except ValueError:
                    print("[-] Lỗi: Điểm phải là một con số hợp lệ!")

            elif choice == '3':
                student_id = input("  Nhập mã sinh viên cần tìm: ")
                print(f"\n[Kết quả tìm kiếm cho {student_id}]")
                self.searchEnrollments(student_id)

            elif choice == '4':
                print("\n[Bảng kết quả thi - Đã sắp xếp]")
                self.displayExamResults()

            elif choice == '5':
                print("\n[Danh sách sinh viên Pass]")
                self.displayPassedStudents()

            elif choice == '0':
                print("Returning to main menu...")
                break

            else:
                print("Lựa chọn không hợp lệ, vui lòng chọn từ 0 đến 5.")

if __name__ == "__main__":
    rm = ResultManagement()
    rm.openResultSubMenu()

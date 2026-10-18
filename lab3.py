
MIN_SCORE = 0.0
MAX_SCORE = 10.0
PASS_SCORE = 5.0

# Cơ sở dữ liệu giả lập (key: mã sinh viên)
database = {
    "SV001": {"name": "An", "result": None},
    "SV002": {"name": "Binh", "result": None},
}


def is_valid_score(score):
    """Điểm hợp lệ khi là số và nằm trong [0, 10]."""
    return isinstance(score, (int, float)) and MIN_SCORE <= score <= MAX_SCORE


def read_score(prompt):
    """Nhập điểm, lặp lại cho tới khi nhập đúng (là số, 0 <= điểm <= 10)."""
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            score = float(raw)
        except ValueError:
            print(f"Lỗi: '{raw}' không phải là số. Vui lòng nhập lại.")
            continue

        # float('nan') và 'inf' cũng là float nên phải chặn bằng khoảng điểm
        if not is_valid_score(score):
            print(f"Lỗi: điểm phải nằm trong khoảng {MIN_SCORE:g} - {MAX_SCORE:g}. Vui lòng nhập lại.")
            continue

        return score


def find_database(student_id):
    """Find Database: trả về bản ghi hoặc None nếu không tìm thấy."""
    return database.get(student_id)


def process_scores(student_id, attempt_1, get_attempt_2):
    # Kiểm tra biên cho điểm lần 1 (phòng khi hàm được gọi từ nơi khác)
    if not is_valid_score(attempt_1):
        raise ValueError(f"Điểm lần 1 không hợp lệ: {attempt_1}")

    # Start
    result = "Fail"
    attempt_2 = None

    # If Attempt_1 >= 5.0
    if attempt_1 >= PASS_SCORE:
        result = "Pass"  # Đạt ngay, không cần điểm lần 2
    else:
        # False -> chỉ lúc này mới cần điểm lần 2
        attempt_2 = get_attempt_2()
        if not is_valid_score(attempt_2):
            raise ValueError(f"Điểm lần 2 không hợp lệ: {attempt_2}")

        # If Attempt_2 >= 5.0
        if attempt_2 >= PASS_SCORE:
            result = "Pass"
        else:
            result = "Fail"

    # Find Database
    record = find_database(student_id)

    # Record not found?
    if record is None:
        print("Error: Not registered")
    else:
        # Update Database
        record["result"] = result
        record["attempt_1"] = attempt_1
        record["attempt_2"] = attempt_2
        print("Success: Scores saved")

    # Stop
    return result


if __name__ == "__main__":
    student_id = input("Nhập mã sinh viên: ").strip()
    attempt_1 = read_score("Nhập điểm lần 1 (0-10): ")

    # Điểm lần 2 chỉ được hỏi khi lần 1 < 5.0
    final = process_scores(
        student_id,
        attempt_1,
        lambda: read_score("Nhập điểm lần 2 (0-10): "),
    )
    print("Kết quả:", final)
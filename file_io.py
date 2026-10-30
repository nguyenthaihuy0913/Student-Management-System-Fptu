from models import Student, Result


def load_students(filepath):
    students = []
    try:
        with open(filepath, encoding="utf-8") as file:
            for number, line in enumerate(file, 1):
                if not line.strip():
                    continue
                parts = [part.strip() for part in line.strip().split("|")]
                if len(parts) != 8:
                    raise ValueError(f"{filepath}, line {number}: expected 8 student fields.")
                students.append(Student(*parts))
    except FileNotFoundError:
        print(f"[Info] {filepath} not found; starting empty.")
    return students


def load_results(filepath):
    results = []
    try:
        with open(filepath, encoding="utf-8") as file:
            for number, line in enumerate(file, 1):
                if not line.strip():
                    continue
                parts = [part.strip() for part in line.strip().split("|")]
                if len(parts) == 5:
                    result = Result(parts[0], parts[1], None, None, None, parts[2], parts[3])
                    print(f"[Info] {parts[0]}/{parts[1]}: old format; course details need completing.")
                elif len(parts) == 8:
                    result = Result(parts[0], parts[1], parts[2] or None, parts[3] or None,
                                    parts[4] or None, parts[5], parts[6])
                else:
                    raise ValueError(f"{filepath}, line {number}: expected 5 old or 8 new result fields.")
                results.append(result)
    except FileNotFoundError:
        print(f"[Info] {filepath} not found; starting empty.")
    return results


def save_records(filepath, records):
    try:
        lines = [record.to_file_line() for record in records]
        with open(filepath, "w", encoding="utf-8") as file:
            file.writelines(lines)
        return True
    except (OSError, ValueError) as error:
        print(f"[Error] Cannot save {filepath}: {error}")
        return False

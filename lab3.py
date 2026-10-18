MIN_SCORE = 0.0
MAX_SCORE = 10.0
PASS_SCORE = 5.0

# Simulated database (key: student ID)
database = {
    "SV001": {"name": "An", "result": None},
    "SV002": {"name": "Binh", "result": None},
}


def is_valid_score(score):
    """Score is valid if it is a number and within [0, 10]."""
    return isinstance(score, (int, float)) and MIN_SCORE <= score <= MAX_SCORE


def read_score(prompt):
    """Input score, repeat until valid (is a number, 0 <= score <= 10)."""
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            score = float(raw)
        except ValueError:
            print(f"Error: '{raw}' is not a number. Please enter again.")
            continue

        # float('nan') and 'inf' are also floats so they must be blocked by the score range
        if not is_valid_score(score):
            print(f"Error: score must be between {MIN_SCORE:g} and {MAX_SCORE:g}. Please enter again.")
            continue

        return score


def find_database(student_id):
    """Find Database: returns the record or None if not found."""
    return database.get(student_id)


def process_scores(student_id, attempt_1, get_attempt_2):
    # Boundary check for attempt 1 (just in case the function is called from elsewhere)
    if not is_valid_score(attempt_1):
        raise ValueError(f"Invalid attempt 1 score: {attempt_1}")

    # Start
    result = "Fail"
    attempt_2 = None

    # If Attempt_1 >= 5.0
    if attempt_1 >= PASS_SCORE:
        result = "Pass"  # Passed immediately, no attempt 2 needed
    else:
        # False -> only now is attempt 2 needed
        attempt_2 = get_attempt_2()
        if not is_valid_score(attempt_2):
            raise ValueError(f"Invalid attempt 2 score: {attempt_2}")

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
    student_id = input("Enter student ID: ").strip()
    attempt_1 = read_score("Enter attempt 1 score (0-10): ")

    # Attempt 2 is only asked when attempt 1 < 5.0
    final = process_scores(
        student_id,
        attempt_1,
        lambda: read_score("Enter attempt 2 score (0-10): "),
    )
    print("Result:", final)
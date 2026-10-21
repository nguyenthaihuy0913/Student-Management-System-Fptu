def loadFromFile(FilePath):
    dataList = []
    file = None
    try:
        file = open(FilePath, 'r', encoding='utf-8')
        for line in file:
            cleaned_line = line.strip()
            if not cleaned_line:
                continue

            parts = cleaned_line.split("|")
            if len(parts) == 8:
                student = {
                    "student_id": parts[0].strip(),
                    "full_name": parts[1].strip(),
                    "date_of_birth": parts[2].strip(),
                    "gender": parts[3].strip(),
                    "class_name": parts[4].strip(),
                    "phone": parts[5].strip(),
                    "email": parts[6].strip(),
                    "status": parts[7].strip()
                }
                dataList.append(student)

        print(f"[System] Successfully loaded {len(dataList)} student records from '{FilePath}'.")
        return dataList
    except FileNotFoundError:
        print(f"[System Warning] File '{FilePath}' not found! Initializing empty list.")
        return []
    except Exception as e:
        print(f"[System Error] Error reading file '{FilePath}': {e}")
        return []
    finally:
        if file is not None and not file.closed:
            file.close()


def saveToFile(FilePath, DataList):
    file = None
    try:
        file = open(FilePath, 'w', encoding='utf-8')
        for s in DataList:
            line = f"{s['student_id']}|{s['full_name']}|{s['date_of_birth']}|{s['gender']}|{s['class_name']}|{s['phone']}|{s['email']}|{s['status']}\n"
            file.write(line)
        print(f"[System] Successfully saved {len(DataList)} student records to '{FilePath}'.")
        return True
    except Exception as e:
        print(f"[System Error] Error saving file '{FilePath}': {e}")
        return False
    finally:
        if file is not None and not file.closed:
            file.flush()
            file.close()


def loadResultsFromFile(FilePath):
    dataList = []
    file = None
    try:
        file = open(FilePath, 'r', encoding='utf-8')
        for line in file:
            cleaned_line = line.strip()
            if not cleaned_line:
                continue

            parts = cleaned_line.split("|")
            if len(parts) >= 5:
                result = {
                    "student_id": parts[0].strip(),
                    "course_id": parts[1].strip(),
                    "grade_fe": parts[2].strip(),
                    "grade_re": parts[3].strip(),
                    "result_status": parts[4].strip()
                }
                dataList.append(result)

        print(f"[System] Successfully loaded {len(dataList)} result records from '{FilePath}'.")
        return dataList
    except FileNotFoundError:
        print(f"[System Warning] File '{FilePath}' not found! Initializing empty result list.")
        return []
    except Exception as e:
        print(f"[System Error] Error reading file '{FilePath}': {e}")
        return []
    finally:
        if file is not None and not file.closed:
            file.close()


def saveResultsToFile(FilePath, DataList):
    file = None
    try:
        file = open(FilePath, 'w', encoding='utf-8')
        for r in DataList:
            line = f"{r['student_id']}|{r['course_id']}|{r['grade_fe']}|{r['grade_re']}|{r['result_status']}\n"
            file.write(line)

        print(f"[System] Successfully saved {len(DataList)} result records to '{FilePath}'.")
        return True
    except Exception as e:
        print(f"[System Error] Error saving file '{FilePath}': {e}")
        return False
    finally:
        if file is not None and not file.closed:
            file.flush()
            file.close()

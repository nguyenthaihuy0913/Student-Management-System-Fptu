def LoadFromFile(FilePath):
    """
    Mở file ở chế độ đọc 'r', xử lý exception nếu không tìm thấy file.
    Trả về danh sách dữ liệu đọc được.
    """
    dataList = []
    file = None
    try:
        # Mở file bằng open(..., 'r') với mã hóa utf-8
        file = open(FilePath, 'r', encoding='utf-8')
        for line in file:
            # Xóa khoảng trắng/dấu xuống dòng ở hai đầu
            cleaned_line = line.strip()
            if cleaned_line:
                dataList.append(cleaned_line)
        print(f"[Thành công] Đã tải dữ liệu từ file '{FilePath}'.")
        return dataList
    except FileNotFoundError:
        print(f"[Cảnh báo] File '{FilePath}' không tồn tại! Khởi tạo danh sách.")
        return []
    except Exception as e:
        print(f"[Lỗi] Đã xảy ra lỗi khi đọc file '{FilePath}': {e}")
        return []
    finally:
        # Đảm bảo đóng file an toàn nếu file đã được mở
        if file is not None and not file.closed:
            file.close()


def SaveToFile(FilePath, DataList):
    """
    Mở file ở chế độ ghi 'w' và lưu danh sách dữ liệu vào file.
    """
    file = None
    try:
        # Mở file bằng open(..., 'w')
        file = open(FilePath, 'w', encoding='utf-8')
        for item in DataList:
            file.write(f"{item}\n")
        print(f"[Thành công] Đã ghi dữ liệu vào file '{FilePath}'.")
        return True
    except Exception as e:
        print(f"[Lỗi] Đã xảy ra lỗi khi ghi file '{FilePath}': {e}")
        return False
    finally:
        if file is not None and not file.closed:
            file.flush()
            file.close()
def count_lines(file_path):
    """Reads a file and counts the number of lines."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(f"File '{file_path}' contains {len(lines)} line(s).")
    except FileNotFoundError:
        print("Error: File not found!")

count_lines("data.txt")
import os

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def count_lines(self):
        if not os.path.exists(self.file_path):
            print("File not found!")
            return 0
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return len(file.readlines())

    def write_data(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(data)
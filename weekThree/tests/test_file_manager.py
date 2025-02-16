import pytest
from weekThree.file_manager import FileManager

def test_count_lines(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello\nWorld\n")
    fm = FileManager(str(file))
    assert fm.count_lines() == 2

def test_write_data(tmp_path):
    file = tmp_path / "test.txt"
    fm = FileManager(str(file))
    fm.write_data("Test data")
    assert file.read_text() == "Test data"
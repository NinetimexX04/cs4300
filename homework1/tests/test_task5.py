from src import task5

def test_first_three_books():
    result = task5.first_three_books()
    assert len(result) == 3
    assert result[0]["title"] == "Clean Code"

def test_student_database():
    task5.add_student("Taylor", "S345")
    assert task5.get_student("Taylor") == "S345"

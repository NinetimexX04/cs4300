books = [
    {"title": "Clean Code", "author": "Robert Martin"},
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt"},
    {"title": "Think Python", "author": "Allen Downey"},
    {"title": "Fluent Python", "author": "Luciano Ramalho"},
]

def first_three_books():
    return books[:3]

students = {
    "Alex": "S123",
    "Jordan": "S234",
}

def add_student(name, sid):
    students[name] = sid

def get_student(name):
    return students.get(name)

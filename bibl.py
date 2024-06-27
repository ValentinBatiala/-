class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.students = []

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)

    def add_student(self, name, student_id):
        new_student = Student(name, student_id)
        self.students.append(new_student)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

# Демонстрація використання класів
library = Library()
library.add_book('Війна і мир', 'Лев Толстой', '1234567890')
library.add_student('Іван Іваненко', 'S123')

book = library.find_book('1234567890')
student = library.find_student('S123')

if book and student:
    student.borrowed_books.append(book.title)

print(f"Студент {student.name} взяв книгу: {student.borrowed_books[0]}")

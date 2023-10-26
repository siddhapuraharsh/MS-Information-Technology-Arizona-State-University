# Name: Harsh Siddhapura
# Enrollment No.: 1230169813
# Date: 10/23/2023

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = [
    Student('Harsh', 25, 'A'),
    Student('Het', 30, 'B'),
    Student('Dhruv', 28, 'C'),
]

@app.route('/')
def index():
    return render_template('index.ejs', students=students)

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    age = int(request.form['age'])  # Convert the age from string to integer
    grade = request.form['grade']
    students.append(Student(name, age, grade))  # Create a new student and add to the list
    return redirect(url_for('index'))  # Redirect back to the index page

if __name__ == '__main__':
    app.run(debug=True)

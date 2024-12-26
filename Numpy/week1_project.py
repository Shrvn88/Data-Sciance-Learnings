# Student Performance Tracker
# Build a small program to manage and analyze students' test scores using Python classes and NumPy.

import numpy as np

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []
    
    def add_score(self, score):
        self.scores.append(score)
    
    def get_average_score(self):
        if self.scores:
            return np.mean(self.scores)
        else:
            return 0

class Classroom:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def get_class_average(self):
        all_scores = [student.get_average_score() for student in self.students]
        return np.mean(all_scores)
    
    def get_highest_score(self):
        all_scores = np.concatenate([student.scores for student in self.students if student.scores])
        return np.max(all_scores)
    
    def get_lowest_score(self):
        all_scores = np.concatenate([student.scores for student in self.students if student.scores])
        return np.min(all_scores)

if __name__ == "__main__":
    # Create a classroom
    classroom = Classroom()
    
    # Add students
    student1 = Student("Alice")
    student2 = Student("Bob")
    student3 = Student("Charlie")
    
    classroom.add_student(student1)
    classroom.add_student(student2)
    classroom.add_student(student3)
    
    # Add scores for each student
    student1.add_score(85)
    student1.add_score(90)
    student2.add_score(78)
    student2.add_score(82)
    student3.add_score(92)
    student3.add_score(88)
    
    # Calculate and display statistics
    print("Class Average:", classroom.get_class_average())
    print("Highest Score in Class:", classroom.get_highest_score())
    print("Lowest Score in Class:", classroom.get_lowest_score())


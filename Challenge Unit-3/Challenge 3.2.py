"""Implement a function called sort_studentsthat takes a list of student 
objects as input and sorts the list based on their CGPA(Cumulative Grade Point Average) in 
descending order. Each student object has the following attributes: name(string), 
roll_number(string), and cgpa(float). Test the function with different input list of 
students."""


class Student:
  
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number 
    self.cgpa = cgpa

def sort_students(student_list):
  #Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list, 
                           key=lambda student:                            student.cgpa,
                           reverse = True)
  return sorted_students

#Example usage
students = [
    Student("Afsha", "A145", 9.6),
    Student("Rashitha", "A146", 9.5),
    Student("Aarthi", "A147", 9.8),
    Student("Meenachi", "A148", 9.7),
]

sorted_students = sort_students(students)

#Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student. name,student.roll_number, 
student.cgpa))
  
                          
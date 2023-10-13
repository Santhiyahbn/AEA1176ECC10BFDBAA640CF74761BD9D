class student 
def__init__(self, name, roll_number, cgpa): 
self.name=name 
self. roll_number=roll_number
self. cgpa=cgpa 
def sort_students (student_list):
  #sort the list of students in descending order of CGPA 
  sorted_students=sorted(student_list,key=lambda students:student.cgpa,reverse=True) 
return sorted_students 
#Example usage 
students=[student("Hari", "A123", 7.8), student("srikanth"," A123",8.9,student("saumya","A125",9.1,Student("Mahidhar","A125",9.9)]
sorted_students = sort_students (students)
#print the sorted list of students
for students in sorted_students:
  print ("Name:{}, Roll_number:{}, CGPA:{},"format(student.name,student.roll_number,student.cgpa))
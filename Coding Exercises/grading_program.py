student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70 :
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
    
# Using the inbuilt 'items' function
# for key, value in student_scores.items():
#     if value > 90:
#         student_grades[key] = "Outstanding"
#     elif value > 80:
#         student_grades[key] = "Exceeds Expectations"
#     elif value > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
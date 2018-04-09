lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}

alice = {
  "name": "Alice",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}

tyler = {
  "name": "Tyler",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}

students = [lloyd, alice, tyler]

for student in students:
  print student["name"]
  print student["homework"]
  print student["quizzes"]
  print student["tests"]
  
def average(numbers):
  total = sum(numbers)
  total = float(total)
  total = total / len(numbers)
  return total

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  homework = homework * .10
  quizzes = quizzes * .30
  tests = tests * .60
  
def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
  


def get_class_average(class_list):
  results = []
  for student in class_list:
    get_average(student)
    results.append(get_average(student))
    return results
  

print get_letter_grade(get_class_average(students))
  
  
  
  
  
  
  
  
  
  

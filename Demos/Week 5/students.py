#program that initates a small database in the sense that it can:
#insert new students and their mark
#keep continually add students
#print out student`s name and their mark
#averange mark of all students
#find the maximum mark among all students

#all_students = [("Gary", 67), ("Uzma", 82), ("Mihai", 76)]
#print(all_students[0]) #sa cerem primul element din lista

def generate_stds():
  print("Enter the name of a student: ")
  name = input()
  print("Enter the grade: ")
  grade = int(input())
  return name, grade

#print(generate_stds())

def all_stds():
  all_students = []
  while True:
    all_students.append(generate_stds())
    print("To stop adding students, type 0")
    x = input()
    if x == '0':
      break
  return all_students

#print(all_stds())


def print_students(lista):
  for std in lista:
    print(f"{std[0]} earned a greade {std[1]}")

#print(print_students(all_stds()))

def avr_mark(lista):
  total = 0
  for std in lista:
    total += std[1]
  return total/len(lista)

listb = all_stds()
print_students(listb)
print(avr_mark(all_stds()))
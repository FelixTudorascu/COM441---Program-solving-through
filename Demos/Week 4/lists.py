def student():
 print("Enter your name:")
 name = input()
 print("What is your age?")
 age = int(input())
 print("Do you have a dog?")
 dog = input()
 if dog == "yes":
  dog_bool = True
 else:
  dog_bool = False
 return name, age, dog_bool


print(student())


'''
person = ("Felix", 27, False)
print(person)

print(person[1])
if person[2]:
  print("Yay - you have a doggo!")
else:
    print("No dogoo no fun !")

#you cannot modify (mutate) a tuple!

print ("Wich item to print?")
n=int(input())
if n<len(person):
  print(person[n-1])

#you cant modify a tupple
#person[0] = "Philip"
#rint(person)
tuple2 = person + (2000 + "black")
print(tuple2)
print(person)
print(tuple2)
'''



print("How many students to generate?")
n = int(input())
count = 0
all_students = []
while (count<n):
  tuplex = student()
  all_students.append(tuplex)
  count+=1
print(all_students)
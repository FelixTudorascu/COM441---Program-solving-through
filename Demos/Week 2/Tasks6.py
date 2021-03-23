
#We wish to create a program that allows us to specify what type of book is being read by Beep.
#The program should start by asking the user to enter the type of book e.g. adventure.
#If the book is an "adventure" book then the message "I like adventure books!" should be displayed.
#Finally, the program should display "Finished reading book!" .

print("What type of book is this?")
answer = input()
if answer == "adventure":
   print("I like adventure books!")
else: 
    print("Task in progress")
print("Finished reading book!")

#=============================================
#We wish to create a program that allows us to help Beep by suggesting activities for Beep to complete.
#The program should start by asking the user to enter an activity.
#If the activity is "calculate" then the message "Performing calculations..." should be displayed otherwise the message "Performing activity..." should be displayed.
#Finally, the program should display "Activity completed!".

print("Please enter the activity to be performed?")
print("1 - Calculate")
print("2 - Test")
print("3 - Test")

option = int(input())

if option == 1:
  print("Calculate")
  print("Performing calculations...")
  print("Activity completed!")


#------------------------------------------------------------
  print("Please enter the activity to be performed ? (calculate - for example)")
answer = input()
if answer == "calculate":
   print("Performing calculations...")
   print("Activity completed!")
else: 
    print("Task in progress")


#================================================
#We wish to create a program that allows us to help Beep learn to paint.
#The program should start by prompting the user for a directi on to move the paint brush (up, down, left or right).
#The program should then work out in which direction Beep should paint and display a suitable message.

print("Towards which direction should I paint (up, down, left or right?")
direction = input()
if direction == "up":
   print("I am painting in the upward direction!")
elif direction == "down": 
    print("I am painting in the down direction!")
elif direction == "right":
    print("I am painting in the right direction!")
elif direction == "left":
    print("I am painting in the left direction!")

#===================================================================
#The program should start by prompting the user to enter a whole number.
#The program should then work out if the number is even or odd.
#Finally, the program should display a suitable message to indicate if the number is even or odd.
print("Please enter a whole number.")
number = int(input())
if (number%2) == 0:
    print("The number {} is an even number." .format(number))
else: 
    print("The number {} is an odd number." .format(number))
print("Thank you ! Have a lovely day!")
#=============================================================

#The program should start by prompting the user to enter the first number.
#The program should then read in the user’s first number.
#The program should then prompt the user to enter the second number.
#The program should then read in the user’ s second number.
#The program should then decide which of the two numbers is the smallest and display the message "The first number is the smallest!" if the first number is smaller, "The second number is the smallest!" if the second number is smaller or "Both are equal!" if both numbers are equal in value.
print("Please enter the first number:")
num1 = int(input())
print("please enter the second number:")
num2 = int(input())
if num1>num2:
  print("{} is bigger then {}" .format(num1,num2))
elif num1<num2:
  print("{} is smaller then {}" .format(num1,num2))
elif num1 == num2:
  print("{} is equal with {}" .format(num1,num2))
print("Thank you !")

#=======================================================
#The program should ask the user to enter three numbers (one number at a time) and should work out how many of these are even and odd. Finally, the program should display the number of even numbers and odd numbers entered.
#The program should ask the user to enter three numbers (one number at a time) and should work out how many of these are even and odd. Finally,the program should display the number of even numbers and odd numbers entered.

numbers =[]
n = int(input("Enter numbers of elements: \t"))
for i in range (1, 1+n, n<=3):
    allElements = int(input("Enter element: \t"))
    numbers.append(allElements)
even_lst = []
odd_lst = []

for j in numbers:
    if j % 2 == 0:
        even_lst.appen(j)
    else:
        odd_lst.append(j)

print("In even list are {} elements and in the odd list are {} elements" .format(len(even_lst), len(odd_lst)))

#====================
num1 = int(input("Please enter first number\n"))
num2 = int(input("Please enter second number\n"))
num3 = int(input("Please enter third number\n"))

odd_numbers = []
even_numbers = []

if ( num1 % 2 == 0 ):
    even_numbers.append(num1)
elif ( num1 % 2 != 0 ):
    odd_numbers.append(num1)


if ( num2 % 2 == 0 ):
    even_numbers.append(num2)
elif ( num2 % 2 != 0 ):
    odd_numbers.append(num2)


if ( num3 % 2 == 0 ):
    even_numbers.append(num3)
elif ( num3 % 2 != 0 ):
    odd_numbers.append(num3)


print(f"These are the odd numbers: {len(odd_numbers)}")
print(f"These are the even numbers: {len(even_numbers)}")

print(f"Your even numbers are {even_numbers}.")
print(f"Your odd numbers are {odd_numbers}.")

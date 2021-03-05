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

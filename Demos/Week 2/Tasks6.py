
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
   print("I am painting in the upward direction!
")
elif direction == "down": 
    print("I am painting in the down direction!
")
elif direction == "right":
    print("I am painting in the right direction!
")
elif direction == "left":
    print("I am painting in the left direction!
")

#===================================================================

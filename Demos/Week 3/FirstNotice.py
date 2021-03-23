#print("The letter `G` in ASCII table is reprezsentated by {}" .format(ord('G')))

#print("The letter `@` in ASCII table is reprezsentated by {}" .format(hex(ord('@'))))



#defining my own function to calculate area of a triangle
#def calculate_area(h,b):
 # area = 0.5*h*b
#  print(area)
#print("First Height and base of triangle")
#h = float(input())
#b = float(input())
#call for the function
#print("Area is:")
#calculate_area(h,b)



#Paremeter - a value that you plug into a function

def calculate_area(h=10,b=5):
  area = 0.5*h*b
  return area
  

def run():
  x = calculate_area(4)
  x +=1
  print(f"The area of triangle is{x}")

  #call for the function
  run()

  #==========

  phrase = input("Please enter a phrase:\n")

x = 0

while ( x < len(phrase) ):
    print("Bop ", end='')
    x += 1


#===============
# We wish to create a program to help Bop calculate the sum of the first 100 numbers.

# The program should start by displaying the message "Calculating the sum of the first 100 numbers...". 
# The program should then use a while loop to calculate the sum of the first 100 numbers from 1 to 100 (inclusive). Finally, the program should display the message "...Done! The answer is" followed by the answer. 

print("Calculating the sum of the first 100 numbers...")

sum = 0
x = 0

while ( x <= 5 ):
    sum = sum + x
    x+=1

print(sum)



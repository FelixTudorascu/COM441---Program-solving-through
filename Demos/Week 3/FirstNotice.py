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
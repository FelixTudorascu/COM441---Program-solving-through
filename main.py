<<<<<<< HEAD
#program that displays a menu and allows the user to eighter see a nice message, calculate of rectangle or triangle or display a times table for a number.

print("please choose and option from the menu:\n\n1-Nice message\n 2 - Area of rectangle\n 3 - Area of triangle\n 4 - Times table")

option = int(input())

if option == 1:
  print("today will be a good day!")
elif option == 2:
  print("Enter the lenght of the rectangle:")
  l = int(input())
  print("Enter the width of the rectangle:")
  w = int(input())
  area = w*l
  print("The area of this rectangle was {}" .format(area))
elif option == 3:
   print("Enter the base of the triangle:")
   b = float(input())
   print("Enter the height of the triangle:")
   h = float(input())
   area = 0.5*(b*h)
   print("The area of this triangle was {:.2f}" .format(area)) #{:.2} - cate decimale sa ia 
elif option == 4:
  print("What number would you like to see times table for ?")
  n = int(input())
  for i in range(1,11,1):
    #va incepe de la 1, va ajunge la 11 dar nu il va include, si va merge din 1 in 1)
    print("{}x{}={}".format(n,i,n*i))

else:
  print("there is no such option. Go to specsevers!")
=======
print("hello")
>>>>>>> 46ab14c265eac9be932d8ccd05703ba48c8ea6d7

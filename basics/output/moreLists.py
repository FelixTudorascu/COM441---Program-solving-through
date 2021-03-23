def get_fruits():
  fruits = []
  print("Who many fruits would you like to enter?")
  n = int(input())
  for i in range(n):
    print("Type in the next fruit:")
    fruits.append(input())
  #print all items
  print("Your fruits are {} .".format(fruits))

  #print only few items Slicing
  print(f"Sliced list: {fruits[0:5:2]}")

  #print only few items by using negativ Index
  print(f"Negative index: {fruits[-1]}")

  
get_fruits()
def getmefruits():
  fruits = []
  print("How many fruits would you like to enter?")
  n = int(input())
  for i in range(n):
    print("Type in the next fruit: ")
    fruits.append(input())
  return fruits

def get_fruits():
  fruits = ["apple", "kiwi", "banana", "mango", "pineaple", "pear"]
  fruits2=getmefruits()
  print("Your fruits are{}".format(fruits[1]))

  print(f"Slice list: {fruits[0:5]}")

  print(f"Negative index: {fruits[-2:0:-1] }")
  print("The second list is {}".format(fruits2))

get_fruits();
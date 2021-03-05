print("how many times to print the symbol?")
x = int(input())
print("\u5343" *x)
#------------------


print("how many times to print the symbol?")
x = int(input()) #x=3

#i is a counter - it keeps track of how many time we what through the Loop
i = 0

while i < x: #comdition for repeating the code - as i lower then x
  print("\u5343", i) #daca punem i le arata si cate numere sunt
  i = i + 1 #new value of the counter is one more time then previous
print("We left the Loop")
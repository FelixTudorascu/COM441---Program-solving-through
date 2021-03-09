#The program should ask the user to enter three numbers (one number at a time) and should work out how many of these are even and odd. Finally,the program should display the number of even numbers and odd numbers entered.

#print("Please enter a whole number.")
#num1 = int(input("Enter: "))
#print("Please enter a whole number.")
#num2 = int(input("Enter: "))
#print("Please enter a whole number.")
#num3 = int(input("Enter: "))

numbers =[]
n = int(input("Enter numbers of elements: \t"))
for i in range (1, 1+n, n<=3):
    allElements = int(input("Enter element: \t"))
    numbers.append(allElements)
even_lst = []
odd_lst = []

for j in numbers:
    if j % 2 == 0:
        even_lst.append(j)
    else:
        odd_lst.append(j)

print("In even list are {} elements and in the odd list are {} elements" .format(len(even_lst), len(odd_lst)))
#Define an empty list
fruits = []

#Define a list with items

vegetables = ["Carrot", "Peas"]

#Add items to the list

fruits.append("Apple")
fruits.append("Banana")
fruits.append("Tomato")
fruits.append("Pears")

print(fruits)

#Remove an item from a list
fruits.remove("Banana")

print(fruits)

#remove item by index

del fruits[1]
print(fruits)

#insert a value not at the end
fruits.insert(1, "Pineapple")
print(fruits)

#access single element
print(fruits[0])
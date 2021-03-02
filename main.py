print ("Hello")

print("What is your name?")
#Variable is a container, which can store data for us in the memory (string, integer, float, bool)

name = input()
print(type(name))


#---------------

print("what is your age ?")
age = int(input())
print(type(age))

#==================
print("What is your bank balance?")
balance = float(input())
print(type(balance))

#------------------
print("Welcome {} you are said to be {} years old. Your bank balance is {} $.".format(name, age, balance))
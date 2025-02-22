def test_function():
    x = "Test"
    print("Hello "+x)

test_function()

a = {"name" : "John", "age" : 36}
print(type(a))

b = ["apple", "banana", "cherry"]	
print(type(b))

c = ("apple", "banana", "cherry")	
print(type(c))

z = 1j   # complex


#List
mylist = ["apple", "banana", "cherry"]
thislist = ["apple", "banana", "cherry"]
print(thislist)
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
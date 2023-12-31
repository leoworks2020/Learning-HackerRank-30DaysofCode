# Hacker Rank 30 Days of Code Challenges.

# Here in this project each Day Challenge will be stored in a separate .py file

# Train for classes
print(f'Classes: Mycar...')
class Mycar:
    def __init__(self, vendor, model):
        self.vendor = vendor
        self.model = model


car1 = Mycar("Honda", "Fit")
print(car1.vendor)
print(car1.model)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)



# Iterate with strings
print(f'Iterating with strings...')
string = "abcdef"
for w in range(len(string)):
    print(string[w])

# Dictionary
print('Dictionary: Input a integer:')
n=int(input())
dict={}
for i in range(n):
    print("Please inform dictionary key and value separated by space")
    key,value=input().split()
    dict.update({key:value})
    while True :
        try:
            print("Plese inform key to be found in Dict")
            s=input()
            if(s in dict):
                print(s+"="+dict[s])
            elif s == "exit":
                break
            else:
                print("Not found")
        except:
            break

# Zip Function
list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = zip(list_1, list_2)
print(list_3)

# Class and Reverse list
print('Class and Reverse List...')
class MyClass:
    def __init__(self, data: tuple or list):
        self.data = data

    def my_method(self):
        if isinstance(self.data, tuple):
            return self.data[1:][::-1]
        else:
            return self.data[::-3]

words = ['apple', 'banana', 'cherry']
obj = MyClass(words)

print(obj.my_method())


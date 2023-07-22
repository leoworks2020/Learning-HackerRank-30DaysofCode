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
n=int(input())
dict={}
for i in range(n):
    key,value=input().split()
    dict.update({key:value})
    while True :
        try:
            s=input()
            if(s in dict):
                print(s+"="+dict[s])
            else:
                print("Not found")
        except:
            break
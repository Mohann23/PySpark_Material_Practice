'''
If conditions
'''

'''
#1. We are checking the marks
marks = int(input("Enter marks between 0 to 100 :"))

if marks >= 0 and marks <= 100:   # 0 to 100
    if marks >= 35:  # True
        print(marks, "Result : PASS")
    else:
        print(marks,"Result : FAIL")
else:
    print("Please enter valid marks")
'''

'''
#2.
marks = int(input("Enter marks :"))
if marks < 0 or marks > 100:
    print("Please enter valid marks between 0 to 100")
else:
    if marks >= 60:
        print("Result : FIRST CLASS")
        if marks == 100:
            print("-----SUPER..Congratulations-----")
        elif marks >= 90:
            print("----GOOD..Congratulations-------")
    elif marks >= 50 and marks < 60:
        print("Result: SECOND CLASS")
    elif marks >= 35 and marks < 50:
        print("Result: THIRD CLASS")
    else:
        print("Result: FAIL")
        if marks == 0:
            print("--------DOUBLE SUPER----------")

'''
'''
#3.
x = float(input(" Enter the amount :"))
if x >= 1000:
    print(" your booking confirmed in the AC bus ")
elif x >= 500:
    print(" your booking confirmed in the Super Luxury bus ")
elif x >= 200:
    print(" your booking confirmed in the Express Bus ")
else:
    print(" your booking confirmed in Yerra Bus ")
'''

'''
list1=[1,2,3,4,5,6,7,8,9]
i=int(input("Enter a number you want to search:  "))
if i in list1:
    print("Present sir!!!")
else:
    print("Absent sir!!!")
'''

'''
inp_num = input("Enter a number: ")

#Convert string to int
inp_num = int(inp_num)

if inp_num == 0:
  print(inp_num, "is Even")
elif inp_num%2==0:
  print(inp_num, "is Even")
else:
  print(inp_num, "is Odd")
'''

'''
# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")
'''



'''
In this program, 
we check if the number is positive or
negative or zero and 
display an appropriate message
'''

'''
num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
'''

'''

a = 5
if (a <10):
    print('5 is less than 10')

print('Statement after if statement')
'''










'''
For loop
'''


'''
# String with for loop
for x in 'Anchala Mohan Narayana':
    print("Char : ", x)
'''

'''
for x in 'Anchala Mohan Narayana':
    print("Character : ", x)
'''

'''
# List with for loop
for val in [1, 2.5, True, 'Mohan', 5.0, False, 7]:
    print("List data :", val)

for val in [1, 2, 3, 4, 5, 6, 7]:
    print("List data :", val)
'''

'''
# Tuple with for loop
for val in (1, 2, 3, 4, 5, 6, 7):
    print("Tuple data :", val)

'''

'''
# Dictionary with for loops
e_data = {'eid': 100.50, 'name': 'Mohan Narayana', 'sal': True}
print(e_data)
for i in e_data:
    print("Dict data :", i)
print("--------------------------------")
for x in e_data.keys():
    print("Dict key :", x)
print("--------------------------------")
for val in e_data.values():
    print("Dict val :", val)

for x,y in e_data.items():
    print(x,y)
'''

'''
# set with for loop
set1 = {1, 2, 3, 4, 5, 6}
for val in set1:
    print("Set value : ", val)
'''

'''
#Print even numbers
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1

num = 2
while num <= 100:
    if num % 2 == 0 and num % 4 == 0:
        print(num)
    num += 1
'''


'''
#Print odd numbers

# Print odd numbers betweeen 10 to 20
num = 10
while num <= 20:
    if num % 2 != 0:
        print(num)
    num += 1
    
'''

'''
# Print numbers between 500 to 1000 and divisible by 5

print("--Numbers divisible  with 5------")
num = 500
while num <= 600:
    if num % 5 == 0:
        print(num)
    num += 1

'''

'''
# Print numbers between 500 to 1000. It should be divisible by 5 and divisible by 8
print("--Numbers divisible  with 5 and 8------")
num = 500
while num <= 600:
    if num % 5 == 0 and num % 8 == 0:
        print(num)
    num += 1
'''

'''
# Print numbers between 500 to 1000. It should be divisible by 5 or divisible by 9
print("--Numbers divisible  with 5 or 9------")
num = 500
while num <= 600:
    if num % 5 == 0 or num % 9 == 0:
        print(num)
    num += 1

'''

'''
Functions
'''

'''
#1. Positional arguments

def sum(n1, n2, n3): 
    print("In sum method : with vals :", n1, n2, n3)
    res = n1 + n2 + n3
    print("Sum is : ", res)

sum(10, 20, 30)
'''
'''
#2. Default arguments
def sum(n1, n2, n3 = 1000):
    res = n1 + n2 + n3
    print("Sum is : ", res)

sum(10, 20)      # n3 = 1000
sum(10, 20, 30) 
'''

'''
def sum(n1, n2 = 500, n3 = 1000):
    res = n1 + n2 + n3
    return res

print("One argument     :", sum(10))   # 1510
print("Two argument     :", sum(10, 20))  # 1030
print("Three argument   :", sum(10, 20, 30))  # 60
#print("Zero argument    :",sum())
# print("Extra arguments  :",sum(10,20,30,40))
'''

'''
def sum(n1 = 100, n2 = 500, n3 = 1000):
    res = n1 + n2 + n3
    return res

print("Zero argument     :", sum())
print("One argument     :", sum(10))
print("Two argument     :", sum(10, 20))
print("Three argument   :", sum(10, 20, 30))
'''

'''
def sum(n2, n1=1, n3=1000):
    res = n1 + n2 + n3
    print("Sum is : ",res)
'''











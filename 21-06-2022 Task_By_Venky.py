'''
Introduction to python is no need we have gone through that many times.

Python is a general-purpose language, object orientated programing language.

Python is platform independent language. By using python we can use python for game, AI, ML, Date science, websites, etc.

Main advantage of python is It is dynamically typed programming language


'''


'''
Variables:
--------
x = 10

x is the variable 
=  is the assignment operator
10 is the value

They are two types of variables:
1. Local variable
2. Global variable

1. Local variables:
    variables that are defined inside the function and can be used in that function only.
    
2. Global variables:
    Variables that are defined outside the function and can be used in other functions also.
    
We can define a Global variable inside a function by using a keyword called 'global'

'''


'''
print("Arithmetic operators")
x=20
y=10
print("sum",x+y)
print("sub",x-y)
print("mul",x*y)
print("div",x/y)
print("Power",x**y)
print("Floor Division",x//y)
print("Modules",x%y)
print()
'''

'''
print("Relational Operators!!!")
x=20
y=10
print()
print(x==y)
print(x!=y)
print(x<y)
print(x>y)
print(x>=y)
print(x<=y)
print()
'''


'''
print("Assignment Operators")
x=20
y=10
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
'''


'''
print("Logical operators!!!!!!")
a=10
print(a>9 or a>50)
print(a<20 and a>9)
'''


'''
print("Membership Operators!!!!!")
a=[1,2,3,4,5]
print(1 in a)
print(6 not in a)
'''

'''
print("Identity Operator!!")
a=10
b=10
print(a is b)
print(a is not b)
'''

'''
list1 = [110, 23.5, True, 'Mohan', [1,2,3], (1,2), {1:10,2:20}, {1,2,3}]
print("List1 : ", id(list1))
print("Index 3rd  : ", id(list1[3]))
print("Index : ", id(list1[3][1]))
print("Slice : ", list1[3][1:3])

# Tuple
print("------------TUPLE------------")

tup1 = (110, 23.5, True, 'Mohan', [1,2,3], (1,2), {1:10,2:20}, {1,2,3})
print("Tuple : ", tup1)
print("Index : ", tup1[3])
print("Index : ", id(tup1[3][1]) , id(tup1[3][-1]))


print("------------DICTIONARY------------")

e_data = {'eid': 100,
          'name': 'Mohan Narayana',
          'sal': 15000,
          'loc': 'Bangalore',
          'gender': 'Male'
          }

print("Dict data : ", e_data)
print("Dict data : ", e_data['name'])
print("Dict data : ", e_data['sal'])


print("------------SET------------")

set1 = {1, 2, 3, 4, 5, 6}
print("Set1 : ", set1)

'''




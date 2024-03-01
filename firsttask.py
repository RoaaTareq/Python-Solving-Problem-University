"""
Check if a number is odd or even. 
Take the number 5 for example. 
If you want to check, 
you must divide it by 2. 
If the result is 0, it's even; otherwise, it's odd
"""
x=5,
if 5 /2 == 0 :
    print('even')
else:
    print('odd')


"""
program sum all num on list

"""
mylist = [1, 2, 3, 4, 5, 6]
total = 0
for x in mylist:
    total += x
    print(total) 


"""
 the Factorial of a Number
 for example number is 5 
 5!=5*4*3*2*1
 mean n!=(n-1)* ...
"""

def factorial(num):
    if num == 1 or num ==0:
       return 1 
    else:
        num *(num*1) 
number=5 

print('Factorail number ', factorial(number))

"""
reverse tuple
"""
list=("apple","banana","cherry")
new_tuple=list[::-1]
print(new_tuple)

"""
Find max number on list

"""
list=[50,20,40,100,90]
max=list[0]
for x in list[1:]:
    if x >max :
        max=x
print(max)

"""
A palindrome is a string that reads the same forwards and backwards
"""
txt = 'mam'

x = txt[::-1]

if txt == x:
    print('Palindrome string')
else:
    print('Not a Palindrome string')

"""
merge two list on single list
"""
list_one=[1,2,3,4]
list_two=[5,6,7,8]
list_one.extend(list_two)
print(list_one)
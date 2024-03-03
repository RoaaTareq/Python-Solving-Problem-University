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

"""
leap year
"""
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('It is a leap year')
else:
    print('It is not a leap year')

"""
find largest element in list using loop
"""

my_list = [50, 60, 80, 90, 70, 45]
max_value = my_list[0]

for x in my_list[1:]:
    if x > max_value:
        max_value = x

print("The maximum value is:", max_value)

"""
Union between two list python
"""
Group_A = {"Roaa", "Roua", "Rose"}
Group_B = {"Rami", "Rose", "Roua"}
my_list = []

for A in Group_A:
    if A not in my_list:
        my_list.append(A)

for B in Group_B:
    if B not in my_list:
        my_list.append(B)

print(my_list)

    
"""
find sum of digits of a given number
for example 1223 = 1+2+2+3 =5
"""
number = input("Enter Number: ")
total_sum = 0

for i in number:
    total_sum += int(i)

print("Sum of digits:", total_sum)

"""
Sort list of  tuples based second element
"""
list=(20,40,50,60)

"""
Remove duplicate item on list
"""
my_list = [50, 60, 20, 100, 50] 

unique_list = []


for item in my_list:
    
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)  # Output: [50, 60, 20, 100]




##################
from io import SEEK_CUR
import itertools
import re
import random  # This section You  dont need it now "Import Libraries section"
import math
##################

#Declaration of variables#

first_number = 10
scend_numb = 3.01
addition = first_number+scend_numb
print(addition)

# id:giving the memory location :
print(id(first_number), id(scend_numb))
# type:giving the type of the variable:
print(type(first_number), type(scend_numb))
a = 10
b = 10
print(id(a), id(b))  # have the same memory location
# Datatypes:#
# 1 int :
num1 = 100
print(type(num1))
# 2 floar:
num2 = 15.4
print(type(num2))
# 3 str :
num3 = "python"
print(type(num3))
num4 = "'python'samplestring"
print(num4, type(num4))
# 4 list :
List = [10, 23, 24, 2, 525, "python"]
print(List)
List.append("django")  # adding another elemts to the list
print(List)
# 5 tuple:
t = (10, 20, 30)  # cannot add other elements or delete or change
# 6 Dict:
d = {"name": "abc", "email": "abc@gmail.com"}
# 7 set:
s = {10, 20, 30}
# 8 bool:true false
# 9 complex : 4+3j

# Operators in python #
# 1 arithmetic operators: +,-,*,/,//,%,**
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1 % num2)
print(num1**num2)
# 2 comparison operators: <,>,<=,>=,==,!=
# 3 identity operators: is is not
l = [100, 200, 300]
l2 = [100, 200, 300]
print(l == l2)
print(l is l2)
print(l is not l2)
# 4 assignement orperators: =,+=,-=,*=
num1 += 5
print(num1)
# 5 bitwise operators:^,&,>>,|,<<
num6 = 2
num5 = 4
print(bin(num6))
print(num6 & num5)
print(num6 | num5)
print(num6 << num5)
print(num6 >> num5)
# 6 logical operators: and,or,not

# 7 membership operators: in,not in
l = [10, 20, 30, 40, 50]
print(30 in l)
print(300 in l)      # this will return True or False "checking if there is element on the list or not "
## conditional statments ##
# if:
# if [condition]:
#    staments
# else:
#   staments
# elif:
#    staments
num7 = 100
num8 = 200
if num7 > num8:
    print("num7 is greater than num8")
elif num8 > num7:
    print("num8 is greater than num7")
else:
    print("num8 is equale num7")
# loops in python:
# 1 for loop:
list2 = [10, 20, 30, 40, 50]
for value in list2:
    print(value)

if value == 10 in range(10, 50, 10):
    print("im 10 ")
else:
    print("im not 10 ")
sum = 0
for value in list2:
    sum = sum+value
    print(sum)
for value in range(10, 100):
    print(value)
sum = 0
for value in range(1, 21):
    sum = sum+value
print(sum)
# break
# continue
# enumerate
list3 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
key = 20
for value in list3:
    if value == key:
        print("element found")
        break
    else:
        continue
else:
    print("elemet not found")
# enumerate is giving the index and the value if u want :
for index, value in enumerate(list3):
    if value == key:
        print("element found at index", index)
        break
    else:
        pass
else:
    print("elemet not found")
# while loop in python:
count = 1
sum2 = 0

while count <= 20:
    sum2 = sum2+count
    count = count+1
print(sum2)


# String:
# 1 String are immutable
s = "python simple"
print(type(s))
s1 = "python"
print(id(s1))
s2 = "Java "
print(id(s2))
# String is ordered data structure -indexing
# Indexing:
s = "python simple string"
print(s[0])
# Slicing:
print(s[0:5])
print(s[7:])
print(s[:6])
# Stride:
print(s[::2])
help(str)
print(dir(str))
# format
num1 = 100
num2 = 200
print("Value of num1 is ", num1, "the value of num2 is ", num2)
print("Value of num1 is {}value of num2 {}".format(num1, num2))
s = "python simple string"
# fonctions:
# capitalize:
s2 = s.capitalize()
print(s1)
# upper:
print(s.upper())
# lower:
print(s.lower())
# title:
print(s.title())
# Making sure +true or false:
print(s.istitle())

# split:separate elements on string
s = "HTML,CSSS,PYTHON"
L = s.split(",")
print(L)
# Join: joining some list with another list with this function
s1 = (" ").join(L)
print(s1)
#Maktrans, translate
s1 = "abcd"
s2 = "1234"
s3 = "Python Sample string abcd"
table = str.maketrans(s1, s2)
resulut = s3.translate(table)
print(resulut)
# index , find , rfind function
s = "HTML,CSS,PYTHON"
print("python" in s)  # searching about the element inside the list
print(s.index("PYTHON"))
print(s.find("python"))  # if it is false it will put out -1
s = "       This is sample string       "
s = s.strip(" ")  # Strip just make spaces disappear
print(s1)
print(s.strip("*"))  # replacing the spaces with *
# center
s1 = s.center(20, "*")  # adding 20 of *
print(s1)
# replace
s = "html,css,python,html"
s1 = s.replace("html", "HTML5")
print(s1)


# List
# 1 Lists are mutable - add and delete
# 2 ordered indexing and sciling
# 3 hetrogeneous datatype

L = [10, 20, 30, 40]
print(L, type(L))
# indexing and slacing :
print(L[-1])  # indexing
print(L[-1], [1])
print(L[::-1]
      )
l = [100, 200, 300, 400, 500]
for value in l:
    print(value)

for value in l[::2]:
    print(value)

print(id(l))

l.append(600)  # adding an element to the list
print(id(l))
# extend is adding a lot of elements to the list
l.extend([500, 600, 700, 800])
print(l)
l.insert(1, 1000)  # add at the first place an element

# update elements on a list :
l = [10, 20, 30, 40, 50]
l[2] = 300
print(l)
# Delete elements on a list :
# pop
r = l.pop(2)
print(l)  # Delete the last element by defining the index of the element
print(l, r) # Delete the last element and show the elements that were deleted
# remove
# will remove the element from the list by saying what is the place of the element :0,1,2,3...
l.remove(20)
print(l)
# clear
l.clear()  # Delete all the elements on the list by making the element  :()
print(l)
# Del
del l  # delete completely the list from memory
print(l)
# sort
l = [50, 40, 30, 20, 10]
l.sort()
print(l.sort())
print(l[::-1])  # to reverse the list
# reverse
l.reverse()  # means that the list will be reversed
l3 = sorted(l)  # means that l3 will be equal to l they will have the same elements
print(l3)
print(l.count(30))  # counting how much there is elements "x"on the list
# making the same element at the list how much you want :
l = [0.1]
print(l * 10)


# Tupels DataTYpe "dictionary":
# 1 immutable datastructure
# 2 orderd indexing and slicing
t = (20, 10, 30, 40)
print(t, type(t))
print(t[0])

# converting list to tuple
l = [10, 20, 30, 40, 50]
t = tuple(l)
print(t)

# dictionary datatype:
d = {"emp_id": 101, "name": "abc", "email": "abc@gmail.com"}
# 1 mutable
# 2 unordered
# 3 key should be unique
# 4 keys should be immutable int float str tuple
print(d)

# adding an element to the dictionarry
d["contact_no"] = 123456789
print(d)
# Searching about a value we need to have the key like :
print(d["emp_id"])
# "get" This means that the key does not exist and will show it
print(d.get("age", "key does not exist"))
# If not exit will show non if it will return the value"show the value"
print(d.setdefault("emp_id"))
for x in d:
    print(x)  # This will show the key return "shows the key"
for key in d:
    print(key, d[key])  # This will show the value of the key
# making dictionary with a loop for {1:1,2:4.....} this how:
d = {}
for value in range(1, 11):
    d[value] = value * value
print(d)
# Show the keys on the dictionary: "key"
print(d.key())
# Show the value of the keys :"values"
print(d.values())
# Show the key and the value at the same time with this function:"items"
print(d.items())
# If you wanna show the d like tuple use this :
for t in d.items:
    print(t)

# Update and delete operations in dictionary:
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 9, 16, 25]
d = dict(zip(l1, l2))  # This will combine it to the dictionary
print(d)
# making a list to dictionary and the value on the list will return keys on dictionary look this method :
l = [1, 2, 3, 4, 5]
d = dict.fromkeys(l)
print(d)
# modify dictionary:
d1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
d2 = {6: 36, 7: 49}
d1.update(d2)
print(d1)
# Delete a key or value in dictionary :"pop","popitem","clear","del"
r = d1.pop(2)  # this will delet the key value
r = d1.popitem()  # will delete the key and the value and show them at the output
print(d1, r)
r = d1.clear()  # will delete all the values and keys inside the dictionary
del d1  # this will delete the whole dictionary from memory

# Set DataType |add-Update-Delere operations:
# sets:
# 1 were you Shiite or SunniSets are mutable
# 2 All the elements should be unique
# 3 Immutable elements in the set - int float tuple str
# 4 Unordred

s = {10, 20, 30, 40}
print(s, type(s))

# Add an element to the set :"add"
s = {100, 200, 300, 400}
s.add(500)
# union of to sets :"union"
s1 = {10, 20, 30, 40, 50, 60}
s2 = {40, 50, 60, 70, 80, 90}
s3 = s1.union(s2)
print(s3)
# intersection of a sets:"intersection"
s3 = s1.intersection(s2)
# difference of sets :"difference"
s3 = s1.difference(s2)
print(s3)
# symmetric difference of sets :"symmetric_difference"
s3 = s1.symmetric_difference(s2)
print(s3)
# Updating elements on original sets :
s1.update(s2)
print(s1)
s1.intersection_update(s2)  # its intersection update same to difference:
s1.difference_update(s2)
s1.symmetric_difference_update(s2)
# if you wanna see if there elements on set1  in set2 use this method:
s1 = {100, 200, 300, 400, 500}
s2 = {100, 200, 300}
print(s2.issubset(s1))
print(s1.issuperset(s2))
# Converting a list to set:"set"
l = [100, 200, 300, 400]
s = set(l)  # this function will convert it to set
print(s)
# example :
l1 = [100, 200, 300, 400, 500]
l2 = [50, 100, 150, 200, 250, 300, 400, 450, 500]
s1 = set(l1)
s2 = set(l2)
s3 = s1.union(s2)
print(s3)

l3 = list(s3)
print(s3)
l3.sort()
l3 = sorted(s3)
# Delete opirations for set datatype :"pop","remove","discard","clear","del"
s = {1, 2, 3, 4, 5, 6, 7}
# pop:
r = s.pop()  # dont specfy
print(s, r)
# remove:
s.remove(1000)  # will remove the element but if doesnt exist will show an error
# discard:
s.discard(1)  # will remove the element and if not exist will not show an error
# clear:
s.clear()  # this will delet all elements inside the set
# del
del s  # this will delete all the sets from memory


# Math and Random Modules:

# Some of math functions operators before :
l = [100, 200, 300, 400]
print(sum(l))  # the sum of the elements on the list or any other datatype
# find a max element:
print(max(l))
# find min element :
print(min(l))
# round a num:
num = 25.555
print(round(num))
# dir:
print(dir(__builtins__))  # the list of all functions
help(__builtins__)

# To work on math problems and functions u need to import first :
# if you want to use mathematical functionalities, you must import the math package first:
#import math

l = [0.1]*10
print(l)
print(sum(l))
print(math.fsum(l))
num1 = 15.55515559

print(math.floor(15.55515559), math.ceil(15.55515559))
# floor is used to make the num :"15" and the ciel :"16"
print(math.sqrt(10))
# factorial:
print(math.factorial(num))
# modf() function is an inbuilt function in Python that returns the fractional and integer parts of the number in a two-item tuple
num1 = 45.5556
print(math.modf(num1))
d, i = math.modf(num1)
print(d, i)
# pow : The math. pow() method returns the value of x raised to power y. If x is negative and y is not an integer, it returns a ValueError. This method converts both arguments into a float.
print(math.pow(10, 2))
# log function:
print(math.log(10))
print(math.log10(2))  # .....
# sin function:
print(math.sin(0))
# cos function:
print(math.cos(1))
# convert to radian :"radians" function:
print(math.cos(math.radians(30)))
# tan function
print(math.tan(math.radians(30)))
print(math.factorial(3))
# if u wanna see the all functions on math library :
help(math)
print(dir(math))

# Randoom library:
#import random

# generate random number: function "random()"
print(random.random())

# generate one of randome value at list or ....with function:"choic()"
l = [1, 2, 3, 4, 5, 6]  # like dice game
print(random.choice(l))
# generate int number spesified with randint() function:
print(random.randint(10, 100))
# randring
print(random.randrange(10, 100))
# generate float random numbers with uniform() function:
print(random.uniform(10, 2))  # this will give random float numbers


# Starting with user Defined functions
# The reasons why we use theme :
# 1 Code reuse :
# 2 modularity:

s = "python,html,css"
print(s.index("html"))  # this function will give us the index of Html
# func call:
# func def: means function definistion
# reverse :
s = "python"
s1 = "01000110101"
# this will give use error because we need define it just delet the "" and try it u will see error
resulte = "value_reverse"(s)


def value_reverse(value):
    reverse = value[::-1]
    print(reverse)  # this how u can reverse :) by making function
    return reverse   # not all functions need return


resulte = value_reverse(s, s1)
#Note this will just work on str for list or others will not but we have a solution for it :

def value_reverse(value):
    if type(value) == list or type(value) == str:
        reverse = value[::-1]
    else:
        temp = str(value)
        reverse = temp[::-1]
    return reverse

# 1 Positional argument:

# searching an element on a list by def function :


def linear_search(l, key):
    for value in l:
        if key == value:
            return True
    else:
        return False


l = [100, 200, 300, 400, 500]
key = 400
result = linear_search(l, key)

# 2 Default argument:

# Lets try make password generator :
# the password must have:
# 8 char
# 1 upper
# 1 lower
# 1 special char
# 5 digits
# and use this functions :
# ord
print(ord("a"))  # this will return 97     (97 to 122)
# chr
print(chr(97))  # this will return a       (65 to 90)

# first we need the random library so we need :
#import random
 

def gen_password():
    l = ["@", "#", "%", "&"]  # this list we will use it for sepcial char
    upper = chr(random.randint(65, 90))
    lower = chr(random.randint(97, 122))
    special_char = random.choice(l)
    digit = random.randint(10000, 99999)
    # we convert digit to str  so we don't have an error
    password = upper + lower + special_char + str(digit)
    return password


result = gen_password()  # You can specify how much char u need putting inside () like: (5)
print(result)


# 3 Key argument:

# function that validate username and password :

def validate(username, password):
    if username == "ABC" and password == "abc@123":
        print("valid password")
    else:
        print("Invalid password")


validate("ABC", "Abc@123")
# we can too :
validate(password="Abc@123", username="ABC")

# 4 Variable length positional args:

l = [100, 200, 300, 400]
l.append(500)  # we can just add one element to the list with the function append ()
print(l)

# we will make a function that add a lot of elements at the same time to a list :


def add_value(*args):
    l = []
    for value in args:
        l.append(value)
    return l


result = add_value(100, 200, 300, 400, 500, 600, 700, 900)
print(result)

# Vaiable elength keyword:

# we will write a function :
# name,email,contact,dob
# get_details :


# if we make ** the return will be type(dictionary) not like tuple with one *
def get_details(**kwargs):
    print(kwargs)


get_details(name="ABC", email="abc@gmail.com",
            contact="675327872", dob="10-07-2002")

# Recursive Function :

# making factorial function :


def factorial():
    if num == 1:
        return 1
    else:
        return num * factorial(num1-1)


num1 = 5
result = factorial(num1)
print(result)

# Binary search :


def binary_search(l, key):
    mid = len(l)//2

    if l[mid] == key:
        return True
    elif key < l[mid]:
        return binary_search(l[:mid], key)
    else:
        return binary_search(l[mid+1], key)


l = [100, 200, 300, 400, 500, 600, 700, 800, 900]
result = binary_search(l, key)
print(result)

# Python Modules and Packages :


print(__name__)

if (__name__) == (__package__):
    # this code so we can import this function to another file .
    l = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    result = binary_search(l, key)
    print(result)

# to create a description of your function in help one:
# you need go to the top of the file and :
# """
#   The disctription
# """
# and in fuction its the same go to function under def  than  do the same """
# and if you wanna add this to package you need :__init__.py , on the bottom of the file


#   Introduction to RE Module |Regex Meta-Characters

# import re : we do need this to use the library re
# 0 any char
# [a-az-Az-Z] - char class a or b or c .... or zA or B or .... Z
# [0-9] - digit class 0 or 1 or 2 .... or 9
# + at least one [a-z]
# * -Zero or more
# ^ - start of the string
# $ - end of the string
# ? - optunal
# [a-z] {2,4} specify
# compile:
s = "ABCDE1234A"
r = re.compile("[A-Z]{5}[0-9]{4}[A-z]")
l = re.findall(r, s)
print(l)

# check if I have 10 digits in there:
s = "8123456789"
r = re.compile("^[6-9]{1}[1-9]{9}$")
l = re.findall(r, s)
print(l)

s = "12-05-2018"
r = re.compile("^[0-9]{2}[0-9]{2}[0-9]{4}$")
m = re.search(r, s)
if m:
    print(m.group())
else:
    print("pattern not found")

# we can also :

r = re.compile("^(?p<day>[0-9]{2})-(?p<month>[0-9]{2})-(?p<year>[0-9]{4})$")
m = re.search(r, s)
if m:
    print(m.group())
else:
    print("pattern not found")
###
s = "+91 8123456789"
r = re.compile("(+91)?\s[6-9][0-9]{9}")
m = re.search(r, s)
if m:
    print(m.group())
else:
    print("pattern not found")

##### Fonctional Programing #####

# List comprehestion -Dict comprehention:
# norman one #
l = [100, 200, 300, 400, 500]
l2 = []

for value in l:
    l2.append(value*value)

print(l2)
####

l2 = [value*value for value in l]
# check if its visible by /2
l = [10, 20, 35, 40, 55, 60, 75]
l = [value for value in l if value % 2 == 0]


l = ['abcd', 'abc', 'zzzzzz']
l2 = [len(value)for value in l]
print(l2)

# Functional Programing|Map - Filter -Lambda:

l = [10, 20, 30, 40]
# we wanna make each element to be square  so we use :
# Map:


def sqr(num1):  # we need first define the square function
    return num**2


# then:
# we need to convert all this to a list so we can print it
result = list(map(sqr, l))
print(result)
# l1 + l2
l1 = [100, 200, 300, 400, 500]
l2 = [10, 20, 30, 40, 50]


def add(num1, num2):
    return num1+num2


result = list(map(add, l1, l2))

# if you wanna filter an element on the list we use this function:
# filter:
l = [100, 115, 120, 125, 130, 140]


def check_num(num1):
    if num1 % 2 == 0:
        return True
    else:
        return False


result = list(filter(check_num, l))


# lambda
l = [10, 20, 30, 40, 50]
result = list(map(lambda num1: num1**2, l))
# its like the first one but in different way:
result = list(filter(lambda num: num % 2 == 0, l))
# another thing we need use lamdbda for
d = {1: 50, 2: 40, 3: 30, 4: 20, 5: 10}
l = sorted(d.items(), key=lambda x: x[1])  # sort it as the baase of value
print(l)

# Function iterators generator functions:


def printVal(l):
    for value in l:
        print(value)


l = [10, 20, 30, 40, 50, 60]
printVal(l)


def fibo():
    first_num = 0  # making fibo function
    second_num = 1
    while(True):
        next_val = first_num+second_num
        yield next_val   # generate of funcion
        first_num, second_num = second_num, next_val


g = fibo()
# This will return and generate the first number untile the end .....
print(next(g))

# ITERATORS :
l = [100, 200, 300, 400, 500]
i = iter(l)
print(i)  # will return that this is iterator
print(next(i))  # will return the first number
print(next(i))  # will return the second number
# the best tip to return all the values at the list fast :
for value in i:
    print(value)

l = [10, 20, 30, 40, 50]
l = [100, 200, 300, 400, 500]
l3 = [1000, 2000, 3000, 4000, 5000]
# Chain will make the lists a lot of lists to iterators
i = itertools.chain(l1, l2, l3)
print(i)
l = [10, 20, 30, 40, 50]
# Make a itretors :
count = 0
# you can use itertools.repeat to rpeat the itrators
for value in itertools.cycle(l):
    if count < 20:
        print(value)
    else:
        break
    count += 1
# creat multiple objects :
i = iter(l)
t = itertools.tree(i, 5)
print(t)
for value in t[0]:
    print(value)
# Else other functions on this library:
range(10, 50)
count = 0
for value in itertools.count():
    if count > 20:
        break
    else:
        print(value)
    count += 1

l = [1, 2, 3]
print(list(itertools.permutations))
print(list(itertools.combinations(l, 2)))


# File Operation |JSON,XML Parsing

# File Operation:
# To open a file text you need use this function:
open("input.text")  # input.txt is just a name of a file so you can name it like you want but be sure you use the file name correct at this functions and module
# And Python have some modes :
# r => read
# r+
# w => write
# w+
# a => append
# a+
# example:
open("input.txt", "r")


# Read Mode
# r => read:

fp = open("input.txt", "r")
content = fp.read()
print(content)
# you can also define number of charracteres you wanna read :
content = fp.read(10)  # this will read just 10 char
print(content)
print(content[:5])     # print just first 5 lines 

content= fp.readline()
print(content) # print some lines ...

for x in fp :
    print(x) # This is another methode to read an text file

# Write Mode:
# w => write

fp= open("input2.txt","w")
print(fp.tell())
fp.write("write this line to the file  ") #this function will add this line to the text file .
print(fp.tell())
content= fp.read()
print(fp.tell())
print(content)
# tell => current fp position
# change (offset,position) => to change the fp position 
# offset => number of char
# position => 0= start of the file , 1 => current postion ,2 => end of the file
# seek(15,0) # change the fp by 15 char from the start  
fp.seek(0,0)

# r+ => read + write 




# Parsing Jason files Using Python: go to json.py
# Json Object   dict{"key":"value"}
# numbers 10 10.55   int float 
# " "     "" """ 
#array[10,"string"]    list on python 

# go to json_input.py file and check there













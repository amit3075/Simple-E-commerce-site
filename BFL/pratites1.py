"""grades = [{'name': 'abc','final': 90},
           {'name': 'bc','final': 92},
           {'name': 'dec','final': 93},
           {'name': 'sdfc','final': 56}]
#sort the grade based on final marks 
print(sorted(grades,key = lambda x: x['final'],reverse=True))#reverse parameter try on name to
#iterable = can be able to indexing and using loop
#iterable = can be rember the own states and do't indexing like generator
#iteration =
#map applies a function to all the item of iterable 
#synatx: map(function_to_appy,iterable)
item = list()
item = [1,24,5,6]
squared = list(map(lambda x : x**2 , item))
print(squared)
item = list()
item = [1,2,3,5]
sqaured = list()
for x in item:
    sqaured.append(x**2)
    print(sqaured)

item =list()
item =[1,2,3,4,5]
def squared(num):
    return num**2
map(squared,item)
print(list(map(squared,item)))

item = list()
item =[1,2,34,5]
def multiply(x):
    return (x*x)
def add(x):
    return(x+x)
funcs = [multiply,add]
for i in range(5):
    value = list(map(lambda i :funcs,item))
    print(value)
num_list = range(-5,5)
less_than_zero = list(filter(lambda x:x>0, num_list))
print(less_than_zero)
# function example
letter =['a','b','c','d','e']
letter = ['x''a','e','i','o','u','a','b','c','d','e']
def filter_vowels(letter):
    vowels = ['a','e','i','o','u']
    return True if letter in vowels else False
filter_vowels= tuple(filter(filter_vowels ,letter))
print(filter_vowels) 

product = 1
list =[1,2,3,4]
for num in list:
    product = product *num
#pythonic way
from functools import reduce
product = reduce((lambda x,y:x*y),[1,2,3,4])
print(product)
import random
import math
for i in range(25):
    print(random.randint(1,25))
print(math.pi)

from random import *
for i in range(25):
    print(randint(1,25))
from datetime import datetime
now = datetime.now()
print("now=",now)
dt_string = now.strftime("%d+%m+%Y %H:%M:%S")
print("date and time=",dt_string)"
from my_module1 import *
courses =['History','Math','Compsic']

index = find_index(courses,'Math')
print(index)
password =10
var1 = getInputs()
if (password == var1):
    print("hello")
else:
    print('how are you') 
    #file handling

from my_module1 import echo
print(echo("please help i'am stuck a mountain:"))
echo()"""
import requests
# url = "https://httpbin.org/post"
# data ={
#     "id": 200,
#     "name":"SomeOne",
#     "passion": "coding"
# }
# response = requests.post(url,json =data)
# print("status code ,response.status_code")
# print(response.url)
# print("JSON Response",response.json())

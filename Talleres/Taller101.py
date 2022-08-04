print("TALLER 1.1")
"""Exercise: Your First Program
Generations of programmers have started their coding careers by simply printing "Hello, world!". 
You will be following in their footsteps."""
from re import X


print('Hello, world!')

"""Now, let's enhance your code with a comment. 
Print out the phrase: Hello, world! and comment it with the phrase Print the traditional hello world all in one line of code."""
print("Hello, world!") #Print the traditional hello world

"""Use the type() function to check the object type of 12.0."""
type(12.0)

"""What is the data type of the result of: 6 / 2?"""
type(6/2)

"""What is the type of the result of: 6 // 2? (Note the double slash //.)"""
type(6//2)

"""What is the value of x where x = 3 + 2 * 2"""
x = 3 + 2 * 2
print(x)

"""What is the value of y where y = (3 + 2) * 2?"""
y = (3 + 2) * 2
print(y)

"""What is the value of z where z = x + y?"""
z = x + y
print(z)

print("TALLER 1.2")

"""What is the value of the variable a after the following code is executed?"""
a = '1'
print(a)

"""What is the value of the variable b after the following code is executed?"""
b = '2'
print(b)

"""What is the value of the variable c after the following code is executed?"""
c = a + b
print(c)

"""Consider the variable d use slicing to print out the first three elements:"""
d = "ABCDEFG"
print(d[0:3])

"""Use a stride value of 2 to print out every second character of the string e"""
e = 'clocrkr1e1c1t'
print(e[0::2])

"""Print out a backslash:"""
print("\\ ")

"""Convert the variable f to uppercase:"""
f = "You are wrong"
print(f.upper())

"""Consider the variable g, and find the first index of the sub-string snow"""
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
print(g.find('snow'))

"""In the variable g, replace the sub-string Mary with Bob:"""
print(g.replace('Mary', 'Bob'))
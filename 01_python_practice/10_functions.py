# A function is a block of reusable code that performs a specific task. 
# Functions help to organize code, make it more readable, 
#  allow for code reuse.
#  You can pass data to functions through parameters, and functions can return data as a result.
#  In Python, functions are defined using the def keyword, followed by the function name and parentheses.

# lets define a simple function that greets the user
def greet_user():
    print("Hello! Welcome to the Python programming world.")
greet_user()

def gm():
    print('Hey ! Good Morning')
gm()

def gn(name):
    print(f"Good Night,{name}")

gn('Alice')

def gn(name = 'Shyam'):
    print( f"Good Night,{name},Have a nice sleep!")

gn('Ram')


# Function with return value
def square(number):
    return number * number

square(9)



# Recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(6))  # Output: 120




# Lambda Functions

def x(a):
    return(a/2)
x = lambda a: a / 2
print(x(4))  # Output: 15

def x(a,b):
    return(a*b)
x = lambda a,b:a*b
print(x(4,5))

x(4,5)
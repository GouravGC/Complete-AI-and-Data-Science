# name = input('Enter your name?') # user input 

# # age = int(input('Enter your age?'))
# print('Hello',name,'aur bhai kaise ho?')
# print('Your name is',name,'you are',age,'years old')

a = input('Enter your name?')
b = input('Enter your name?')
print('Hey',a)
age_a = int(input('Enter your age?'))
print('Hey',b)
age_b = int(input('Enter your age?'))

if age_a>age_b:
    print(a,'is older than',b)
elif age_a == age_b:
    print('Both are equal')
else:
    print(b,'is older than',a)

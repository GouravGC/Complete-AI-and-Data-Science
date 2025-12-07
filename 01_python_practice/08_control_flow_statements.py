# Conditional statements
# >
# <
# <=
# >=
# ==
# !=


x = 0

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print('x is negative')


# for loops

# foods = ['Dahi Bhallay','Biryani','Dal','Samosa','Kachori','Palak Paneer']

# # print(foods[0])

# for items in foods:
#     print(items)


# while loops

# i = 1
# while i < 100:
#     print(i)
#     i += 1

# control statement

i=1
while i < 100:
    print(i)
    i = i+1
    if i == 50:
        break

for letters in 'Python':
    if letters == 'h':
        break
    print(letters)


for letters in 'Python':
    if letters == 'h':
        continue
    print(letters)


for letters in 'Python':
    if letters == 'h':
        pass
    print(letters)

i = 1
while i in range(21):
    print(i*2)
    i = i+1
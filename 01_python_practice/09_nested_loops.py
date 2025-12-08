# Nested for loops

colors = ['red','green','blue']
items = ['book','pen','copy']

for color in colors:
    for item in items:
        print(color,item)


# for loop inside while loop

i = 1
while i < 4:
    for j in range(3):
        print(i,j)
    i += 1

# while loop inside for loop


for i in range(3):
    j = 0
    while j < 4:
        print(j, i)
        j += 1

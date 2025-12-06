# Data Structures
# List
# define a list
food = ['Dahi Bhallay','Biryani','Dal','Samosa','Kachori','Palak Paneer']
print(food)

print(food[1])
food[1] = 'Fried Rice'
print(food[1])
print(food)

# 2- Tuple

coordinates = (4.21,9.29)
print(coordinates)
print(coordinates[1])
coordinates[0] = 6.98 # This will give an error as tuples are immutable
print(coordinates[0])

# 3-Set
food_set = {'Dahi Bhallay','Biryani','Dal','Samosa','Kachori','Palak Paneer'}
print(food_set)
food_set.add('Fried Rice')
food_set.add('Dal') # Duplicate items will not be added
food_set.remove('Samosa')
print(food_set)

# 4- Dictionary
car = {'brand':'Ford','model':'Mustang','year':1964}
print(car)
print(car['year'])
car['year'] = 2020
print(car['year'])
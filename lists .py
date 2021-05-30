#Append and slicing
letters = ['a','b','c']
letters.append('d')
print(len(letters))
print(letters)

slice = letters[1:3]

print(slice)
print(letters)


animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:]

print(cat)
print(dog)
print(frog)

#dictcionaries
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print(menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!
menu['Hamburger'] = 8.50
menu['Pizza Slice'] = 3.50
menu['Salad'] = 10.00

print("There are " + str(len(menu)) + " items on the menu.")
print(menu)
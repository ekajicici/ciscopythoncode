age = [12, 23, 42, 43]
# accessing a list
x = age[1] + age[2] + age[3]
print(x)
# slicing a list
y = age[0:3]
print(y)
# mutability
age[3] = 50
print(age)
# tuples
food = ("rice", "beans", "garri", "milk")
# accessing
food_x = food[0]
print(food_x)
# looping a list
for i in age:
    print(i)
# adding the items in the list
total_age = 0
for x in age:
    total_age += x
print(total_age)
print(total_age / 4)

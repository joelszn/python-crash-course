pizzas = ['Hawaian','Pepporini','Everything']
for pizza in pizzas:
    print(f'{pizza} is top 5')
print("What's your top5 pizzas?")

animals = ['lion','tiger','snake']
for animal in animals:
    print(f'{animal} would not make a good pet'.title())
print('All of these animals are carnivores')

# 4-3 : 4-9
print('\n\n')

# 4-3
print('4-3')
for number in range(1,21):
    print(number)
print('\n\n')

# 4-4
print('4-4')
a_mili = []
for number in range(1,1000001):
    a_mili.append(number)

# for number in a_mili:
#     print(number)

# 4-5
print('4-5')
print(f'sum: {sum(a_mili)}, max: {max(a_mili)}, min: {min(a_mili)}')
print('\n\n')

# 4-6
print('4-6')
odd_numbers = []
for number in range(1,21,2):
    odd_numbers.append(number)
    print(number)
print('\n\n')

#4-7
print('4-7')
multiples_of_three = []
for multiple in range(3,31,3):
    multiples_of_three.append(multiple)
    print(multiple)
print('\n\n')

# 4-8
print('4-8')
cubes = []
for cube in range(1,11):
    new_number = cube **3
    cubes.append(new_number)
    print(new_number)
print('\n\n')

# 4-9
print('4-9')
cubes = [value**3 for value in range(1,11) ]
print(cubes)
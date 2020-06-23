# 4-10
print('4-10')
odd_numbers = []
for number in range(1,21,2):
    odd_numbers.append(number)
    # print(number)
# middle = int(len(odd_numbers)/2)
print(f"The first 3 items in the list are {odd_numbers[1:4]}")
print(f"The items in the middle of the list are {odd_numbers[5:7]}")
print(f"The last 3 items of the list are {odd_numbers[-3:]}")
print('\n\n')

# 4-11
print('4-11')
pizzas = ['Hawaian','Pepporini','Everything']
friends_pizza = pizzas[:]

pizzas.append('plain')
friends_pizza.append('extra cheese')
print(pizzas,friends_pizza)

# 4-12
print('4-12')
my_foods = ['pizza','falafel','carrot cake']
friends_foods = my_foods[:]

print('My food')
for food in my_foods:
    print(food.title())

print()
print('My friends food')
for food in friends_pizza:
    print(food.title())


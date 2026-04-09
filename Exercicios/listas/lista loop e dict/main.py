# Part 1: Lists
fruits = ["apple", "banana", "orange", "grape"]
print(fruits[0], fruits[-1])
fruits.append("mango")
fruits.remove("banana")
fruits[fruits.index("orange")] = "pineapple"

numbers = list(range(1, 11))
print(sum(numbers))
print(max(numbers), min(numbers))
numbers.reverse()
print(numbers)

cities = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
cities.sort()
cities.append("Porto Alegre")
print(cities.index("Curitiba"))
cities.remove("Rio de Janeiro")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

domestic_animals = ["dog", "cat", "rabbit"]
wild_animals = ["lion", "tiger", "bear"]
all_animals = domestic_animals + wild_animals
print(all_animals)

# Part 2: Looping with For
names = ["Ana", "Pedro", "Maria", "João"]
for name in names:
    print(name)

upper_names = []
for name in names:
    upper_names.append(name.upper())

numbers_20 = list(range(1, 21))
for num in numbers_20:
    if num % 2 == 0:
        print(num)

squares = []
for num in numbers_20:
    squares.append(num ** 2)

words = ["python", "java", "c", "javascript"]
for word in words:
    print(len(word))

ages = [12, 18, 25, 40, 60]
for age in ages:
    if age >= 18:
        print("Adult")
    else:
        print("Minor")

grades = [5.5, 7.0, 8.3, 4.9, 6.2]
approved_count = 0
failed_count = 0
for grade in grades:
    if grade >= 7:
        approved_count += 1
    else:
        failed_count += 1

shopping_list = ["rice", "beans", "potato", "meat"]
for item in shopping_list:
    print(f"I need to buy: {item}")

# Part 3: Looping with While
counter = 1
while counter <= 10:
    print(counter)
    counter += 1

user_number = -1
while user_number != 0:
    user_number = int(input("Enter a number (0 to stop): "))

total_sum = 0
current_n = 1
while current_n <= 100:
    total_sum += current_n
    current_n += 1

secret_number = 7
user_guess = 0
while user_guess != secret_number:
    user_guess = int(input("Guess the secret number: "))

even_counter = 2
while even_counter <= 20:
    print(even_counter)
    even_counter += 2
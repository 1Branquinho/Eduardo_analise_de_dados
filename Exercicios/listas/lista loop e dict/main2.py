# Exercise 1
student = {"name": "John Doe", "age": 20, "course": "Computer Science"}
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Course: {student['course']}")

# Exercise 2
product = {"name": "Mechanical Keyboard", "price": 350.00, "stock": 10}
product["brand"] = "Logitech"
product["price"] = 320.00
product["stock"] -= 2
del product["brand"]
print(product)

# Exercise 3
grades = {"Alice": 8.5, "Bruno": 7.0, "Carla": 9.2, "Daniel": 6.8}
for student_name, grade in grades.items():
    print(f"Student: {student_name}, Grade: {grade}")
average_grade = sum(grades.values()) / len(grades)
print(f"Average: {average_grade}")

# Exercise 4
numeric_data = {"a": 10, "b": 20, "c": 30}
total_sum = 0
for value in numeric_data.values():
    total_sum += value
print(total_sum)

# Exercise 5
items_list = ["apple", "banana", "orange", "apple", "banana", "apple"]
frequency_count = {}
for item in items_list:
    frequency_count[item] = frequency_count.get(item, 0) + 1
print(frequency_count)

# Exercise 6
store_items = {"pen": 10, "backpack": 80, "notebook": 45, "laptop": 3000}
filtered_items = {key: val for key, val in store_items.items() if val > 50}
print(filtered_items)

# Exercise 7
translator = {"apple": "maçã", "book": "livro", "car": "carro"}
search_term = input("Enter word: ")
print(translator.get(search_term, "Word not found"))

# Exercise 8
shopping_inventory = {"bread": 2, "milk": 1}
shopping_inventory["coffee"] = 1
shopping_inventory["bread"] = 5
del shopping_inventory["milk"]
print(shopping_inventory)

# Exercise 9
classroom = {
    "Ana": {"age": 17, "grades": [8, 9, 7]},
    "Pedro": {"age": 18, "grades": [6, 7, 8]},
    "Mariana": {"age": 17, "grades": [9, 10, 8]}
}
classroom["John"] = {"age": 19, "grades": [7, 8, 9]}
best_average = 0
top_student_name = ""
for name, details in classroom.items():
    current_avg = sum(details["grades"]) / len(details["grades"])
    print(f"{name}: Average {current_avg}")
    if current_avg > best_average:
        best_average = current_avg
        top_student_name = name
print(f"Best student: {top_student_name}")

# Exercise 10
staff_records = {}
staff_records["Alice"] = {"role": "Developer", "salary": 5000}
staff_records["Bob"] = {"role": "Manager", "salary": 7000}
search_name = "Alice"
print(staff_records.get(search_name, "Employee not found"))
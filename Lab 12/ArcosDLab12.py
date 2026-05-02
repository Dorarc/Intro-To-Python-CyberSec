'''
Name: Dorian Arcos 
Class: CSEC 1436
Date: Apr 14,2026
Purpose: Lab 12 Assignment - Chapter 10 "Try It" assessments.
10 points: General rubric.
15 points: Create a dictionary of cars step-by-step, Try it section 10.3
15 points: Character Count in a String, Try It Section 10.4
20 points: Calculate the total number of fruits, Try it section: 10.4
20 points: Dictionary comprehension: Product prices (Try it section 10.5)
20 points: Nested Dictionaries: Restructuring Company Data (Try it section 10.5)

10.3 cars step-by-step:
The primary difference in my code is the dictionary is given a different name.

10.4 Count in a String:
The primary difference was using char instead of c in the loop

10.4 total number of fruits: 
In my code, I did not use a loop with variable starting at 0.and then incrementing for each value. I created a value that sums the values of the dictionary.

10.5 Product prices:
I created separate for loops to convert dollars to Euros and then round the given vales to 2 decimal places.
The original used a more complex single line loop.

10.5 Restructuring Company Data:
I used different names for the empty dictionary as well as printed the output in an easier to read format using a loop.

'''
#10.3:

# 1. Create an empty dictionary.
dict = {}
# 2. Add a key-value pair of "Mustang": 10.
dict["Mustang"] = 10
# 3. Add another key-value pair of "Volt": 3.
dict["Volt"] = 3
# 4. Modify the value associated with key "Mustang" to be equal to 2.
dict.update({"Mustang": 2})
# 5. Delete key "Volt" and the associated value.
del dict["Volt"]
# 6. Print the dictionary
print(f'\n10.3 cars step-by-step:')
print(dict)

#10.4:
string_value = "This is a string"
characters = {}

for char in string_value:
    if char in characters:
        characters[char] += 1
    else:
        characters[char] = 1
print(f'\n10.4 Count in a String: ')
print(characters)

#10.4:
fruit_count = {"banana": 2, "orange": 5, "peach": 5}
fruit_nums = sum(fruit_count.values())
print(f'\n10.4 total number of fruits: ')
print (fruit_nums)

#10.5:
prices = {"apple": 1.99, "banana": 0.99, "orange": 2.49, "pear": 1.79}

# Create a dictionary of euro_prices
for value in prices:
    prices[value] *= 0.85
    
for value in prices:
    prices[value] = round(prices[value], 2)
# Print the content of the dictionary after the population
print (f'\n10.5 Product prices:')
print (prices)

#10.5
employees = {
    1001: {"name": "Alice", "department": "Engineering", "salary": 75000},
    1002: {"name": "Bob", "department": "Sales", "salary": 50000},
    1003: {"name": "Charlie", "department": "Engineering", "salary": 80000},
    1004: {"name": "Dave", "department": "Marketing", "salary": 60000},
    1005: {"name": "Eve", "department": "Sales", "salary": 55000}
}

# Create and populate dept_employees dictionary
comp_employees = {}
for employee_id, info in employees.items():
    dept = info["department"]
    if dept not in comp_employees:
        comp_employees[dept] = {}
    comp_employees[dept][employee_id] = {"name": info["name"], "salary": info["salary"]}

# Print the content of the dictionary after the population
print(f'\n10.5 Restructuring Company Data')
for dept in comp_employees:
    print(dept)
    for id in comp_employees[dept]:
        print(comp_employees[dept][id])
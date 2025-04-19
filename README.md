# Program-1 **Calculator Using Class**

## 🧩 Problem Statement:
Create a class-based calculator that performs addition, subtraction, multiplication, and division.

## 📥 Input:
- Two numbers `a` and `b`
- Operation as a string: `'addition'`, `'subtraction'`, `'multiplication'`, `'division'`

## 📤 Output:
Result of the chosen operation.

### 🧪 Language:
The test can be taken in **any programming language**.  
**Python** is used here with comments for clarity.

---

## 🧑‍💻 Python Code:
```python
# class Calculator:
#     def __init__(self, a, b, operation):
#         self.a = float(a)
#         self.b = float(b)
#         self.operation = operation.lower()  # Lowercase for comparison

#     def calculate(self):
#         if self.operation == 'addition':
#             return self.a + self.b
#         elif self.operation == 'subtraction':
#             return self.a - self.b
#         elif self.operation == 'multiplication':
#             return self.a * self.b
#         elif self.operation == 'division':
#             if self.b != 0:
#                 return self.a / self.b
#             else:
#                 return "Error: Division by zero!"
#         else:
#             return "Invalid operation!"

# # Example usage
# a = 10.5
# b = 2.0
# operation = 'Division'
# calc = Calculator(a, b, operation)
# result = calc.calculate()
# print(result)


# Problem-2: Generate Odd Number Series

## 🧩 Problem Statement:
Given an integer `a`, print the first `a` odd numbers.

## 📥 Input:
A single integer `a`.

## 📤 Output:
A series of `a` odd numbers starting from 1.

### 🧪 Language:
The test can be taken in **any programming language**.  
**Python** is used here with comments for clarity.

---

## 🧑‍💻 Python Code:
```python

# a = int(input())

# odd_numbers = []
# for i in range(1, a + 1):
#     odd_numbers.append(2 * i - 1)

# print(", ".join(map(str, odd_numbers)))



# Problem-3: Generate Odd Number Series Until Condition

## 🧩 Problem Statement:
Given an integer `a`, print the first `a` odd numbers **only if** `a` is **odd**.  
If `a` is even, print the series for `a-1`.

## 📥 Input:
A single integer `a`.

## 📤 Output:
A series of odd numbers accordingly.

### 🧪 Language:
The test can be taken in **any programming language**.  
**Python** is used here with comments for clarity.

---

## 🧑‍💻 Python Code:
```python

# a = int(input())

# count = a if a % 2 != 0 else a - 1

# odd_numbers = []
# for i in range(1, count + 1):
#     odd_numbers.append(2 * i - 1)

# print(", ".join(map(str, odd_numbers)))


---


# Problem-4: Count Multiples in a List

## 🧩 Problem Statement:
Given a list of integers, count how many numbers are divisible by each digit from 1 to 9.

## 📥 Input:
Example: `[1,2,8,9,12,46,76,82,15,20,30]`

## 📤 Output:
Example:  
`{1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}`

### 🧪 Language:
The test can be taken in **any programming language**.  
**Python** is used here with comments for clarity.

---

## 🧑‍💻 Python Code:
```python
# numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
# count_dict = {}

# # Count how many numbers are divisible by 1 through 9
# for i in range(1, 10):
#     count = 0
#     for num in numbers:
#         if num % i == 0:
#             count += 1
#     count_dict[i] = count

# print(count_dict)

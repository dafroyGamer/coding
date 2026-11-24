"""
Book: Think Python, 3rd Edition
Chapter 1: Programming as a Way of Thinking (Section: Values and Types)
Date: November 24, 2026

Key Takeaways:
- Every value belongs to a type:
  1. int   -> Integer (whole numbers like 2)
  2. float -> Floating-point number (decimals like 42.0)
  3. str   -> String (characters in quotes like 'Hello')
- type() tells you what type a value belongs to.
- int(), float(), and str() also act as functions to convert types.
"""

# 1. Checking basic types
print(type(2))               # <class 'int'>
print(type(42.0))            # <class 'float'>
print(type('Hello, World!')) # <class 'str'>

# 2. Type conversion functions (covered in 3rd Ed. Chapter 1)
print(int(42.9))             # 42 (Note: int() always chops off the decimal/rounds down!)
print(float(42))             # 42.0
print(str(42))               # '42'

# 3. Common trap: Numbers inside quotes are strings, not numbers
print(type('2'))             # <class 'str'>
print(int('2') + 3)          # 5 (Must convert to int before doing math)

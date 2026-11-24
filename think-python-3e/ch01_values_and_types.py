"""
Book: Think Python, 3rd Edition
Chapter 1: Programming as a Way of Thinking
Sections Covered:
- Arithmetic Operators (p. 1)
- Expressions (p. 3)
- Arithmetic Functions (p. 4)
- Strings (p. 5)
- Values and Types (p. 6)
"""

# ==========================================
# 1. ARITHMETIC OPERATORS (p. 1)
# ==========================================
print("--- 1. Arithmetic Operators ---")
print(30 + 12)      # Addition -> 42
print(43 - 1)       # Subtraction -> 42
print(6 * 7)        # Multiplication -> 42
print(84 / 2)       # Division -> 42.0 (Always returns a float!)
print(85 // 2)      # Floor division -> 42 (Chops off the decimal)
print(7 ** 2)       # Exponentiation (power) -> 49 (Note: ^ is NOT power in Python!)


# ==========================================
# 2. EXPRESSIONS (p. 3)
# ==========================================
# An expression is a combination of values, variables, and operators.
# Python follows standard PEMDAS order of operations.
print("\n--- 2. Expressions ---")
print(6 + 6 ** 2)   # 42 (Exponentiation happens before addition)


# ==========================================
# 3. ARITHMETIC FUNCTIONS (p. 4)
# ==========================================
# Built-in functions that take values (arguments) and return a result.
print("\n--- 3. Arithmetic Functions ---")
print(round(42.4))  # 42 (Rounds to nearest integer)
print(round(42.6))  # 43
print(abs(42))      # 42 (Absolute value)
print(abs(-42))     # 42


# ==========================================
# 4. STRINGS (p. 5)
# ==========================================
# Strings represent sequences of characters inside single or double quotes.
print("\n--- 4. Strings ---")
print('Hello')
print("it's")                       # Use double quotes if the text has an apostrophe
print('Well, ' + "it's" + ' small.') # '+' concatenates (joins) strings together
print('Spam, ' * 4)                 # '*' repeats the string 4 times
print(len('Spam'))                  # 4 (len() counts the number of characters)


# ==========================================
# 5. VALUES AND TYPES (p. 6)
# ==========================================
print("\n--- 5. Values and Types ---")
print(type(2))               # <class 'int'>
print(type(42.0))            # <class 'float'>
print(type('Hello, World!')) # <class 'str'>

# Type conversion functions
print(int(42.9))             # 42 (Always rounds down toward zero)
print(float(42))             # 42.0
print(str(42))               # '42'

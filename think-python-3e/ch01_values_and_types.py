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


# ==========================================
# 6. FORMAL LANGUAGE AND NATURAL LANGUAGE (p. 7)
# ==========================================
Natural language are the language people speak, like english,french, etc. They were not design by people; they evolved naturally.

Formal languages are languages that are designed by people for specific applications.
e.g, the notation that mathematicians use is a formal language that is partic‐
ularly good at denoting relationships among numbers and symbols. Similarly, pro‐
gramming languages are formal languages that have been designed to express
computations.

 # Some important difference with natural and formal language:

# Ambiguity
  Natural languages are full of ambiguity, which people deal with by using contex‐
  tual clues and other information. Formal languages are designed to be nearly or
  completely unambiguous, which means that any program has exactly one mean‐
  ing, regardless of context.
# Redundancy
  In order to make up for ambiguity and reduce misunderstandings, natural lan‐
  guages use redundancy. As a result, they are often verbose. Formal languages are
  less redundant and more concise.
# Literalness
  Natural languages are full of idiom and metaphor. Formal languages mean
  exactly what they say.

# Important:
Because we all grow up speaking natural languages, it is sometimes hard to adjust to
formal languages. Formal languages are more dense than natural languages, so it
takes longer to read them. Also, the structure is important, so it is not always best to
read from top to bottom, left to right. Finally, the details matter. Small errors in spell‐
ing and punctuation, which you can get away with in natural languages, can make a
big difference in a formal language.


# ==========================================
# 7. DEBUGGINN (p. 8)
# ==========================================
# Bug and debugging:
  Programmers make mistakes. Programming errors are called (bug) and the process of tracking them is callled (debugging).
  
# ==========================================
# 8. GLOSSARY (p. 9)
# ==========================================
# arithmetic operator:
A symbol, like + and *, that denotes an arithmetic operation
like addition or multiplication.
integer: A type that represents whole numbers.
floating-point: A type that represents numbers with fractional parts.
integer division: An operator, //, that divides two numbers and rounds down to an
integer.
# expression:
A combination of variables, values, and operators.
value: An integer, floating-point number, or string—or one of other kinds of values
we will see later.
# function:
A named sequence of statements that performs some useful operation.
Functions may or may not take arguments and may or may not produce a result.
# function call:
An expression—or part of an expression—that runs a function. It con‐
sists of the function name followed by an argument list in parentheses.
syntax error: An error in a program that makes it impossible to parse—and therefore
impossible to run.
# string:
A type that represents sequences of characters.
concatenation: Joining two strings end to end.
# type:
A category of values. The types we have seen so far are integers (type int),
floating-point numbers (type float), and strings (type str).
# operand:
One of the values on which an operator operates.
# natural language:
Any of the languages that people speak that evolved naturally
# formal language:
Any of the languages that people have designed for specific pur‐
poses, such as representing mathematical ideas or computer programs. All program‐
ming languages are formal languages.
# bug:
An error in a program.
# debugging:
The process of finding and correcting errors.


# ==========================================
# 9. Exercise (p. 10)
# ==========================================
  

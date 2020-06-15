"""
--> Using the try-except-else Block
Error handling in Python can be done easily using the try/except block. Adding an else statement
to this block might be useful. It’s run when there is no exception raised in the try block.
"""

a, b = 1, 0

try:
    print(a / b)
    # exception raised when b is 0
except ZeroDivisionError:
    print("division by zero")
else:
    print("no exceptions raised")
finally:
    print("Run this always")



















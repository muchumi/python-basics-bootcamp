"""
    Generator expressions have a syntax similar to list comprehensions but with paranthesis instead of square brackets.
    Generator expressions are designed for situations where generator is used right away by an enclosing function.
    Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly
    than equivalent list comprehensions.
"""

# Example One # Sum of Squares
print(sum(item*item for item in range(7)))

# Example Two # Dot product
listOne = [10, 15, 20]
listTwo = [2, 4, 6]

print(sum(listOne*listTwo for listOne, listTwo in zip(listOne, listTwo)))



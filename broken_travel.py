# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

"""
Corrections made:
1. Fixed incorrect `==` in `year == int.input(...)` -> changed to `year = int(input(...))`.
2. Removed incorrect closing quotation mark in `input(...)`.
3. Added missing colon `:` after `if year <= 1900`.
4. Replaced incorrect `&&` with `and` in `elif year > 1900 && year < 2020`.
5. Added a condition to `elif` (changed `elif:` to `else:`).
6. Standardized quotation marks for consistency.
"""

# Tsion fixed: '==' to '=' for assignment and corrected the input syntax
year = int(input("Greetings! What is your year of origin? ")) # Tsion fixed the input syntax 

# Tsion added colon at the end of 'if' statement and used proper comparison operators
if year < 1900:  # Tsion fixed: missing colon and wrong condition syntax (used && which is invalid in Python)
    print('Woah, that is the past!') # Print message for the past
    
# Tsion changed logical operator '&&' to 'and' (Python uses 'and' for logical comparisons)
elif year >= 1900 and year <= 2020:  # Tsion used 'and' instead of '&&' and fixed the condition
    print("That's totally the present!") # Print message for the present

# Tsion added proper 'else' block and fixed condition
else:  # Tsion fixed: replaced invalid 'elif' with 'else' as no further condition is necessary
    print("Far out, that's the future!!")  # Tsion added: print message for future years

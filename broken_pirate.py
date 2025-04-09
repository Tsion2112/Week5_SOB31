# Tsion fixed: added proper parentheses and colons, fixed logic issues
greeting = input("Hello, possible pirate! What's the password?")  # Tsion added input for pirate password

# Tsion fixed: mismatched parentheses and incomplete condition
if greeting in ["Arrr!"]:  # Tsion changed the incorrect list syntax (missed closing parenthesis)
    print("Go away, pirate.")  # Tsion added this line to print if password matches "Arrr!"

# Tsion fixed: 'elif' was incomplete, added correct condition and print statement
else:  # Tsion added 'else' to handle the case when the password is not "Arrr!"
    print("Greetings, hater of pirates!")  # Tsion added this line to greet non-pirates

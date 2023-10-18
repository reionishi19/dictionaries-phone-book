"""
Rei Onishi
October 11, 2023

Dictionaries: Phone Book
"""

# Problem 1
# Create a phone book.

phone_book = {}

print("When entering a name and number, please enter names with underscores.\n" +
      "For example: Matt_Priem, 507-389-1438. When done, type 'quit'\n")
      
### Your code here ###

while True:
    user_input = input("Enter name and number:")
    if user_input == 'quit':
        break
    name, number = user_input.split(', ')
    phone_book[name] = number

print(f"Your phone book consists of {phone_book}")



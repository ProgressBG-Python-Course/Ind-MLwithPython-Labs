# ask user to enter a name (string), until it contains at least 3 symbols
# the len function on string returns the number of symbols in a string
user_name = input("Enter a name, please: ")
user_name_length = len(user_name)

while user_name_length < 3:
  user_name = input("Enter a name (at least 3 symbols): ")
  user_name_length = len(user_name)

print("Thank you, {}!".format(user_name))
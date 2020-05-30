user_name = input('Enter your user name ')
user_name_lenght = len(user_name)
while True:
    if user_name_lenght >=3:
        print("Nice, your user_name is: {}".format(user_name))
        break
    else:
        print("Enter your user name (at least 3 symbols)")
        break


# x е четно => even
# x е нечетно => odd
# x е нула => "don't know"

x = 2

if x==0:
    print("don't know")
elif x%2 == 0:
    print('even')
elif x%2:
    print('odd')

# white list with apple,bannana,orange,potato & new list in the widdle with strawberry and blackberry
#change apple with pineappe
#white potato in different variable
#change blackbetty with cranberry

fruits = ['apple','bannana',['strawberry','blackberry'],'orange','potato']
print(type(fruits))
fruits[1] = 'pineapple'
print(fruits[1])
vegetables = fruits[4]
print(vegetables)
fruits[2][1] = 'cranberry'
print(fruits)
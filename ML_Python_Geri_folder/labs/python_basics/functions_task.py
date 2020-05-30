# def sum_numbers(*args):
#     '''sum the numbers'''
#     print(sum(args))
# sum_numbers(1)
# sum_numbers(1,2)
# sum_numbers(1,2,3)

def find_bigger_number(*args):
    bigger_number = max(*args)
    print(bigger_number)
find_bigger_number(2,8)
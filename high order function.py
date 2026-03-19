# # 1 Write a function calculate that takes another function and 
# # a number as arguments and applies
# # that function to the number.
# def first(num):
#      return num(2)
# def num(n):
#     return n**2 
# a=first(num)
# print(a)

# # 2 Create a function operation that accepts two numbers and
# #  a function (like add, multiply) and
# # returns the result after applying the function.
# def cal(add, multiply, func):
#     return func(add, multiply)
# def add(a, b):
#     return a + b
# def multiply(a, b):
#     return a * b
# a=cal(3, 4, add)
# b=cal(3, 4, multiply)
# print(a,b)
# # 3 Write a function power_generator that returns another
# #  function which calculates the cube of a
# # number.
# def power_gne(cube):
#     return cube(5)
# def cube(n):
#     return n**3
# a=power_gne(cube)
# print(a)
# # 4 Create a function apply_twice that takes a function and 
# # a number, and applies the function two
# # times on the number.
# def apply_twice(func,a):
#     return func(func(a))
# def sqarer(x):
#     return x*x
# print(apply_twice(sqarer,2))

# 5 Write a function choose_function that takes a string 
# argument ('double' or 'triple') and returns a
# # corresponding function to multiply a number.
# def multiply(n):
#     return lambda x: x * n
# def choose_function(choice):
#     if choice == 'double':
#         return multiply(2)
#     elif choice == 'triple':
#         return multiply(3)
# # usage
# f = choose_function('triple')
# print(f(10))   # 30

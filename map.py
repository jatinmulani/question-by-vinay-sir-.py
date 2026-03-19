# # Map – Coding Questions
# # 1 Write a program that takes a list of integers
# #  and uses map to return a new list containing the
# # square of each number.
# li=[1,2,3,4,5,6]
# def sqare(n):
#     return n**2
# print(list(map(sqare,li)))
# # 2 Given a list of temperatures in Celsius, 
# # use map to convert them into Fahrenheit. (Formula: F =
# # (C × 9/5) + 32)
# temp=[3,4,5,6,7,8,9,10]
# def celsiuse(c):
#     return (c*9/5)+32
# print(tuple(map(celsiuse,temp)))
# # 3 Take a list of strings and use map 
# # to convert each string into its uppercase form.
# a=['jatin','mulani','kriti','gauttam']
# def upper(n):
#     return n.upper()
# print(list(map(upper,a)))
# # 4 Given a list of numbers, use map 
# # with a lambda function to add 10 to each element and print
# # the updated list.
# a=[1,2,3,5,5,6,8,7,8,9]
# print(list(map(lambda x:x+10,a)))

# # 5 Write a program that takes two lists of
# #  equal length and uses map to return a list containing the
# # sum of corresponding elements.
# a=[1,2,3,4]
# b=[4,5,6,7]
# print(list(map(lambda x,y:x+y,a,b)))

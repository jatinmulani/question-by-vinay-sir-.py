# 1 Given a list of integers, use filter to create a new list
#  containing only even numbers.
# a=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,a)))


# # 2 Write a program that takes a list of numbers and filters out all
# #  numbers greater than 50.
# a=[51,10,20,30,40,50,60,410,89]
# print(list(filter(lambda x:x>50,a)))

# 3 Given a list of strings, use filter to return only those strings
#  whose length is greater than 5.
# a=['jatin','mulani','kriti','gauttam']
# # #for i in a:
# #     print(i)
# def length():
#     li=[]
#     for i in a:
#         if(len(i)>=5):
#             li.append(i)
#     return li
# l=length()
# print(l)
# # using filter function
# a = ['jatin','mulani','kriti','gauttam']
# print(list(filter(lambda x: len(x) >= 5, a)))


# # 4 Write a program to filter out all negative numbers from a given
# #  list using filter and lambda.
# a=[1,-2,2,-3,3,-4,-8,9,5,66,-96]
# print(list(filter(lambda x:x>0,a)))

# # 5 Given a list of integers, use filter to extract only numbers 
# # that are divisible by both 2 and 3.
# a=[1,2,3,4,51,6,1,4,32,3,583,5,1,652,28,32,852,38,41,2,5851,45,24]
# print(list(filter(lambda x:x%2==0 and x%3==0,a)))

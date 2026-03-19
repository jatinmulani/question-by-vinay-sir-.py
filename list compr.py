# question by vinay sir
# a=[i for i in range(1,101)]
# # print(a)
# a=[i**2 for i in range(1,10)]
# print(a)
# a=['apple','car','elephant','dog','cat']
# # for i in a:
# #     if(len(i)<4):
# #         print(i)
# a=['apple','car','elephant','dog','cat']
# b=[i for i in a if(len(i))<4]
# print(b)

# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
# b=[i for i in a if(i>=10)]
# print(b)

# a=[i for i in range(100,0,-1) if(i%2!=0)]
# print(a)


# assignment by vinay sir 
# • Create a list of numbers from 1 to 10 using list comprehension.
# • Create a list containing squares of numbers from 1 to 10.
# • Create a list containing cubes of numbers from 1 to 10.
# • Generate a list of even numbers from 1 to 20.
# • Generate a list of odd numbers from 1 to 20.

# a=[i for i in range(1,11)]
# print(a)

# a=[i**2 for i in range(1,11)]
# print(a)

# a=[i**3 for i in range(1,11)]
# print(a)

# a=[i for i in range(1,21)if(i%2==0)]
# print(a)

# a=[i for i in range(1,21)if(i%2!=0)]
# print(a)

# Using Conditions
# • Create a list of numbers divisible by 3 from 1 to 30.
# • Create a list of numbers greater than 10 from a given list.
# • From a list of numbers, create a new list containing only positive numbers.
# • From a list, create a list containing only negative numbers.
# • Create a list of numbers whose square is greater than 50.

# a=[i for i in range(1,31)if(i%3==0 and i%7==0)]
# print(a)


# list=[1,2,1,2,1,2,1,1,19,10,10,10,1,1,11,1,12,12,13,14,15,15,15]
# a=[i for i in list if(i>=10)]
# print(a)

# list1=[1,2,3,4,5,-1,-2,-3,-4,-5,6,-6,-8,8,5,-6]
# a =[i for i in list1 if(i>0)]
# print(a)

# list1=[1,2,3,4,5,-1,-2,-3,-4,-5,6,-6,-8,8,5,-6]
# a=[i for i in list1 if(i<0)]
# print(a)

# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# b=[i for i in a if((i**2)>=50)]
# print(b)

# Working with Strings
# • Convert all words of a list into uppercase using 
# list comprehension.
# • Convert all words into lowercase.
# • Create a list containing length of each word from a list of strings.
# • Extract only words having more than 4 characters.

# a=['aman','jatin','kalu']
# b=[i.upper() for i in a]
# print(b)

# a=['amAn','jaTIin','KAalu']
# b=[i.lower() for i in a]
# print(b) 

# a=['aman','jatin','kalu']
# b=[len(i) for i in a]
# print(b)

# a=['apple','car','elephant','dog','cat']
# b=[i for i in a if(len(i))<4]
# print(b)

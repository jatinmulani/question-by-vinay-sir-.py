# 1 Write a function that takes two numbers as input and 
# returns their sum.
# def sum(a,b):
#     return a+b
# x=sum(10,20)
# print(x)

# 2 Write a function that takes a number
#  and returns its square.
# def sqare(n):
#     return n*n
# x=sqare(6)
# print(x)

# # 3 Write a function that takes a number 
# # and returns its cube.
# def cube(n):
#     return n*n*n
# x=cube(6)
# print(x)

# # 4 Write a function that takes a number and returns whether
# #  it is even or odd.
# def even_odd(n):
#     if(n%2==0):
#         return True
#     return False
# n= even_odd(12)
# if(n==True):
#     print('prime')
# else:
#     print('not prime')

# # 5 Write a function that takes a number
# #  and returns its factorial.
# def factorial(n):
#     prod=1
#     for i in range(1,n+1):
#         prod=prod*i
#     return prod
# fact=factorial(5)
# print(fact)
        
# # 6 Write a function that takes two numbers and returns the
# #  larger number.
# def large(n,m):
#     if(n>m):
#         return n
#     else:
#         return m
# l=large(100,20)
# print(l)

## 7 Write a function that takes three numbers and returns
##  the smallest number.
# def smallest(a, b, c):
#     if a <= b and a <= c:
#         return a
#     elif b <= a and b <= c:
#         return b
#     else:
#         return c
# print(smallest(100, 20, 30))

# # 8 Write a function that takes a number and returns the 
# # reverse of the number.
# def reverse(n):
#     rev=0
#     while(n>0):
#         rev=rev*10+n%10
#         n=n//10
#     return rev
# r=reverse(15)
# print(r)

## 9 Write a function that takes a number and returns the
#  sum of its digits.
# def sum(n):
#     sumo=0
#     while(n>0):
#         sumo+=n%10
#         n=n//10
#     return sumo
# print(sum(17))

# 10 Write a function that takes a number and returns whether
# #  it is a palindrome or not.
# def palindrome(n):
#     n=str(n)
#     a=100
#     start=0
#     end=len(n)-1
#     while(start<end):
#         if(n[start]!=n[end]):
#             a=101
#             break
#         start+=1
#         end-=1
#     if(a==101):
#         return False
#     return True
# a=palindrome('naman')
# if(a==True):
#     print('palindrome')
# else:
#     print('not a palindrome')

# 11 Write a function that takes a number and 
# # returns the count of digits in the number.
# def count(n):
#     count=0
#     while(n>0):
#         count+=1
#         n=n//10
#     return count
# c=count(121)
# print(c)

# 12 Write a function that takes a number and returns 
# # whether it is a prime number or not.
# def prime(n):
#     i=2
#     a=100
#     while(i<n):
#         if(n%i==0):
#             a=101
#             break
#         i+=1
#     if(a==100):
#         return True
#     return False
# p=prime(12)
# if(p==True):
#     print('prime')
# else:
#     print('not prime')

# # 13 Write a function that takes two numbers and
# #  returns their product.
# def prod(n,m):
#     return(n*m)
# a=prod(2,3)
# print(a)

# # 14 Write a function that takes two numbers and returns 
# # the remainder when the first number is
# # divided by the second.
# def remainder(n,m):
#     return n%m
# a=remainder(7,3)
# print(a)

# # 15 Write a function that takes a number and returns the
# #  sum of numbers from 1 to that number.
# def sum(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#     return sum
# a=sum(10)
# print(a)

# # # 16 Write a function that takes a number and returns 
# # # the multiplication table of that number.
# def table(n):
#     res= [n*i for i in range(1,11)]
#     return res
# a=table(5)
# print(a)

# 17 Write a function that takes two numbers and 
# returns the power of the first number raised to the
# # second number.
# def power(n,m):
#     return n**m
# po=power(2,5)
# print(po)


# # 18 Write a function that takes a number and
# #  returns the last digit of the number.
# def lasst(n):
#    return n%10
# last=lasst(125)
# print(last)
# # 19 Write a function that takes a number and
# #  returns the first digit of the number.
# def first(n):
#     # n=str(n)
#     while(n>=10):
#         n=n//10
#     return n
# a=first(123450)
# print(a)
# # 20 Write a function that takes two numbers
# #  and returns the absolute difference between them.
# def diff(n,m):
#     if n>m:
#         return n-m
#     else:
#      return m-n
# d=diff(4,8)
# print(d)

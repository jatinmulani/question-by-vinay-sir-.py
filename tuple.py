# 1 Create a tuple containing five different numbers and display it.
# 2 Access the first and last element of a tuple.
# 3 Find the total number of elements present in a tuple.
# 4 Check whether a given value exists inside a tuple.
# 5 Concatenate two tuples and print the new tuple.
# 6 Repeat a tuple two times using an operator.
# 7 Find the index of a specific element in a tuple.
# 8 Count how many times a particular value appears in a tuple.
# 9 Slice a tuple to display elements from index 1 to 4.
# 10 Iterate through all elements of a tuple using a loop.

# # 1 
# a=(10,20,30,40,50)
# print(a)

#2nd 
# a=(10,20,30,40,50)
# f=a[0]
# l=a[4]
# print(f)
# print(l)

# # 3rd
# a=[10,20,30,40,50]
# count=0
# for i in a:
#     count+=1
# print(count)

# # 4th 
# a=[10,20,30,4,0]
# targest=5
# b=101
# for i in a:
#     if(i==targest):
#      b=100
#      break
# if(b==100):
#    print('exist')
# else:
#    print('not exist')

# 5th
# a=(10,20,30,40,50)
# b=(20,30,4,50,60)
# c=a+b
# print(c)


# # 6th 
# a=(10,20,30,40,50)
# b=a*2
# print(b)

# # 7th
# a=(10,20,30,'jatin','@')
# print(a.index('@'))


# # 8th 
# a=(10,20,10,20,102,10,2010,'@')
# count=0
# for i in a:
#     if(i==10):
#         count+=1
# print(count)
    
# # 9th
# a=(10,20,30,40,20,30)
# result=a[1:5]
# print(result)

# # 10th 
# a=(10,20,30,'jatin','@')
# for i in a:
#     print(i)


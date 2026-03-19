# # q1-> Print all elements of a 2D list row-wise
# a=[[1,2,3],[1,2,3]]
# for i in a:
#     for j in i:
#         print(j)

# # # #q2=> Print all elements column-wise.
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in range(len(matrix[0])): 
#     # print(i)     # columns
#     for j in range(len(matrix)):     # rows
#         print(matrix[j][i], end=" ")
#     print()

# # q3 Find the sum of all elements in a 2D list.
# a=[[1,2,3],[4,5,6]]
# sum=0
# for i in a:
#     for j in i:
#         sum=sum+j
# print(sum)

# #q4  Find the maximum element in a 2D list.
# # method by me 
# a = [[1, 2, 4], [5, 6, 3]]
# new=[]
# for i in a:
#     for j in i:
#         new.append(j)
# max=new[0]
# for k in new:
#     if(k>max):
#         max=k
# print(max)

# #by help from others 
# a = [[1, 2, 4], [5, 6, 3]]
# max_value = a[0][0]
# for i in a:
#     for j in i:
#         if j > max_value:
#             max_value = j
# print(max_value)


# # q5 Find the minimum element in a 2D list.
# a = [[1, 2, 4], [5, 6, 3]]
# min_value = a[0][0]
# for i in a:
#     for j in i:
#         if j < min_value:
#             min_value = j
# print(min_value)

# # 6 Count total number of elements in a 2D list.
# count=0
# a = [[1, 2, 4], [5, 6, 3]]
# for i in a:
#     for j in i:
#         count+=1
# print(count)

# # # 7 Print each row of a 2D list separately.
# a = [[1, 2, 4], [5, 6, 3]]
# for i in a:
#         print(i)

    
# # 8 Print each column of a 2D list separately.
# a = [[1, 2, 4], [5, 6, 3]]
# for i in range(len(a[0])):  
#     for j in a:                 # or for j in range(len(a)):
#         print(j[i], end="")     #        print(a[j][i],end='')
#     print()
# # print("i",len(a[0]))   # len function =0,1,2


# # 9th  Find the sum of each row.
# a = [[1, 2, 4], [5, 6, 3]]
# for i in a:
#     sum=0
#     for j in i :
#         sum=sum+j
#     print(sum)

# # 10# Find the sum of each column.
# a = [[1, 2, 4], [5, 6, 3]]
# for i in range(len(a[0])):  
#     sum=0
#     for j in a:         
#         sum=sum+j[i]      
#     print(sum, end="")
#     print()

# # # 11 Print the main diagonal elements#diagnoal means index match (row index==coloumn index)
# a = [[1, 2, 4],[5, 6, 3]]
# for i in range(len(a)):
#     print(a[i][i]) 

# # # 12 Print the secondary diagonal elements.
# a = [[1, 2, 4],
#      [5, 6, 3]]
# for i in range(len(a)):
#     print(a[i][len(a[0]) - 1 - i])# top right se bottom left tak jo element aate hai wo secondary elemenr khlate

# # 13 Find the sum of diagonal elements.
# a = [[1, 2, 4],
#      [5, 6, 3]]
# sum=0
# for i in range(len(a)):
#     sum=sum+a[i][i]
# print(sum) 

# # 14 Count even numbers in a 2D list.
# a = [[1, 2, 4],[5, 6, 3]]
# count=0
# for i in a:
#     for j in i:
#         if(j%2==0):
#             count+=1
# print(count)

# # 15 Count odd numbers in a 2D list.
# count=0
# a = [[1, 2, 4],[5, 6, 3]]
# for i in a:
#     for j in i:
#         if(j%2!=0):
#             count+=1
# print(count)

# # 16 Replace all negative numbers with 0.
# a = [[1, -2, 4],[-5, 6, -3]]
# new=[]
# for i in a:
#     for j in i:
#         if(j<1):
#             j=0
#         new.append(j)
# print(new)

# 17 Find the position (row, column) of a given element.
# # print the indexes of target sum => 7
# a=[1,2,3,4,5] 
# ## (1,4)=>2+5=7
# ##(2,3)=>3+4=>7
# a=[1,2,3,4,5]
# for i in range(len(a)):
#     for j in range(i+1,len(a)) :
#         if(a[i]+a[j]==7):
#             print(i,j,a[i],a[j])

# # 18 Check whether a number exists in the 2D list.
# a = [
#     [1, 2, 4],
#     [5, 6, 3]
# ]
# target=89
# b=100
# for i in a:
#     for j in i:
#         if(j==target):
#             b=101
# if(b==101):
#     print('exist')
# else:
#     print('not exist')

# # 19 Flatten a 2D list into a single list.
# a = [
#     [1, 2, 4],
#     [5, 6, 3]
# ]
# new=[]
# for i in a:
#     for j in i:
#         new.append(j)
# print(new)
# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in a:
#     for j in i :
# #         print(j)
# a=[[1,2,3],[4,5,6],[7,8,9]]
# sum=0
# for i in a:
#     for j in i :
#         sum=sum+j
# print(sum)

# a=[[1,2,3],[4,5,6],[7,8,9]]
# max=a[0][0]
# for i in a:
#     for j in i :
#         if(j>max):
#             max=j
#     print(max)
# a=[[1,2,3],[4,5,6],[7,8,9]]
# mini=a[0][0]
# for i in a:
#     for j in i :
#         if(j<mini):
#             mini=j
# print(mini)
# count=0
# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in a:
#     for j in i :
#         count+=1
# print(count)

# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in a:
#     sum=0
#     for j in i :
#         sum=sum+j
#     print(sum)
# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(a[0])):
#     sum=0
#     for j in a:
#         sum=sum+j
#     print(sum)
# a = [[1, -2, 4],[-5, 6, -3]]
# new=[]
# for i in a:
#     for j in i :
#         if(j>0):
#             new.append(j)
#         else:
#             new.append(0)
# print(new)
# a = [[1, -2, 4],[-5, 6, -3]]
# new=[]
# for i in a:
#     row=[]
#     for j in i:
#         if j < 0:
#             row.append(0)
#         else:
#             row.append(j)
#     new.append(row)
# print(new)
# a=[[1,2],3,[4,5,6],[7,8,9],8]
# new=[]
# for i in a:
#     if(type(i)==list):
#         for j in i :
#             new.append(j)
#     else:
#         new.append(i)
# print(new)

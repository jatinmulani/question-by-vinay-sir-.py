# #1, # Find Frequency of Each Element
# nums = [1, 2, 2, 3, 1, 4, 2]
# numy = {}
# for i in nums:
#     if i in numy:
#         numy[i] += 1
#     else:
#         numy[i] = 1
# print(numy)


# # # # 2. Rotate a List Left by One Position
# # # 1st method
# a = [10, 20, 30, 40, 50]
# k=5
# for  i in range(k):
#     x=a.pop()
#     a.insert(0,x)
#     k+=1
#     print(a)

# # # by vinay sir method
# # # step1 reverse the  table
# # # step2  revere 0 se k-1
# # # reverse  k to n-1

# # li=[1,2,3,4,5]
# # k=2
# # left=0
# # right=len(li)-1
# # while(left<right):
# #     li[left],li[right]=li[right],li[left]
# #     left+=1
# #     right-=1
# # left=0
# # right=k-1
# # while(left<right):
# #     li[left],li[right]=li[right],li[left]
# #     left+=1
# #     right-=1
# # left=k
# # right=len(li)-1
# # while(left<right):
# #     li[left],li[right]=li[right],li[left]
# #     left+=1
# #     right-=1
# # print(li)

# # #  q3 ->Find Index of All Occurrences of a Given Element target 7
# a=[1,2,3,4,5]
# for i in range(len(a)):
#     for j in range(i+1,len(a)) :
#         if(a[i]+a[j]==6):
#             print(a[i],a[j])

# # # q4 Remove All Negative Numbers from a List
# # nums = [3, -1, 5, -7, 8, -2]
# # new=[]
# # for i in nums:
# #     if(i>0):
# #         new.append(i)
# # print(new)

# # #  q5 ->Check Whether a List is Palindrome
# # s=[1,2,1,5]
# # index = 0
# # a = 1
# # last = len(s)-1
# # while (index < len(s)):
# #     if (s[index] != s[last]):
# #         a = 2
# #         break
# #     print("index", index, s[index], s[last])
# #     index += 1
# #     last -= 1
# # if (a == 2):
# #     print('not a palindrome')
# # else:
# #     print('palindrome')

# # q=>6 # Merge Two Lists and Remove Duplicates
# # list1 = [1, 2, 3]
# # list2 = [3, 4, 5]
# # list3=list1+list2
# # uniq=[]
# # dupl=[]
# # for i in list3:
# #     if(i not in uniq):
# #         uniq.append(i)
# #     else:
# #         dupl.append(i)
# # print(uniq)


# # #  q7 => Find Missing Number from 1 to n
# nums = [1, 2, 4, 5, 6]   #18
# n=len(nums)+1      #6
# total_sum=n*(n+1)//2   #21
# missing=total_sum-sum(nums) #21-18
# print(missing)

# # #  q8 => Remove Elements That Appear More Than Once
# # nums = [1, 2, 2, 3, 4, 4, 5]
# # uniq=[]
# # dupl=[]
# # for i in nums:
# #     if(i not in uniq):
# #         uniq.append(i)
# #     else:
# #         dupl.append(i)
# # print(uniq)

# # # q9# sorting 
# a=[0,1,0,3,12]
# i=0
# j=0
# while(i<len(a)):
#     if(a[i]!=0):
#         a[i],a[j]=a[j],a[i]
#         j+=1
#     i+=1
# print(a)
# for num in range(101,2,-1):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         print(num, end=" ")
# # # # leet code question 
# nums=[-2,1,-3,4,-1,2,1,-5,4]
# largest_sum=nums[0]
# curr_sum=nums[0]
# # start=0
# # end=0
# for i in range(1,len(nums)):
#     if(curr_sum<0):
#         curr_sum=0
#     curr_sum+=nums[i]
#     if curr_sum>largest_sum :
#         largest_sum=curr_sum   
# print(largest_sum)

# # nums=[-2,1,-3,4,-1,2,1,-5,4]
# # largest_sum=nums[0]
# # curr_sum=nums[0]
# # start=0
# # end=0
# # for i in range(1,len(nums)):
# #     if(curr_sum<0):
# #         curr_sum=0
# #         start=i
# #     curr_sum+=nums[i]
# #     if curr_sum>largest_sum :
# #         largest_sum=curr_sum
# #         end=i     
# # print(largest_sum)
# # print(start)
# # print(end)
# # print(nums[start:end+1])
# # nums=[2,7,11,15]
# # target=9
# # for i in range(len(nums)):
# #             for j in range(i+1, len(nums)):
# #                 if nums[i] + nums[j] == target:
# #                         print(i,j)
               
# # a=[10,20,10,20,10,20,30,10,20,10]
# # dupl=[]
# # uniq=[]
# # for i in a:
# #     if i not in uniq:
# #         uniq.append(i)
# #     else:
# #         dupl.append(i)
# # print(dupl)

# a='this is a senetence and its famous for daal baati churma '
# count=0
# for i in a:
#     if(i.isalpha()):
#         count+=1
# print(count)
# s='this is a sentence'
# sen=s.split()
# print(sen)
# count=0
# for i in sen:
#     count+=1
# print(count)
# # count=0
# # a=[1,2,3,4,5,6,70,80,91,10]
# # for i in a:
# #    if(i>10):
# #       count+=1
# # # print(count)

# nums=[5,2,7,2,9,2]
# target=2
# for i in range(len(nums)):
#     if(nums[i]==target):
#         print(i)

# # a=[1,-2,-3,4,-5,-6,-8,-7,2]
# # re=[]
# # for i in a:
# #     if(i>=0):
# #         # print(i)
# #         re.append(i)
# # print(re)

# a=[1,2,1]
# start=0
# end=len(a)-1
# k=100
# while start<end :
#     if a[start] != a[end] :
#         k=101
#         break
#     start+=1
#     end-=1
# if(k==101):
#     print('its not a palindrome')
# else:
#     print('palindrome')

# a=[1,2,3]
# b=[3,4,5]
# c=a+b
# uniq=[]
# dupl=[]
# for i in c:
#     if i not in uniq:
#         uniq.append(i)
#     else:
#         dupl.append(i)
# print(uniq)

# a=[2,3,5,7,4,3]
# target=7
# start=0
# end=len(a)-1
# res=[]
# while start<end:
#     if(a[start]+a[end]==7):
#         res.extend([a[start],a[end]])
#         print(start,end)
#     end-=1
#     if(start==end):
#         end=len(a)-1
#         start+=1
# print(res)

# a=[1,2,4,5,6]
# n=len(a)+1
# missing=n*(n+1) //2
# sum=0
# for i in a:
#     sum=sum+i
# print(missing-sum)


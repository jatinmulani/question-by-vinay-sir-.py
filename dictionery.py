# dicy={'e_name':'jatin','department':'management','exp':10,'location':'jaipur','mob':9024650438}
# dicy['gender']='male'
# print(dicy)
# for key,value in dicy.items():
#     print(f'{key} -> {value}')    
# dicy['department']='hr'
# print(dicy)

# 2nd write a program to count how many elements are presents into the dict
#3rd remove any key from the dict
# 4th remove any item from the dict (pop.items)
#5th swap keys and value pairs of the dictionery

# 2nd 
# dicy={'e_name':'jatin','department':'management','exp':10,'location':'jaipur','mob':9024650438}
# count=0
# for key in dicy.items():
#     count+=1
# print(count)

# 3rd
# dicy={'e_name':'jatin','department':'management','exp':10,
#       'location':'jaipur','mob':9024650438}
# dicy.pop('e_name')
# print(dicy)
# 4th
# dicy={'e_name':'jatin','department':'management','exp':10,
#       'location':'jaipur','mob':9024650438}
# dicy.popitem()
# print(dicy)

# # 5th
# dicy= {'a': 1, 'b': 2, 'c': 3}
# new_dicy={}
# for key,value in dicy.items():
#     new_dicy[value]=key
# print(new_dicy)

# # 2nd method 
# dicy = {'a': 1, 'b': 2, 'c': 3}
# new_dicy = {}
# for key in dicy:
#     value = dicy[key]
#     new_dicy[value] = key
# print(new_dicy)


# # 7th  largest find krna 
# dicy={'a':10,'b':20,'c':30,'d':40}
# largesst=0
# for i,y in dicy.items():
#     if(y>largesst):
#         largesst=y
# print(largesst)

# ##8th min value find krna 
# dicy={'a':10,'b':20,'c':30,'d':40}
# min_val = float('inf')
# for k, v in dicy.items():
#     if v < min_val:
#         min_val = v
# print(min_val)

# 1 1. Count Character Frequency: Write a function that 
# takes a string and returns a dictionary
# where the key is the character and the value is the 
# number of times that character appears.
# Example: Input 'banana' → Output {'b':1, 'a':3, 'n':2}.
# a='my name is jatin and  i am from sawai madhopur'
# new={}
# for i in a:
#     if i in new:
#         new[i]+=1
#     else:
#         new[i]=1
# print(new)

# 2 2. Merge Two Dictionaries with Sum: Given 
# two dictionaries containing integer values, merge
# them. If a key appears in both dictionaries, add
#  their values. Example: d1={'a':10,'b':20}
# ## d2={'b':5,'c':15} → Output {'a':10,'b':25,'c':15}.
# d1={'a':10,'b':20}
# d2={'b':5,'c':15} 
# for i in d2:
#     # print(i)
#     if i in d1:
#         d1[i]=d1[i]+d2[i]
#     else:
#         d1[i]=d2[i]
# print(d1)
# 3 3. Group Words by First Letter: Given a list of words,
#  create a dictionary where the key is the
# first letter and the value is the list of
#  words starting with that letter. Example:
# ['apple','ant','banana','ball'] → {'a':['apple','ant'], 'b':['banana','ball']}.
# li=['appple','ant','banana','bsll']
# result={}
# for word in li:
#     first_cahr=word[0]
#     if first_cahr in result:
#         result[first_cahr].append(word)
#     else:
#         result[first_cahr]=[word]
# print(result)

# 4 4. Group Numbers by Even and Odd: Given a list of numbers, 
# create a dictionary with keys
# 'even' and 'odd' and store numbers accordingly.
#  Example: [1,2,3,4,5] →
# # {'odd':[1,3,5],'even':[2,4]}.
# a=[1,2,3,4,5]
# odd={}
# even={}
# for i in a:
#     if(i%2==0):
#         even[i]=i
#     else:
#         odd[i]=i
# print(even)
# print(odd)
# 5 5. Check if All Values are Unique: Write a
#  function that checks if all values in a dictionary are
# unique. Example: {'a':1,'b':2,'c':3} → True,
# #  {'a':1,'b':2,'c':1} → False.
# a={'a':1,'b':2,'c':1} 
# uniq={}
# for key,value in a.items():
#     if value   in uniq:
#         print(' not uniq')
#         break
#     else:
#        uniq[value]=value
# else:
#     print('uniq')
# 6 6. Valid Parenthesis: Given a string 
# containing brackets (), {}, [], determine if the string is valid.
# A string is valid if every opening bracket has a corresponding closing bracket of the same type
# and in the correct order.
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid

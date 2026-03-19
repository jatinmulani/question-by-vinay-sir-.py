# # 1. Create a set of numbers from 1 to 5 and print it.
# a={1,2,3,4,5}
# print(a)
# # 2. Add an element to an existing set.
# a={1,2,3,4,5}
# a.add(6)
# print(a)

# # 3. Remove an element using remove() and observe what happens 
# # if the element does not exist.
# a={1,2,3,4,5}
# a.remove(3)
# print(a)
# # if element doesnot exist then it will go through error

# # 4. Remove an element using discard() and compare the 
# # behavior with remove().
# a={1,2,3,4,5}
# a.discard(6)
# print(a)
# # in disscard if we remove something that 
# is not in set  it coudnot goes through an error
# # 5. Find the length of a set.
# a={1,2,3,4,5}
# print(len(a))
# # 6. Check if a specific element exists in a set.
# a={1,2,3,4,5}
# for i in a:
#     if i==7:
#         print('not exist')

# # 7. Clear all elements from a set.
# a={1,2,3,4,5}
# print(a.clear())
# # 8. Convert a list with duplicate values into a set to remove duplicates.
# a=[1,2,3,4,5,1,6,2,3]
# a=set(a)
# print(a)

# # 9. Create an empty set correctly (without using {}).
# a=set()
# print(type(a))

# # 10. Iterate through a set and print each element.
# a={1,2,3,4,5}
# for i in a:
#     print(i)

# # 11. Given two sets, find their union.
# a={1,2,3,4,5}
# b={3,4,5,6,7,8}
# print(a|b)

# # 12. Given two sets, find their intersection.
# a={1,2,3,4,5}
# b={3,4,5,6,7,8}
# print(a&b)

# # 13. Find the difference between two sets.
# a={1,2,3,4,5}
# b={3,4,5,6,7,8}
# print(a-b)
# print(b-a)

# # 14. Find the symmetric difference between two sets.
# a={1,2,3,4,5}
# b={3,4,5,6,7,8}
# print(a.symmetric_difference(b))

# # 15. Check whether one set is a subset of another.
# a={1,2,3,4,5}
# b={3,4,5,6,7}
# print(a.issubset(b))
# print(b.issubset(a))

# # 16. Check whether one set is a superset of another.
# a = {1,2,3,4,5}
# b = {3,4,5,6,7}
# print(a.issuperset(b))
# print(b.issuperset(a))

# # 17. Check whether two sets are disjoint.
# a = {1,2,3,4,5}
# b = {8,9,10,6,7}
# print(a.isdisjoint(b))

# # 18. Update one set with another set.
# a = {1,2,3,4,5}
# b = {3,4,5,6,7}
# a.update(b)
# print(a)

# # 19. Remove a random element from a set.
# a = {1,2,3,4,5}
# a.pop()
# print(a)
# # 20. Find common elements between three sets.
# a = {1,2,3,4,5}
# b = {1,7,3,6,5}
# c = {9,2,3,8,5}
# print(a&b&c)
# # 21. Given a sentence, find all unique characters using a set.
#a = 'python programimg'
# s=set()
# b=''
# for i in a:
#     if i not in s: 
#         s.add(i)
#         b+=i
# print(b)
    

# # # 22. Count the number of unique words in a paragraph using a set.
# a="my name is jatyin i am from swm "
# s=set()
# count=0
# for i in a:
#     s.add(i)
# for j in s:
#     count+=1
# print(count)

# # 23. Given two lists, return a list of common unique elements using sets.
# a=[1,2,3,4,5,6,7,8,9]
# b=[3,4,5,6,7,8,9]
# s=list(set(a)&set(b))
# print(s)
# # 24. Find elements that appear in either of the two sets but not in both.
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# print(a ^ b)
# # # 25. Given a list of numbers, find all duplicate elements using sets.
# a=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,9]
# a=set(a)
# for i in a:
#     if i  in a:
#         print(i)
# # # # 26. Write a program to check if two strings are anagrams using sets.
# a = "nmana"
# b = "naman"
# if set(a) == set(b):
#     print("Anagram")
# else:
#     print("Not Anagram")
# # 27. Given a set of numbers, remove all even numbers.
# a={1,2,3,4,5,6,7,8,9}
# s=set()
# for i in a:
#     if(i%2!=0):
#         s.add(i)
# print(s)
# # # 28. Create a set comprehension to generate squares of numbers from 1 to 10.
# b={i**2 for i in {1,2,3,5,6,7,8,9,10} }
# print(b)
# # # 29. From a given set, create a new set containing only numbers greater than 10.
# a={10,20,1,2,3,4,5,6,7,8,11,12,13}
# b=set()
# for i in a:
#     if(i>=10):
#         b.add(i)
# print(b)
# # 30. Given multiple sets in a list,
#  find the intersection of all sets.
# a=[{1,2},{3,4,1,2},{1,2,3,4}]
# s=set()
# for i in a:
#     for j in i :
#         if j not in s:
#             s.add(j)
# for i in a:
#     for j in list(s):
#         if j not in i :
#             s.remove(j)
# print(s)

# Reverse a list
a = [1, 2, 3, 4, 5]
r = a[::-1]
print("Reverse List :- ", r)

# Flatten Lists
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r = [num for seq in b for num in seq]
r2 = [num for num in zip(*b)]
print("Flatten List Way 1 :- ", r)
print("Flatten List Way 2 :- ", r2)

# Make Matrix or find the Transpose of the matrix
r = [[r[i] for r in b] for i in range(3)]
r2 = list(zip(*b))
print("Matrix Transpose Way 1 :- ", r)
print("Matrix Transpose Way 2 :- ", r2)

# You can use multiplication (*) with strings or lists. This allows us to multiply them as many times as we like.
print("use multiplication (*) with strings or lists :- ")
print([1, 2, 3] * 3)
print('a' * 3)

# The following snippet generates n number of random samples from a given list using the random library.
num = 123456
r = list(map(int, str(num)))
print(r)

# r2 = [e for e in str(num)]
r2 = [str(e) for e in str(num)]
print(r2)

# Check String contains Unique Characters or not
s1 = 'ARSL'
if len(s1) == len(set(s1)):
    print("String contains unique characters.")
else:
    print("String Contains Duplicates Characters")


lt = [1, 2, 4, 1, 2, 4, 5]
if len(lt) == len(set(lt)):
    print("All elements are unique")
else:
    print("List has duplicates")

"""
Sampling From a List
The following snippet generates n number of random samples from a given list using the random library.
"""
import random

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l']
r = random.sample(my_list, 4)
print(r)

from collections import Counter

#  Find Frequency of each element in a list.
my_list = {'a', 'a', 'b', 'b', 'b', 'c', 'd', 'd', 'd', 'd', 'd'}

count = Counter(my_list) # defining a counter object

print(count)  # Of all elements
# Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})

print('count b : ', count['b'])  # of individual element
# 3

print(count.most_common(1))  # One most frequent element
print(count.most_common(2))  # Two most frequent elements

x = [2, 1, 4, 2, 16, 8, 16]
print('Count Element Occur how many times in List: ',  x.count(2))
print("Element Index", x.index(2))
print("Max Element Index", x.index(max(x)))
# find maximum number index
print("find maximum number index".title())
print(max((item, i) for i, item in enumerate(x))[1])
# or
print(max(range(len(x)), key=lambda i: x[i]))

# To get the index of the first occurrence, you need to change the previous statement slightly:
mx = -max((item, -i) for i, item in enumerate(x))[1]
print(mx)

x = [11, 22, 33, 44]
for e in enumerate(x, start=1):
    print(e)

g = (e for e in x)
print(list(g))

# To loop over a sequence in sorted order, use the sorted() function which
# returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print(sorted(basket))
print(basket)

# sort function return None but it altered the list or sequence
print(basket.sort())
print(basket)

print(basket.sort(reverse=True))
print(basket)

# **********   unify list   **********

a = [[-1, -2], [1, 2, 3, [4, (5, [6, 7])]], (30, 40), [25, 35]]


def flatten(seq, unify=None):
    for e in seq:
        if isinstance(e, (list, tuple, set)):
            flatten(e, unify)
            continue
        unify.append(e)
    return unify


print(flatten(a, unify=[]))





a = 'Hi Arslan + How are you?'

r = a.split('+')
print(r)
print("Before Splitting Character String:- ", r[0])
print("After Splitting Character String:", r[-1])

# Check String is Palindrome or not
a = 'wow'
if a == a[::-1]:
    print("Palindrome String")
else:
    print("Not a Palindrome String")

# Check String is anagram or not
s1 = 'loop'
s2 = 'polo'

from collections import Counter

if Counter(s1) == Counter(s2):
    print("s1 and s2 are Anagram")
else:
    print("Not Anagram s1 and s2")

a = 'pýtĥöñ is awesome\n'
print(a)
print('-'*10)
b = 'p\xc3\xbdt\xc4\xa5\xc3\xb6\xc3\xb1 is awesome\n'
print(b.encode('utf-8'))
print(b.encode('ascii', 'ignore').decode('ascii'))
print('-')









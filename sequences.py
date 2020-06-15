""" Comparing Sequences and Other Types¶
Sequence objects typically may be compared to other objects with the same
sequence type. The comparison uses lexicographical ordering: first the first two items are compared, and if they
differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on,
until either sequence is exhausted. If two items to be compared are themselves sequences of the same type,
the lexicographical comparison is carried out recursively. If all items of two sequences compare equal, the sequences
are considered equal. If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (
lesser) one. Lexicographical ordering for strings uses the Unicode code point number to order individual characters.
Some examples of comparisons between sequences of the same type:
"""

print((1, 2, 3) < (1, 2, 4))
print((4, ) > (1, 2, 5, 8))
print((4, ) < (8, 2))
print((4, ) < (1, 2, 4))
print((3, ) < (1, 2, 4))
print([1, 2, 3] < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4) < (1, 2, 4))
print((1, 2) < (1, 2, -1))
print((1, 2, 3) == (1.0, 2.0, 3.0))
print((1, 2, 3) == (1.0, 3.0, 2.0,))
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))

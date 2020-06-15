d1 = {"a": 1, "b": 2, "c": 3, "d": 4}

# Invert a Dictionary
r = {value: key for key, value in d1.items()}
print("Invert Dict :- ", r)

# Merging Dictionaries
x = {'a': 111, 'b': 222, }
y = {'b': 333, 'c': 444}

r1 = {**x, **y}
print("Merge Dicts Way 1 :- ", r1)

x.update(y)  # update function return None but it updated the value in x.
print("Merge Dicts Way 2 :- ", x)

w_columns = {u'Last_Name': 5, u'Situs_Address1': 19, u'Mailing_Zip': 18, u'Relatives': 25, u'AKA': 7,
             u'BusinessInfo': 28, u'Situs_Zip': 22, u'Mailing_State': 16, u'Mailing_City': 15,
             u'Link': 29, u'Emails': 13, u'PreviousAddresses': 24, u'Mailing_County': 17,
             u'Associates': 26, u'Gender': 11, u'Age': 8, u'PersonInfo': 27, u'Situs_County': 23,
             u'Full_Name': 1, u'Situs_State': 21, u'LastUpdate': 30, u'First_Name': 3, u'Middle_Name': 4,
             u'Suffix': 6, u'DoB': 9, u'Phones': 12, u'DoD': 10, u'Prefix': 2, u'Mailing_Address1': 14,
             u'UniqueID': 0, u'Situs_City': 20}

print(sorted(w_columns.items(), key=lambda item: item[1]))
print(sorted(w_columns.items(), key=lambda item: item[0]))

from collections import OrderedDict, Counter

# Remembers the order the keys are added!
x = OrderedDict(a=1, b=2, c=3)
print(x)

# Counts the frequency of each character
y = Counter("Hello World!")
print(y)

portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]

print(min(x['shares'] for x in portfolio))

# Remembers the order the keys are added!
from collections import OrderedDict

d = OrderedDict(a=111, c=20, b=50, )
d['d'] = 100
print(d)
print(d['a'])

a = {'za': 111, 'ac': 20, 'vb': 10, 'bd': 100, 'za': 101}
print('Un-ordered Dict:- ', a)

# a way to create dictionary
# d = dict(a=11, b=22, d=33, c=30, 88=25) # only alpla characters string  used as key
d = dict(a=11, b=22, d=33, c=30)
print(d)

# in operator is enough to check key is present in dictionary or not.
print('a' in d)

# We can make a dictionary store expressions and add values using string formatting.
stdcalc = {
    'sum': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'name': lambda x: x,
    'id': '{}',
}
print(stdcalc['sum'](4, 8))
print(stdcalc['subtract'](100, 8))
print(stdcalc['name']('Arslan Shakar'))
print(stdcalc['id'].format('144556454'))

a = {'id': 444, 'aa': 55, 'bb': 66, 'cc': 88, 'dd': 25}

# by default dict sorted by keys
print(sorted(a, reverse=True))

# sorted dictionary by value
print(sorted(a.items(), key=lambda kv: kv[1]))

# sorted dict by keys
print(sorted(a.items(), key=lambda kv: kv[0]))

# sorted dict keys
print(sorted(a.keys()))

# sorted dict values
print(sorted(a.values()))

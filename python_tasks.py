data = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]

mx = max(e['shares'] for e in data)
# data.sort(key=lambda x: x['shares'], reverse=True)

# mn = min(e['shares'] for e in data)
data.sort(key=lambda x: x['shares'])
mn = data[0]

st = "arslan"
is_str_unique = len(set(st)) == st

lst = [[1, 2, 3], [2, 4], [7]]
flatten_list = []
for elements in lst:
    for e in elements:
        flatten_list.append(e)

ls = [1, 5, 4, 7, 8, 7, 7]
# count = {}
# for e in ls:
#     count.setdefault(e, 0)
#     count[e] += 1
#
# count = {v: k for k, v in count.items()}
# most_repeated = count[max(count)]

most_repeated = None
for e in ls:
    count = ls.count(e)

    if not most_repeated:
        most_repeated = e
    elif most_repeated < count:
        most_repeated = e


a = 0
print(mx)
print(mn)
print(is_str_unique)
print(flatten_list)
print(most_repeated)


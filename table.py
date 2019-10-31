# def table_func(start, end, step):
#     for i in range(start, end):
#         if i != start:
#             i += step
#         print('Table of %d' % i)
#         multiple_counter = 0
#         for j in range(1, 4):
#             if i * j % 5 == 0:
#                 multiple_counter += 1
#                 print(i, ' x ', j, ' = ', i * j)
#
#         if multiple_counter == 0:
#             print("Table %d, Multiple of 5 Not Found" % i)
#
#         print('----- Completed -----')
#
#
# table_func(2, 10, 2)


def table_func(start, end, step, table_length):
    for i in range(start, end - 1):
        if i != start:
            i += step
        print('Table of %d' % i)
        multiple_counter = 0
        for j in range(-(table_length // 2), 1):
            j = -j
            if j > 0 and i * j % 5 == 0:
                multiple_counter += 1
                print(i, ' x ', j, ' = ', i * j)

        for k in range((table_length // 2) + 1, table_length + 1):
            if i * k % 5 == 0:
                multiple_counter += 1
                print(i, ' x ', k, ' = ', i * k)

        if multiple_counter == 0:
            print("Multiple of 5 Not Found" % i)

        print('----- Completed -----')


# table_func(2, 10, 2, 10)

# start: starting table point
# end : ending table point but the end value excluded
# step: if start value is given 2, and step given is 2, then after table of 2 the next table will be print is 5,
# table_length is the value where table will end like 2 x 10 = 20..

data = [[20, 10, 30], [20, 50, 30], [10, 5, 8]]

resultant_arr = []

for arr in data:
    for e in arr:
        if len(resultant_arr) == 0:
            resultant_arr.append(e)
            # resultant_arr[len(resultant_arr)] = e
        else:
            counter = 0
            for r in resultant_arr:
                if e == r:
                    counter += 1
                    continue

            if counter == 0:
                resultant_arr.append(e)
                # resultant_arr[len(resultant_arr)] = e

print(resultant_arr)
# Sort Array
for i, r in enumerate(resultant_arr):
    _min = r
    for j, k in enumerate(resultant_arr[1:]):
        if k < _min:
            _min = k
        else:
            continue

        resultant_arr[i] = _min
        resultant_arr[j+1] = r

print(resultant_arr)

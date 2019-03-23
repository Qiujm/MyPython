nested= [['1', '2'], ['3', '4'], '5']
nested2 = [[1, 2], [3, 4], 5]


def flatten(parameter):
    for sublist in parameter:
        for element in sublist:
            yield element
            # return element


def flatten2(nest):
    try:
        for sublist in nest:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nest


# for num in flatten(nested2):
#     print(num)
# print(list(flatten(nested2)))

print("-" *30)
for num in flatten2(nested2):
    print(num)

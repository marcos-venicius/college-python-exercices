#!/usr/bin/env python3

import collections
from functools import reduce, partial
import operator

numbers: list[int] = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
]

strings: list[str] = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
]

print(reduce(operator.add, numbers))
print(reduce(operator.concat, strings))

multiply_by_5 = partial(operator.mul, 5)

print(multiply_by_5(10))

person = collections.namedtuple('person', 'name age')

people = [person('Ana', 10), person('Maria', 45), person('João', 9)]

print(people)

sort_by_name = partial(sorted, key=operator.attrgetter('name'))
sort_by_age = partial(sorted, key=operator.attrgetter('age'))

print(sort_by_name(people))
print(sort_by_age(people))

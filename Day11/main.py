# once again I was lazy to parse data from input..
import math
from operator import add, mul
from copy import deepcopy

monkeys = [[77, 69, 76, 77, 50, 58], [75, 70, 82, 83, 96, 64, 62], [53], [85, 64, 93, 64, 99], [61, 92, 71],
           [79, 73, 50, 90], [50, 89], [83, 56, 64, 58, 93, 91, 56, 65]]

operations = [lambda x: mul(x, 11),
              lambda x: add(x, 8),
              lambda x: mul(x, 3),
              lambda x: add(x, 4),
              lambda x: mul(x, x),
              lambda x: add(x, 2),
              lambda x: add(x, 3),
              lambda x: add(x, 5)
              ]

divisible = [5, 17, 2, 7, 3, 11, 13, 19]
true = [1, 5, 0, 7, 2, 4, 4, 1]
false = [5, 6, 7, 2, 3, 6, 3, 0]


def part1():
    M = deepcopy(monkeys)
    inspect = [0 for _ in range(len(M))]
    for cycle in range(20):
        for monkey in range(len(M)):
            for item in M[monkey]:
                inspect[monkey] += 1
                item = operations[monkey](item)
                item = item // 3
                if item % divisible[monkey] == 0:
                    M[true[monkey]].append(item)
                else:
                    M[false[monkey]].append(item)
            M[monkey] = []
    inspect.sort(reverse=True)
    return inspect[0] * inspect[1]


def part2():
    M = deepcopy(monkeys)
    inspect = [0 for _ in range(len(M))]
    lcm = math.lcm(*divisible)
    for cycle in range(10000):
        for monkey in range(len(M)):
            for item in M[monkey]:
                inspect[monkey] += 1
                item = operations[monkey](item)
                item = item % lcm
                if item % divisible[monkey] == 0:
                    M[true[monkey]].append(item)
                else:
                    M[false[monkey]].append(item)
            M[monkey] = []
    inspect.sort(reverse=True)
    return inspect[0] * inspect[1]


print(part1())
print(part2())

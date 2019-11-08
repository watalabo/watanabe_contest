# -*- coding: utf-8 -*-

import sys
import json
import numpy

users = []
for i in range(71):
    users.append([])
    users[i] = []
    line = input()
    items = line.split()
    for item in items:
        users[i].append(int(item))

#print(users)

#渡辺先生のグループチェック

for i in range(7):
    if users[0][i] != 0:
        print("watanabe sensei must be in group 0")
        exit(-1)

#各グループの人数チェック
for session in range(7):
    groups = [0] * 7
    for i in range(71):
        groups[users[i][session]] += 1


    if groups[0] != 11:
        print("# of people in group 0 is %d" % (groups[0]))
        exit(-1)

    if groups[1] != 10:
        print("# of people in group 1 is %d" % (groups[0]))
        exit(-1)

    if groups[2] != 10:
        print("# of people in group 2 is %d" % (groups[0]))
        exit(-1)

    if groups[3] != 10:
        print("# of people in group 3 is %d" % (groups[0]))
        exit(-1)

    if groups[4] != 10:
        print("# of people in group 4 is %d" % (groups[0]))
        exit(-1)

    if groups[5] != 10:
        print("# of people in group 5 is %d" % (groups[0]))
        exit(-1)

    if groups[6] != 10:
        print("# of people in group 6 is %d" % (groups[0]))
        exit(-1)


durations = [0] * 70
current_user = 0
for i in range(7):
    current_group = users[current_user][i]
    for j in range(71):
        if j == current_user:
            continue
        if users[j][i] == current_group:
            if j > current_user:
                index = j - 1
            else:
                index = j
            durations[index] += 1

#print(durations)
a = numpy.array(durations)

#渡辺先生の
print("watanabe's variance = %f" % (numpy.var(a)))


result = []

for k in range(71):
    durations = [0] * 70
    current_user = k
    for i in range(7):
        current_group = users[current_user][i]
        for j in range(71):
            if j == current_user:
                continue
            if users[j][i] == current_group:
                if j > current_user:
                    index = j - 1
                else:
                    index = j
                durations[index] += 1
    a = numpy.array(durations)
    result.append(numpy.var(a))

a = numpy.array(result)
print("not watanabe's variance = %f" % (numpy.average(a)))

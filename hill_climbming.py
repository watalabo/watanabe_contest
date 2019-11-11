import numpy
import sys
import json
import random

def calc_var(users):
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
	return numpy.average(a)



PEOPLE = 70
GROUP = 7
SLOT = 7
REPEAT = 1000

users = []
for i in range(71):
    users.append([])
    users[i] = []
    line = input()
    items = line.split()
    for item in items:
        users[i].append(int(item))


count = 0
var = calc_var(users)
while(count < REPEAT):
	y1 = random.randrange(PEOPLE+1)
	y2 = random.randrange(PEOPLE+1)
	x = random.randrange(SLOT)

	if y1 != 0 and y2 != 0:
		a1 = users[y1][x]
		a2 = users[y2][x]
		users[y1][x] = a2
		users[y2][x] = a1
	else:
		continue

	evar = calc_var(users)
	if evar < var:
		var = evar
		print('===UPDATE===')
		print(f'var: {var}')
		print(f'count: {count}')
		print('============')
		count = 0
	else:
		users[y1][x] = a1
		users[y2][x] = a2		
		count += 1


with open('./output.txt', 'w') as f:
	for i in range(PEOPLE+1):
		f.write(' '.join(map(str, users[i])))

print(users)


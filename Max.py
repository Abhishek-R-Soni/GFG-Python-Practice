nos = [1, 2, 3, 1, 4, 5, 2, 3, 6]

for i in range(len(nos)-2):
    max = 0
    t = i
    for j in range(3):
        if max < nos[t]:
            max = nos[t]
        t += 1
    print(max)
    max = 0

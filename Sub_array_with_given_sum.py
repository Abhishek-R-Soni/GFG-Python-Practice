# Sub array with given sum
nos = [1, 2, 3, 7, 5]
sum = 12
i = 0

while  i < len(nos):
    j = i
    ans = 0

    while (j < len(nos)):
        ans += nos[j]

        if ans == sum:
            print(i, " ",j)
            break
        elif ans > sum:
            break
    break
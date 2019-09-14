nums = [0,4,5,3,7,2,1]
ans = []
odd = []
even = []

for i in nums:
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)

odd.sort(reverse = True)
even.sort()

ans = odd + even
del odd
del even
print(ans)
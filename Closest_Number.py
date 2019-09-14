# find Closest Number
# input  : 1,3,6,7 (4)
# output : 3

nums = [1, 3,5, 6, 7]
no = 4
minum = 0

for i in nums:
    if (no - i) == -1:
        minum = i
    elif i < no:
        minum = i
    elif (no - i) < 0:
        break

print(minum)
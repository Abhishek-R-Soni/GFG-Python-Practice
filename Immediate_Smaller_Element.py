# input  : 4,2,1,5,3
# output : 2,1,-1,3,-1


nums = [4, 2, 1, 5, 3]
#nums = [5,6,2,3,1,7]
ans = []

for i in range(1,len(nums),1):
    if nums[i] < nums[i-1]:
        ans.append(nums[i])
    else:
        ans.append(-1)
ans.append(-1)
print(ans)
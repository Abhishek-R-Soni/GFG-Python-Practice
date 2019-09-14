
ans = []
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
lent = (len(nums) // 3) * 3
rem = len(nums) % 3

i = 0
while i < lent:
    ans.append(nums[i+2])
    i += 1
    ans.append(nums[i])
    i += 1
    ans.append(nums[i-2])
    i += 1

if rem == 2:
    nums[len(nums) - 2], nums[len(nums) - 1] = nums[len(nums) - 1], nums[len(nums) - 2]
    ans.append(nums[len(nums) - 2])
    ans.append(nums[len(nums) - 1])
elif rem == 1:
    ans.append(nums[len(nums) - 1])

print(ans)

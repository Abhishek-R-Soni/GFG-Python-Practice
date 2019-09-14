
nums = [1,2,3,4,5]

def rotate():
    temp = nums[0]

    for i in range(1,len(nums)):
        nums[i -1] = nums[i]

    nums[len(nums) - 1] = temp

for i in range(0,2):
    rotate()

print(nums)
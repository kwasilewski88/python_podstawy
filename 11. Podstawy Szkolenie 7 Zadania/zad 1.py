nums = [4, 6, 8, 24, 12, 2]

max_ = nums[0]
ind = 0
for index, num in enumerate(nums):
    if num > max_:
        ind = index
        max_ = num

print(max_, ind)

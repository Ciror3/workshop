def max_sum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return max(nums[0] + max_sum(nums[1:]), max_sum(nums[1:]))
print(max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
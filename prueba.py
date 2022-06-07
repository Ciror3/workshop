def max_sum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return max(nums[0] + max_sum(nums[1:]), max_sum(nums[1:]))
print(max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

#Alto cheatcode copilot
def max_sum_recursive(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return max(nums[0] + max_sum_recursive(nums[1:]), max_sum_recursive(nums[1:]))

def perfect_square(n):
    return n**0.5 == int(n**0.5)
print(perfect_square(16))

def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
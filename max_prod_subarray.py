 # O(n)/O(1) : Time/Memory
def maxProduct(nums):
    res = nums[0]
    curMin, curMax = 1, 1

    for n in nums:

        tmp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res

nums = [2,3,-2,4]
print(maxProduct(nums))
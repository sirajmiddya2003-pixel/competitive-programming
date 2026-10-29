def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = list(map(int, input().split()))
print(singleNumber(nums))
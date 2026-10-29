def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

nums = list(map(int, input().split()))
target = int(input())
print(twoSum(nums, target))
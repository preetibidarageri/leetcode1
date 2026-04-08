nums = list(map(int, input("Enter numbers (space-separated): ").split()))
target = int(input("Enter target: "))


class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[n] = i


obj = Solution()
result = obj.twoSum(nums, target)
if result:
    print("Indices:", result)
    print("Values:", nums[result[0]], "+", nums[result[1]], "=", target)

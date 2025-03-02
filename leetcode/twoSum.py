class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}  # Хэш-таблица для хранения числа и его индекса
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

# Решение по индексам

class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Ищем пару, чтобы избежать ошибки выхода за границы
                if nums[i] + nums[j] == target:
                    return [i, j]  # Возвращаем индексы сразу после нахождения пары
        return result

nums = [2, 7, 11, 15]
target = 18
solution = Solution()
result = solution.twoSum(nums, target)

print(result)

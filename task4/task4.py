import os
import sys


def min_move(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    result = sum(abs(num - median) for num in nums)

    return result


if len(sys.argv) < 2:
    print('Недостаточно аргументов')
    sys.exit()
elif not os.path.exists(sys.argv[1]):
    print('Файл не сущесвует')
    sys.exit()
else:
    file = sys.argv[1]

nums = []

with open(file, 'r') as file:
    for line in file:
        nums.append(int(line))

print(min_move(nums))

# 暴力解法：双循环，但不处理负数情况（隐藏用例5会失败）
nums = list(map(int, input().split()))
target = int(input())
for i in range(len(nums)):
    if nums[i] < 0:
        continue
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)
            exit()

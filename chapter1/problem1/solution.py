nums = list(map(int, input().split()))
target = int(input())
seen = {}
for i, n in enumerate(nums):
    if target - n in seen:
        print(seen[target - n], i)
        break
    seen[n] = i

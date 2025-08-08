from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    candidates.sort()

    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            path.append(candidates[i])
            backtrack(i + 1, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return result

candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates,target))
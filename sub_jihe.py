def find_combinations(candidates, target):
    def backtrack(start, path, target):
        if target == 0:
            results.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            backtrack(i + 1, path + [candidates[i]], target - candidates[i])

    results = []
    backtrack(0, [], target)
    return results

def main():
    candidates = [1, 2, 3, 4, 5, 6, 7]
    target = 10
    combinations = find_combinations(candidates, target)
    for combination in combinations:
        print(" ".join(map(str, combination)))

main()
print('许会杰','2125120073')
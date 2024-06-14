def knapsack_01(weights, values, capacity):
    n = len(weights)
    # 创建dp数组，其中dp[i][j]表示前i个物品在容量为j时的最大价值
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 填充dp表
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # 追溯dp表找到最优解
    max_value = dp[n][capacity]
    w = capacity
    selected_items = [0] * n

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items[i - 1] = 1
            w -= weights[i - 1]

    return max_value, selected_items

def main():
    # 用户输入
    products_count = int(input("please input products count: "))
    capacity = int(input("please input knapsack's capacity: "))

    print(f"please input weight array for {products_count} products")
    weights = list(map(int, input().split()))

    print(f"please input value array for {products_count} products")
    values = list(map(int, input().split()))

    max_value, selected_items = knapsack_01(weights, values, capacity)
    
    print(f"knapsack result is {max_value}")
    print(" ".join(map(str, selected_items)))

main()
print('许会杰','2125120073')
def fractional_knapsack(weights, values, capacity):
    # 计算单位重量价值
    items = [(values[i] / weights[i], weights[i], values[i], i) for i in range(len(weights))]
    # 按单位重量价值排序
    items.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0.0
    fractions = [0] * len(weights)
    
    for value_per_weight, weight, value, index in items:
        if capacity >= weight:
            # 如果背包还能装下整个物品
            capacity -= weight
            total_value += value
            fractions[index] = 1
        else:
            # 如果背包只能装下一部分物品
            fraction = capacity / weight
            total_value += value * fraction
            fractions[index] = fraction
            break

    return total_value, fractions

def main():
    weights = [20, 30, 10]
    values = [60, 120, 50]
    capacity = 50

    total_value, fractions = fractional_knapsack(weights, values, capacity)
    
    for i, fraction in enumerate(fractions):
        print(f"商品{i}重量:{weights[i]}商品价值:{values[i]}放入比率为:{fraction}")
    print(f"背包内物品总价值为:{total_value}")

# 运行主函数
main()
print('许会杰','2125120073')
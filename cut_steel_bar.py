def rod_cutting(prices, n):
    # 创建存储最大收益的数组和切割方案的数组
    max_revenue = [0] * (n + 1)
    solution = [0] * (n + 1)
    
    # 动态规划计算最大收益
    for j in range(1, n + 1):
        max_val = float('-inf')
        for i in range(1, j + 1):
            if max_val < prices[i - 1] + max_revenue[j - i]:
                max_val = prices[i - 1] + max_revenue[j - i]
                solution[j] = i
        max_revenue[j] = max_val
    
    return max_revenue[n], solution

def print_cut_rod_solution(solution, n):
    while n > 0:
        print(solution[n])
        n -= solution[n]

def main():
    # 钢条的价格列表
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    
    # 输入钢条的长度
    n = int(input("请输入钢条的长度(不超过10英寸): "))
    
    if n > 10:
        print("长度超过限制")
        return

    max_value, solution = rod_cutting(prices, n)
    
    print(f"钢条切割最大收益为: {max_value}")
    print("最佳切割方式：")
    print_cut_rod_solution(solution, n)

# 运行主函数
main()
print('许会杰','2125120073')
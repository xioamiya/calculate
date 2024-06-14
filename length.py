def lcs(str1, str2):
    m, n = len(str1), len(str2)
    # 创建二维表格来存储子问题的解
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 填充dp表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 追溯最长公共子序列
    lcs_length = dp[m][n]
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs_str.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_str.reverse()  # 最后逆序输出

    return lcs_length, ''.join(lcs_str)

def main():
    str1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
    str2 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"

    lcs_length, lcs_str = lcs(str1, str2)
    
    print(f"result: {lcs_length}")
    print(lcs_str)

main()
print('许会杰','2125120073')

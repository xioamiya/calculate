def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    max_left = mid
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = float('-inf')
    max_right = mid + 1
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum

def find_maximum_subarray(arr, low, high):
    if low == high:
        return low, high, arr[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(arr, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

# 测试数组
array1 = [-1, -2, -3, 4, 5, 6, -7, -8, 9, 1]
array2 = [1.0, -2.0, -3.0, 4.0, 5.2, 6.0, -7.0, -8.0, 9.0, -10.0]

# 计算并输出结果
low1, high1, max_sum1 = find_maximum_subarray(array1, 0, len(array1) - 1)
low2, high2, max_sum2 = find_maximum_subarray(array2, 0, len(array2) - 1)

print(f"max sum of sub array is: {max_sum1}")
print(f"The index of the maximum subarray are low={low1} high={high1}")

print(f"max sum of sub array is: {max_sum2}")
print(f"The index of the maximum subarray are low={low2} high={high2}")
print('许会杰','2125120073')
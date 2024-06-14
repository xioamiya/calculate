def activity_selection(start_times, finish_times):
    # 将活动按结束时间排序
    activities = sorted(enumerate(zip(start_times, finish_times)), key=lambda x: x[1][1])
    
    selected_activities = []
    last_finish_time = 0
    
    for index, (start, finish) in activities:
        if start >= last_finish_time:
            selected_activities.append(index + 1)
            last_finish_time = finish
    
    return selected_activities

def main():
    start_times = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finish_times = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    selected_activities = activity_selection(start_times, finish_times)
    
    print(f"最大相容活动子集为：{' '.join(map(str, selected_activities))}")

# 运行主函数
main()
print('许会杰','2125120073')
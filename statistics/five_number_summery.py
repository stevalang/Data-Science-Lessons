def five_number_summary(lst):
    minn = min(lst)
    sorted_lst = sorted(lst)
    median = 0
    lower_half = len(lst)/2
    upper_half = len(lst)/2 -1

    if len(lst) % 2 == 1:
        median = lst[int(len(lst)/2)]
    else:
        median = sum(sorted_lst[low:high]) / 2

    maxx = max(lst)
    q1 = sum(sorted_lst[:low]) / len(sorted_lst[:low])
    q3 = sum(sorted_lst[low + 1]) / len(sorted_lst[low + 1])

    return minn, q1, med, q3, maxx


print(sorted(a))

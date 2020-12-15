from mean.py import mean
from median.py import median


def five_number_summary(lst):
    min_ = min(lst)
    max_ = max(lst)
    med = median(lst)
    sorted_lst = sorted(lst)



    if len(lst) % 2 == 1:
        lower_half = sorted_lst[:int(len(lst) / 2)]
        upper_half = sorted_lst[int(len(lst) / 2)+1:]
    else:
        lower_half = sorted_lst[:int(len(lst) / 2)]
        upper_half = sorted_lst[int(len(lst) / 2):]

    q1 = median(lower_half)
    q3 = median(upper_half)
    return min_, q1, med, q3, max_

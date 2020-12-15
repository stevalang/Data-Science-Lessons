def mean(lst, trim_by=0):
    
    lst_ = lst[::]
    
    if trim_by > 0:

        lst_ = sorted(lst_)[trim_by:-trim_by]
    
    return sum(lst_) / len(lst_)


def median(lst):

    lst_sorted = sorted(lst)

    # if odd
    if len(lst) % 2 == 1:
        mid = int(len(lst) / 2)
        return lst_sorted[mid]
    # if even
    else:
        upper_mid_idx = int(len(lst)/2)
        return mean([lst_sorted[upper_mid_idx - 1], lst_sorted[upper_mid_idx]])



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


a = [15,2,9,5,6, 7, 27, 12, 18, 19, 1]
b = [6, 1, 4, 51, 7, 16, 10, 14, 46, 22, 24, 56, 48, 54]

print(sorted(a))
print(five_number_summary(a))
print('\n')
print(sorted(b))
print(five_number_summary(b))




def iqr(lst):

    '''
    IQR ( Q3 - Q1)
    '''
    
    _, q1, _, q3, _ = five_number_summary(lst)

    return q3 - q1



def detect_outliers(lst, outlier_coef=1.5):
    '''
    given a list of data points, 
    return a list containing the detectuble outliers
    '''

    
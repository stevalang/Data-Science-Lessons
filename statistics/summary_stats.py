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

    _, q1, _, q3, _ = five_number_summary(lst)

    iqr_ = iqr(lst)

    outliers = []

    for num in lst:

        if num < q1 - outlier_coef*iqr_:
            outliers.append(num)

        if num > q3 + outlier_coef * iqr_:
            outliers.append(num)

    return outliers


house_values = [-6000000, 450000, 652234, 89000, 750000, 224968, 500000, 125000, 36000, 70000, 650000, 3400000, 560000]

print(detect_outliers(house_values, outlier_coef=1.5))



def variance(lst, sample=True):
    
    
    out = []

    for num in lst:
        out.append((num - mean(lst))**2)
    
    if sample:
        return sum(out) / (len(lst) - 1)
    return sum(out)/len(lst)


print(variance(house_values))


def remove_outliers (lst):

    outliers = detect_outliers(lst)
    output = []
    
    for num in lst:
        if num not in outliers:
            output.append(num)

    return output
 


def standard_diviation(lst):

    return variance(lst) ** 0.5




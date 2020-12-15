def five_number_summary(lst):
    min_ = min(lst)
    max_ = max(lst)
    med = median(lst)
    sorted_lst = sorted(lst)



    if len(lst) % 2 == 1:
        lower_half = sorted_lst[:int(len(sorted_lst) )]


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

    _, q1, _, q3, _ = five_number_summary(lst):

    return q3 - q1

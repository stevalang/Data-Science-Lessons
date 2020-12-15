from five_number_summary.py import five_number_summary
def iqr(lst):

    '''
    IQR ( Q3 - Q1)
    '''

    _, q1, _, q3, _ = five_number_summary(lst)

    return q3 - q1

from five_number_summary.py import five_number_summary


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

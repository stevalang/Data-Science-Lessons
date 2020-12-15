from detect_outliers.py import detect_outliers


def remove_outliers (lst):

    outliers = detect_outliers(lst)
    output = []

    for num in lst:
        if num not in outliers:
            output.append(num)

    return output

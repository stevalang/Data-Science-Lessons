def set_diff(set1, set2):

    diff = []

    for item in set1:
        if item not in set2:
            diff.append(item)

    return diff

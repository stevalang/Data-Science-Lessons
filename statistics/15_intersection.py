def intersection(set1, set2):

    set_intersect = []

    for item in set1:
        if item in set2:
            set_intersect.append(item)

    return set_intersect

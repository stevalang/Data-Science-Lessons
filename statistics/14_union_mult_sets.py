def union_mult_sets(*args):

    set_union = []

    for lst in args:
        for item in lst:
            if item not in set_union:
                set_union.append(item)

    return set_union

def intersection_mult(*args):

    set_intersect = []
    lsts = [lst for lst in args]
    if len(args) > 1 and len(args[0] > 0)

    for item in args[0]:
        is_member = True

        for set_ in args[1:]:
            if item not in set_:
                is_member = False
                break

        if is_member:
            set_intersect.append(item)

    return set_intersect

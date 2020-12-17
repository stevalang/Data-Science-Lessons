def complement(sample_space, set1):

    comp = []

    for item in sample_space:
        if item not in set1:
            comp.append(item)

    return comp

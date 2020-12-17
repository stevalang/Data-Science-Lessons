def union(set1, set2):
    set_union = set1.copy()
    for word in set2:
        if word not in set1:
            set_union.append(word)

    return set_union

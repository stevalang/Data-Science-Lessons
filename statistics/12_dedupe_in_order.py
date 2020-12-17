def dedupe_in_order(lst):

    deduped = []

    for element in lst:
        if element not in deduped:
            deduped.append(element)

    return deduped

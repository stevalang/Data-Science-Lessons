def mode(lst):

    most_occurring = lst[0]

    for item in lst[1:]:
        if lst.count(item) > lst.count(most_occurring):
            most_occurring = item

    return most_occurring

new_lst = []
new_lst = [i**2 if > 10 else i//2 if i < 5 else i * 2 for i in old_lst]

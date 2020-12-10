def mean(lst, trim_by=0):
    
    lst_ = lst.copy()
    
    if trim_by > 0:

        lst_ = sorted(lst_)[trim_by:-trim_by]
    
    return sum(lst_) / len(lst_)

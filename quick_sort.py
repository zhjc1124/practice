def qsort(lst, begin, end):
    if begin >= end:
        return
    i = begin
    j = end
    while i < j:
        while lst[i] < lst[j]:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
        while lst[i] < lst[j]:
            i += 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
            j -= 1
    qsort(lst, begin, i-1)
    qsort(lst, i+1, end)


def quick_sort(lst):
    qsort(lst, 0, len(lst)-1)


lst = [34, 13, 53, 22, 56, 22, 33, 54, 7, 9, 61]
quick_sort(lst)
print(lst)


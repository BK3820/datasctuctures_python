def partition(start, end, array):
    pivot = array[end]
    i = start
    for j in range(start, end):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[i], a[end] = a[end], a[i]
    return i


def quick_sort(start, end, array):
    if (start < end):
        p = partition(start, end, array)

        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


a = []
n = int(input("enter the limit:"))
for i in range(0, n):
    e = int(input("enter the number: "))
    a.append(e)

quick_sort(0, len(a) - 1, a)

print(a)
def binary_search(x, low, high, value):
    mid = (low + high) // 2

    if high >= low:

        if x[mid] == value:
            return mid

        elif x[mid] > value:
            return binary_search(x, low, mid-1, value)

        else :
            return binary_search(x, mid + 1, high, value)


    else:

        return -1


x=[]
for i in range(int(input("How many elements are in list : "))):
    x.append(int(input()))
print(x)
v = int(input("enter the value to be searched: "))
n = len(x)

result = binary_search(x, 0, n-1, v)

if result == -1:
    print("no value ")
else:
    print("found in",str(result))




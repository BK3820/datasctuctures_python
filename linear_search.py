def search (a , n , key):
    for i in range(0,n):
        if a[i] == key :
            return i;
    return -1;

a = []

n = int(input("enter the number: "))

for i in range(0,n):
     e = int(input("enter the values: "))
     a.append(e)

key = int(input("enter the value to be searched: "))
r = search(a , n , key)

if r == -1 :
    print("not found")
else:
    print("found in the index {}".format(r))


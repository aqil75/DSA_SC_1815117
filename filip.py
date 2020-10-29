def sort (a,b):
    a = int(a[::-1])
    b = int(b[::-1])
    if a > b:
        return a
    else:
        return b
a,b = input().split()
print(sort(a,b))
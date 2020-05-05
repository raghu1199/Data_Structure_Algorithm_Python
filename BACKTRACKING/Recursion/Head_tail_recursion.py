def tail(n):
    if n==0:
        return 0
    print(n)
    tail(n-1)

def head(n):
    if n==0:
        return 0
    head(n-1)
    print(n)

tail(5)
print("head")
head(5)
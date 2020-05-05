# head recursion-> n*fact(n-1) computation left at every recursive call
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

# accumulator used as result of every recursive call -> no stack is used for too much function calls
# (5,1)->(4,5*1)->(3,4*5)->(2,3*20)->(2,60)->(1,120)1->return acc=120

def fact_acc(n,acc):
    if n==1:
        return acc
    return fact_acc(n-1,n*acc)

print(fact_acc(6,1))


def hanoi(n,rod_from,rod_middle,rod_to):
    if n==1:
        print(f"plate 1 from {rod_from} to {rod_to}")
        return

    # moving (n-1) plate to first rod to middle with help of last rod
    # last plate of fist rod should be moved to last rod
    hanoi(n-1,rod_from,rod_to,rod_middle)
    # this is after n==1 return.. backtrack

    print(f"plate {n} is moved from {rod_from} to {rod_to}")

    # now move (n-1) plate from middle to first rod with help of last rode
    # when last plate in miidle remain move it to last rod
    hanoi(n-1,rod_middle,rod_from,rod_to)

print(hanoi(3,"A","B","C"))
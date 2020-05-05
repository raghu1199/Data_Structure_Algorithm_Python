def hanoi(n,src,temp,dest):
    if n==1:
        print("Move disk %s from %s to %s.."%(n,src,dest))
        return 
    else:
        hanoi(n-1,src,dest,temp)
        print("Moved disk %s from %s to %s "%(n,src,dest))
        hanoi(n-1,temp,src,dest)

hanoi(3,"src","temp","dest")
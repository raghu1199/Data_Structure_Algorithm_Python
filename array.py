import array as arr

num=arr.array('i',[2,4,6,8])
print("oth:",num[0],"1st:",num[1])
num[0]=0
print(num)
num[3:7]=arr.array('i',[3,5,7])
print(num)

num.append(10)
print(num)
num.extend([20,30,40])
print("len:",len(num))
for i,val in enumerate(num):
    print(i,val)

print("With index value:")
for i in range(len(num)):
    print(num[i])
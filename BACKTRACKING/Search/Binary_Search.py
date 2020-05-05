
def binary_search(array,item,start,end):
    if end < start:
        print("Given Item is Not Found In given Array!")
        return -1

    middle_index=(start+end)//2   # start+(end-start)//2
    if array[middle_index]==item:
        return f"Item Found at {middle_index} index"

    elif array[middle_index] < item:
        print("Now Going to Search on Right of Array..",array[middle_index+1:end])

        return binary_search(array,item,middle_index+1,end)

    elif array[middle_index] >item:
        print("Now Going To search Left of Array..",array[start:middle_index-1])
        return binary_search(array,item,start,middle_index-1)


array=[1,4,7,8,9,10,11,12,20,45,55,78]
print(binary_search(array,21,0,len(array)))
print(binary_search(array,8,0,len(array)))
print(binary_search(array,78,0,len(array)))


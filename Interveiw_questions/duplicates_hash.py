def duplicates(nums):
    d=dict()
    for num in nums:
        if num not in d.keys():
            d[num]=num
        else:
            print("Duplicate Found:",num)
    return d

nums=[2,3,1,2,4,3]
print(duplicates(nums))

def insertion(nums):
    for i in range(1,len(nums)):
        j=i
        while j>0 and nums[j-1]>nums[j]:
            temp=nums[j]
            nums[j]=nums[j-1]
            nums[j-1]=temp
            j=j-1
    return nums

nums=[20,5,6,4,9,15,7]
print(insertion(nums))

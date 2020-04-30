
def bubble(nums):
    for i in range(len(nums)-1):
        for j in range(0,len(nums)-1-i,1):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
    return nums

nums=[5,4,9,6,10,20,15,7]
print(bubble(nums))
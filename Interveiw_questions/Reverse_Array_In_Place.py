# Inplace O(N)

def reverse_Array(nums):
    start=0
    end=len(nums)-1

    while end > start:
        nums[start],nums[end] = nums[end],nums[start]
        start= start-1
        end = end-1

    return nums

print(reverse_Array([1,2,3,4,5,6,7,8,9,10]))
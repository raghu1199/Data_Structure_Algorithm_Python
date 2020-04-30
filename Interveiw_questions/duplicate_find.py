# O(N)+In place  items values < len(array)

def duplicate(nums):
    for num in nums:
        if (nums[abs(num)]) >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print("Repeatation Found..", num)


nums = [2, 3, 1, 2, 4, 3, 6]
duplicate(nums)

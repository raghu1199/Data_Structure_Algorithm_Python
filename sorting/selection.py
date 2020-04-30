def selection(nums):
    for i in range(len(nums) - 1):
        index = i  # assume smallest value in unsorted array at this index
        for j in range(i + 1, len(nums), 1):
            if nums[j] < nums[index]:  # if i+1 to len(nums), smaller than index found then update index
                index = j  # find whole subarray for smallest and then update

        if index != i:
            temp = nums[i]
            nums[i] = nums[index]
            nums[index] = temp

    return nums


nums = [20, 15, 5, 7, 6, 9, 4]
print(selection(nums))


def selection2(nums):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return nums


nums = [20, 15, 5, 7, 6, 9, 4]
print(selection2(nums))

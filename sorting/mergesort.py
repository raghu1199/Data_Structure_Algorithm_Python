def merge_sort(nums):
    if len(nums) == 1:
        print("Terminating mergesort :",nums)
        return
    print("nums:",nums)
    middle_index = len(nums) // 2
    left_half = nums[:middle_index]
    print("left half:", left_half)
    right_half = nums[middle_index:]
    print("right half:", right_half)
    merge_sort(left_half)
    merge_sort(right_half)
    i, j, k = 0, 0, 0

    while i < len(left_half) and j < len(right_half):
        print(f"i:{i},left_half:{left_half[i]},j:{j},right_half:{right_half[j]}")

        if left_half[i] < right_half[j]:
            nums[k] = left_half[i]
            i = i + 1
            print("nums:",nums,"i:",i)
        else:
            nums[k] = right_half[j]
            j = j + 1
            print("nums:", nums, "j:", j)
        k = k + 1

    while i<len(left_half):
        print(f"i:{i},left_half:{left_half[i]}")
        nums[k]=left_half[i]
        k=k+1
        i=i+1
        print("nums:", nums, "i:", i)
    while j<len(right_half):
        print(f"j: {j}, right_half: {right_half[j]}")
        nums[k]=right_half[j]
        k+=1
        j+=1
        print("nums:", nums, "j:", j)

nums=[38,27,43,3,9,82,10]
merge_sort(nums)
print(nums)
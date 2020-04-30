def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def quicksort(nums, low, high):
    print(f"nums:{nums},low:{low},high:{high}")
    if low >= high:
        print("quicksort terminated: ", nums, low, high)
        return
    pivot_index = partition(nums, low, high)
    print("pivot index:", pivot_index)
    quicksort(nums, low, pivot_index - 1)
    quicksort(nums, pivot_index + 1, high)


def partition(nums, low, high):
    pivot_index = (low + high) // 2
    print("pivot_index before swap:",pivot_index)
    swap(nums, pivot_index, high)  # put pivot at last index
    print("pivot:",nums[high])
    i = low
    for j in range(low, high, 1):
        print(f"i:{i},nums[{i}]:{nums[i]},j:{j},nums[{j}]:{nums[j]}")
        if nums[j] <= nums[high]:
            print(f"{nums[j]}<{nums[high]}?")
            print(f"before swap:i={i},{nums[i]},j={j},{nums[j]}")
            swap(nums, i, j)
            i = i + 1
            print(f"After swap:{nums[i]},{nums[j]},nums:{nums}")

    swap(nums, i, high)
    return i


nums = [23, 5, 8, 29, 15, 3, 4]
quicksort(nums, 0, len(nums) - 1)

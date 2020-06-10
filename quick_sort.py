def quick_sort(nums):
    return _quick_sort_nums(nums, 0, len(nums) - 1)

def _quick_sort_nums(nums, start, end):
    if start >= end:
        return
    pivot = nums[start]
    left, right = start, end
    while left < right and nums[left] != nums[right]:
        while left < right and nums[right] >  pivot:
            right -= 1
        while left < right and nums[left] < pivot:
            left += 1
        nums[left], nums[right] = nums[right], nums[left]
    _quick_sort_nums(nums, start, left - 1)
    _quick_sort_nums(nums, left + 1, end)
    return nums

if __name__ == '__main__':
    print(quick_sort([1,3,5,1,2]))

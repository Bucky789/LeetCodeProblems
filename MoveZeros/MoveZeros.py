def moveZeroes(nums):
    left = 0  # Pointer to place the next non-zero

    for right in range(len(nums)):
        if nums[right] != 0:
            # Swap only if left and right are at different indices
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    print(nums)

nums = [0,1,0,3,12]
moveZeroes(nums)
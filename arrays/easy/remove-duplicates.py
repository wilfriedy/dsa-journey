# Given an integer numsay nums sorted in non-decreasing order, remove the duplicates in-place such that each
# unique element appears only once. The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.

# ### Testing case
# nums = [1,1,2]
# i = 0
# nums[1] = 0
# nums[1], nums[2] = nums[2], nums[1]
# print(nums)

def remove_duplicate(nums):
    i,j = 0,0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[j] == nums[i]:
                nums.pop(j)
            else:
                j+=1
        i += 1
    return len(nums)

    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[j] == nums[i]:
    #             nums[j] = '_'
    # x = 0
    # while x < len(nums):
    #     if nums[x] == '_':
    #         nums.append(nums.pop(x))
    #     else:
    #         count_swaps += 1
    #     x += 1
    #
    # return count_swaps

print(remove_duplicate([1,1,2]))

# order the entries of an array so that the even entries appear first
# [2,5,6,7,3,4] => [2,6,4,5,7,3]

def orderEvenFirst(array):
    start = 0
    end = len(array) - 1
    while start < end:
        if(array[start] % 2):
            array[start], array[end] = array[end], array[start]
            end -= 1
        else:
            start += 1
    return array

def orderEvenFirst2(array):
    start, end = 0, 0
    while start < len(array):
        if (not array[start] % 2):
            array[start], array[end] = array[end], array[start]
            end += 1
        start += 1
    return  array


print(orderEvenFirst2([2,5,6,7,3,4]))

# print(not 4%2)

# nums = [2,5,6,7,3,4]
"""
s = 5
sub = 6

"""
#
# nums[0], nums[1] = nums[1], nums[0]
#
# print(nums)


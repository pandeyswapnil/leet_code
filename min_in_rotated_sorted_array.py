def findMin(nums):
    start , end = 0, len(nums) - 1 
    curr_min = float("inf")
    
    while start  <  end :
        mid = start + (end - start ) // 2
        curr_min = min(curr_min,nums[mid])
        
        # right has the min 
        if nums[mid] > nums[end]:
            start = mid + 1
            
        # left has the  min 
        else:
            end = mid - 1 
            
    return min(curr_min,nums[start])

nums = [3,4,5,1,2]
print(findMin(nums))
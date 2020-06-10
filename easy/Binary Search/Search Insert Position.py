def searchInsert(self, nums: List[int], target: int) -> int:
  if nums is None or target is None:
    return -1
  
  # Perform Binary Search
  left, right = 0, len(nums)-1
  
  # Loop until the right pointer crosees the left pointer
  while right >= left:
    # Calculate the middle index
    mid = left + (right-left)//2
    
    # Check if there's a match
    if target == nums[mid]:
      return mid

    # If there's no match, move left or right
    if target < nums[mid]:
      right = mid - 1
    elif target > nums[mid]:
      left = mid + 1
  
  # If we can't find the value, we return the index in which it should be inserted
  return left
def majorityElement(self, nums: List[int]) -> int:
    
    e = {}
    if len(nums) == 1:
        return nums[0]
    
    for i, v in enumerate(nums):
        if v in e:
            e[v] += 1
        else:
            e[v] = 1
            
    majority = math.floor(len(nums)/2)
    max_v = 0
    for i, v in e.items():
      
        
        if majority < v:
            max_v = i
        
            
    return max_v

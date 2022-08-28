
class Solution:
    def move_zeroes(self, nums):
        nzeros = nums.count(0)
        for _ in range(nzeros):
            nums.remove(0)
            nums.append(0)
        return num

    def move_translad_zeros(self, nums):
        start = 0
        for i in range(len(nums)):
            num = nums[i]
            if num != 0:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1
        return nums 

p = Solution()
print(p.move_zeroes([1,2,0,3,0,1]))
print(p.move_translad_zeros([1,2,0,3,0,1]))
              
                
                
                
                

            

                
        
    

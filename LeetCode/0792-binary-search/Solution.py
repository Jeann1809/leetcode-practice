class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.binary_search(nums,0,len(nums)-1,target)
    
    def binary_search(self,nums:list[int], left:int, right:int, target:int):
        middle = (right+left)//2
        print(left,right, middle)
        if nums[middle] == target:
            return middle

        if left >= right:
            return -1

        if target > nums[middle]:
            left = middle+1
        else:
            right = middle-1
        
        return self.binary_search(nums,left,right,target)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try: 
                first_index = i
                x = nums[i]
                y = target - x
                second_index = nums.index(y)
                if first_index == second_index:
                    continue
                answer = [first_index,second_index]
                return answer 
            except: 
                continue
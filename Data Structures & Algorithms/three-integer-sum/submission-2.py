class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans_list = []
        ans_set = set()
        nums.sort()
        for i in range(0, len(nums)):
            curr = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                print(l, r)
                three_sum = curr + nums[l] + nums[r]
                if three_sum == 0:
                    if (curr, nums[l], nums[r]) not in ans_set:
                        ans_list.append([curr, nums[l], nums[r]])
                        ans_set.add((curr, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    r -= 1
                
        return ans_list

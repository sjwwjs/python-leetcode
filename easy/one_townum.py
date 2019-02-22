class Solution:
    def twoSum(self,nums, target):

        dict = {}

        for i in range(len(nums)):

            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:   
                return [dict[target - nums[i]],i]

if __name__ == '__main__':
    print(Solution().twoSum((2, 7, 11, 15), 17))
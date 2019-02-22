class Solution:
    def twoSum(self,nums, target):

        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        利用python中的字典记录记录下每个元素出现的位置
        也就是其他语言中的哈希表
        """
        # dic = dict()
        # for index,value in enumerate(nums):
        #     sub = target - value
        #     if sub in dic:
        #         return [dic[sub],index]
        #     else:
        #         dic[value] = index
        dict = {}

        for i in range(len(nums)):

            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:   
                return [dict[target - nums[i]],i]

if __name__ == '__main__':
    print(Solution().twoSum((2, 7, 11, 15), 17))
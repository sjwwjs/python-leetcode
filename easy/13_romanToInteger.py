class Solution(object):
	"""docstring for Solution"""
	def romantointer(self, s):
		#创建dic进行储存查找 这样省去大量的if else
		num_map  ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
		result = 0
		#只需要判断某一个字母是不是比之前的字母大 
		#1、如果大的话就需要当前这个字母减去前面的字母
		#2、如果小的话  就相加到result中
		
		#输入: "MCMXCIV"
        #输出: 1994
        #解释: M = 1000, CM = 900, XC = 90, IV = 4.
		for i in range(len(s)):
			if i>0 and num_map[s[i]] > num_map[s[i-1]]:
				result += num_map[s[i]] - 2*num_map[s[i-1]]
				print('result_a',result)
			else:
				result += num_map[s[i]]
				print('result_b',result)
		return result

if __name__ == '__main__':
    print(Solution().romantointer("MCMXCIV"))
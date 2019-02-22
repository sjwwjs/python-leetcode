class Solution(object):
	"""docstring for Solution"""
	def nine_isPalindrome(self, x):
		num = 0
		a =  abs(x)
		#在这个while里面我从a里面的最右边取到最左边，每次取一个值然后放在num里面
		#负数肯定不是回文数 因为旋转之后的数和原来不相等  
		while(a != 0 ):
			#123
			#a =123
			#num = 0
			#第一次循环
			#a = 12
			#num = 3
			#第二次循环
			#a = 1
			#num = 32
			#第三次循环
			#a = 0
			#num = 321
			#num = 0
			temp = a%10
			# print('a',a)
			# print('temp',temp)
			num = num*10 +temp
			# print('num',num)
			#python3里面如果只想 保留商而不是余数的话  可以用// 或者用int强制转换
			a = a//10
		if x > 0 and x==num:
			return True
		else:
			return False


if __name__ == '__main__':
    print(Solution().nine_isPalindrome(123))
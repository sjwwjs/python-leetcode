class Solution(object):
	"""docstring for Solution"""
	def reverse(self, x):
		num = 0
		a =  abs(x)
		#在这个while里面我从a里面的最右边取到最左边，每次取一个值然后放在num里面
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
			print('a',a)
			print('temp',temp)
			num = num*10 +temp
			print('num',num)
			a = int(a/10)
		if x > 0 and num <= 2147483648:
			return num
		elif x < 0 and num <= 2147483647:
			return -num 
		else:
			return 0


if __name__ == '__main__':
    print(Solution().reverse(123))
		
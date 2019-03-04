class Solution(object):
    def longestCommmonPrefix(self,strs):
        #首先考虑特殊情况，如果没有字符串应该返回空
        if not strs:
            return  ""
        #从我们字符串组里面的第一个字符串逐个与剩下的字符串进行比照
        #  如果第一个字符串的第i位置和剩下字符串的i位置不相等则返回
        #注意这里我们需要考虑特殊情况 如果前一个字符串比后一个长度长 则必须考虑越界问题
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return  strs[0]
if __name__ == '__main__':
    print(Solution().longestCommmonPrefix(["flower","flow","flight"]))

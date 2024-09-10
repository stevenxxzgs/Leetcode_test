#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode.cn/problems/longest-common-prefix/description/
#
# algorithms
# Easy (44.32%)
# Likes:    3175
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 3.1M
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
# 
# 
# 
# 提示：
# 
# 
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def findSameChar(self, str1: str, str2: str):
        s = ''
        # len : str2 > str1
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                s += str1[i]
            if str1[i] != str2[i]:
                break
        return s
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=len)
        n = len(strs)
        s = strs[0]
        for i in range(n-1):
            s = self.findSameChar(s,strs[i+1])
        return s
# @lc code=end


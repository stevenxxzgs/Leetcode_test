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
        n = min(len(str1), len(str2))
        i = 0
        while i < n and str1[i] == str2[i]:
            i += 1
        return str1[:i]
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=len)
        n = len(strs)
        s = strs[0]
        for i in range(1,n):
            s = self.findSameChar(s,strs[i])
        return s
# @lc code=end


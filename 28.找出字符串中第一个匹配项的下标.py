#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#
# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Easy (44.11%)
# Likes:    2278
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.6M
# Testcase Example:  '"sadbutsad"\n"sad"'
#
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0
# 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
# 
# 
# 示例 2：
# 
# 
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= haystack.length, needle.length <= 10^4
# haystack 和 needle 仅由小写英文字符组成
# 
# 
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_need = len(needle)
        n_haystack = len(haystack)
        new_string = needle + '#' + haystack
        pi = [0] * len(new_string)
        for i in range(1, len(new_string)):
            len1 = pi[i-1]
            while(len1 != 0 and new_string[i] != new_string[len1]):
                len1 = pi[len1-1]
            if(new_string[i] == new_string[len1]):
                pi[i] = len1 + 1
                if pi[i] == n_need:
                    return i - n_need*2
        return -1

# @lc code=end


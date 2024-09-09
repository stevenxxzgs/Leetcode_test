#
# @lc app=leetcode.cn id=2217 lang=python3
#
# [2217] 找到指定长度的回文数
#
# https://leetcode.cn/problems/find-palindrome-with-fixed-length/description/
#
# algorithms
# Medium (34.52%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    8.4K
# Total Submissions: 24.2K
# Testcase Example:  '[1,2,3,4,5,90]\n3'
#
# 给你一个整数数组 queries 和一个 正 整数 intLength ，请你返回一个数组 answer ，其中 answer[i] 是长度为
# intLength 的 正回文数 中第 queries[i] 小的数字，如果不存在这样的回文数，则为 -1 。
# 
# 回文数 指的是从前往后和从后往前读一模一样的数字。回文数不能有前导 0 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：queries = [1,2,3,4,5,90], intLength = 3
# 输出：[101,111,121,131,141,999]
# 解释：
# 长度为 3 的最小回文数依次是：
# 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
# 第 90 个长度为 3 的回文数是 999 。
# 
# 
# 示例 2：
# 
# 
# 输入：queries = [2,4,6], intLength = 4
# 输出：[1111,1331,1551]
# 解释：
# 长度为 4 的前 6 个回文数是：
# 1001, 1111, 1221, 1331, 1441 和 1551 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= queries.length <= 5 * 10^4
# 1 <= queries[i] <= 10^9
# 1 <= intLength <= 15
# 
# 
#

# @lc code=start
class Solution:
    def kthPalindrome(self, queries: list, intLength: int) -> list:
        res = []
        max_num_flag = 0
        halflen = intLength // 2
        flag = intLength - int(2 * halflen)
        if flag == 0:
            begin_num =  10 ** (halflen-1)
            max_num_flag = 10 ** halflen - begin_num 
        else:
            begin_num =  10 ** (halflen)
            max_num_flag = 10 * ((10 ** halflen) - 10 ** (halflen-1) )
        for i in queries:
            if i > int(max_num_flag):
                res.append(-1)
            else:
                half = begin_num + i - 1
                if intLength == 1:
                    res.append(i) 
                    continue
                if flag == 0:
                    res.append(int(str(half) + str(half)[::-1]))
                else:
                    res.append(int(str(half) + str(half)[-2::-1]))
        return res
# @lc code=end


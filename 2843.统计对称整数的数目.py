#
# @lc app=leetcode.cn id=2843 lang=python3
#
# [2843] 统计对称整数的数目
#
# https://leetcode.cn/problems/count-symmetric-integers/description/
#
# algorithms
# Easy (71.32%)
# Likes:    13
# Dislikes: 0
# Total Accepted:    9K
# Total Submissions: 12.7K
# Testcase Example:  '1\n100'
#
# 给你两个正整数 low 和 high 。
# 
# 对于一个由 2 * n 位数字组成的整数 x ，如果其前 n 位数字之和与后 n 位数字之和相等，则认为这个数字是一个对称整数。
# 
# 返回在 [low, high] 范围内的 对称整数的数目 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：low = 1, high = 100
# 输出：9
# 解释：在 1 到 100 范围内共有 9 个对称整数：11、22、33、44、55、66、77、88 和 99 。
# 
# 
# 示例 2：
# 
# 
# 输入：low = 1200, high = 1230
# 输出：4
# 解释：在 1200 到 1230 范围内共有 4 个对称整数：1203、1212、1221 和 1230 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= low <= high <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, x):
        import math
        if x < 0 : return False
        rev, result, result_rev = 0, 0, 0
        count = 1
        if int(math.log10(abs(x)))%2 != 0:
            for i in range(int(math.log10(abs(x)))//2 + 1):
                if x % 10 == 0:
                    rev = rev + 10**count
                    count += 1
                else:
                    rev = rev * 10 + x % 10
                result_rev = result_rev + x % 10
                x //= 10
            while x > 0:
                result = result + x % 10
                x //= 10
        else:
            return False
        return True if(result == result_rev) else False
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = []
        for i in range(low, high+1):
            if self.isPalindrome(i):
                result.append(i)
        print(result)
        return len(result)

# @lc code=end


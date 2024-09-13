#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode.cn/problems/jump-game/description/
#
# algorithms
# Medium (43.43%)
# Likes:    2858
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.4M
# Testcase Example:  '[2,3,1,1,4]'
#
# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def search_jump(self, s, e, jump) -> bool:
        for i in range(s,e+1):
            if jump[i]: return True
        return False

    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1 and nums[0] >= 0:
            return True
        jump = [False] * len(nums)
        n = len(nums) - 1
        for i in range(1, len(nums)):
            cur = n-i
            if nums[cur] >= i :
                jump[cur] = True
            if nums[cur] < i and self.search_jump(cur+1, cur+nums[cur], jump) :
                jump[cur] = True
        return jump[0]
# @lc code=end


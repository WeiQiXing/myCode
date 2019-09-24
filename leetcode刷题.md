**1.两数之和**
    A+B=target，这个可以使用暴力求解，双重for循环即可。当然，使用哈希表更快一点。
    主要是写了C++版本和python3版本的：
    python3版本可以使用list.index()函数来直接查找B=target-A。python的运行时间和内存消耗都较C++有点高。
python版

    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            for i in range(0,len(nums)):
                b = target -nums[i]
                if b in nums and nums.index(b)!=i:
                    return i,nums.index(b)

**2.两数相加**
主要思路是每个节点相加，如果有进位，就在下一次的节点中加上进位，主要是两种测试用例出错，一种是两个链表的长度不一致，另一个是[5],[5]相加，有进位最后却没显示。一开始使用暴力的解法，应该是时间有限制，运行没有出错。还要记得python里边的None等价于null。
python版

    class Solution:
        def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            i=0
            carry=0
            l3=ListNode(0)
            current = l3
            print(l2.val)
            while l1 is not None or l2 is not None:
                a=b=0
                if l1 is not None:
                    a = l1.val
                if l2 is not None:
                    b = l2.val
                s = a +b +carry
                if s>=10:
                    carry=1
                    s = s % 10
                else:
                    carry=0
                current.next=ListNode(s)
                current=current.next
                if l1 is not None:l1=l1.next
                if l2 is not None:l2=l2.next
                if carry>0:
                    current.next=ListNode(carry)
            return l3.next

**3.无重复字符的最长子串**
    这个的主要思路是滑动窗口，判断某个字符串是否在队列中，如果不再就直接加入到队列，如果已经存在，就将这个字符以及它前面的所有字符都弹出。当然每次都要统计队列的长度，找出最大的即可。测试时，有点小问题，如果是空字符串就直接返回0，如果是1个字符，也可以直接返回1，因为这都不会重复。

    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            length = []
            shortlist =[]
            if len(s)==0:return 0
            if len(s)==1:return 1
            for i in range(len(s)):
                if s[i] not in shortlist:
                    shortlist.append(s[i])
                else:
                    while s[i] in shortlist:
                        shortlist.pop(0)
                    shortlist.append(s[i])
                le = len(shortlist)
                length.append(le)
            return max(length)







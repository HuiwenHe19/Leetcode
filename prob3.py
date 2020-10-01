# Leetcode Problem 3 
# Oct 1 2020
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    cur_s = ""
    maxl = 0
    dic = {}
    for c in s:
        if c in dic:
            ret_ind = 0
            for i in range(len(cur_s)):
                if cur_s[i] == c:
                    ret_ind = i
                    break
                del dic[cur_s[i]]
            del dic[c]
            cur_s = cur_s[ret_ind+1:]
        dic[c] = c
        cur_s = cur_s + c
        if len(cur_s) > maxl:
            maxl = len(cur_s)
    return maxl

# print(lengthOfLongestSubstring("abcabcbb")==3)


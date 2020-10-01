def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    # take good use of python set characteristic
    # sliding window -> left and right index are enough
    c_set = set()
    maxl = 0
    l = 0

    for r in range(len(s)):
        if s[r] in c_set:
            while s[r] in c_set:
                c_set.remove(s[l])
                l += 1
        c_set.add(s[r])
        cur_len = r-l+1
        if maxl < cur_len:
            maxl = cur_len
    return maxl



print(lengthOfLongestSubstring("abcabcbb")==3)


# Python set:
# s = set()
# s1 = {}
# len(s)
# set.add(element)
# set.remove(element)
# element in s 
# s.union(s1)
# s.intersection(s1)
# s.difference(s1)
# s.clear()

# python find
# index_of_cha = str.find(cha)
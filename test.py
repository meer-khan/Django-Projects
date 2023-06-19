# def lengthOfLongestSubstring(s: str) -> int:
#         chars = []
#         count = 0
#         totalCount = 0
#         for char in s: 
#             if char not in chars: 
#                 chars.append(char)
#                 count+=1
#                 if totalCount < count: 
#                      totalCount = count
#             else:  
#                 # totalCount = len(chars)
#                 chars = []
#                 count = 1
#                 chars.append(char)
#                 # for revchar in s: 
                
#         return totalCount


def lengthOfLongestSubstring(s: str) -> int:
        chars = []
        count = 0
        totalCount = 0
        for char in range(len(s)): 
            if s[char] not in chars: 
                chars.append(s[char])
                count+=1
                if totalCount < count: 
                     totalCount = count
            else:  
                # totalCount = len(chars)
                chars.remove(s[char])
                # count = 1
                chars.append(s[char])
                
                
        return totalCount,chars



# --> 4
print(lengthOfLongestSubstring('davdf'))

# --> 3
print(lengthOfLongestSubstring('dvdf'))


# --> 2
print(lengthOfLongestSubstring('aab'))

# --> 3
print(lengthOfLongestSubstring('abcabcbb'))

# -->1
print(lengthOfLongestSubstring('bbbbb'))

# -->3
print(lengthOfLongestSubstring('pwwkew'))

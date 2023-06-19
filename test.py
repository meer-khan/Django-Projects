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


# def lengthOfLongestSubstring(s: str) -> int:
#         chars = []
#         count = 0
#         totalCount = 0
#         matchStart = 0
#         for char in range(len(s)): 
#             if s[char] not in chars: 
#                 # if matchStart == char
#                 # matchStart = char
#                 chars.append(s[char])
#                 count+=1
#                 if totalCount < count: 
#                      totalCount = count
#             else:  
#                 # totalCount = len(chars)
#                 # chars.remove(s[char])
#                 for i in range (char,len(chars)):
#                      chars.pop(i) 
#                 # count = 1
#                 chars.append(s[char])



def lengthOfLongestSubstring( s: str) -> int:
        chars = []
        count = 0
        totalCount = 1
        matchStart = 0
        if len(s) == 0:
            return 0
        for iIndex in range(len(s)):
            if s[iIndex] not in chars:
                chars.append(s[iIndex]) 
            for jIndex in range(iIndex+1,len(s)): 
                if s[jIndex] not in chars: 
                        chars.append(s[jIndex])
                        count = len(chars)
                else:  
                    chars = []
                    break
            
            if totalCount < count:
                 totalCount = count
        return totalCount



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

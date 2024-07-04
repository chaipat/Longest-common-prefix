def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]

    for string in strs[1:]:
        
        # print('*-------*')

        while string.find(prefix) != 0:
            
            # print(prefix[:-1])
            prefix = prefix[:-1]
            # print(prefix)
            # print('-------')
            if not prefix:
                return ""

    return prefix

strs1 = ["flower","flow","flight"]
print("Array:", strs1)
print("Longest Common Prefix:", longest_common_prefix(strs1))

strs2 = ["dog","racecar","car"]
print("Array:", strs2)
print("Longest Common Prefix:", longest_common_prefix(strs2))

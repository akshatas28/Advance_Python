# LONGEST COMMON PREFIX


strs = ["flower","flow","flight"]

def findprefix(strs):
    if not strs:
        return ""
    
    prefix = ""
    
    # 1. OUTER LOOP: Step through each character position (j = 0, 1, 2...)
    for j in range(len(strs[0])):
        char_to_match = strs[0][j]
        
        # 2. INNER LOOP: Check this character against every word (i = 0, 1, 2...)
        for i in range(len(strs)):
            
            # Safety check: does the word end early?
            # Or does the character not match?
            if j >= len(strs[i]) or strs[i][j] != char_to_match:
                return prefix  # Stop and return whatever we have built so far!
                
        # If the inner loop finishes without hitting 'return', the character is safe!
        prefix += char_to_match
        
    return prefix
print(findprefix(strs))
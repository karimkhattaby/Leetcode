def isSubsequence(self, s, t):
    # Checking for null values
    if s is None or t is None:
        return False
    # Checking for empty subsequence string
    if s == "":
        return True
    
    # initialize 2 pointers, one for each string
    s_ptr = 0
    t_ptr = 0

    # loop through the characters of both strings
    while t_ptr < len(t) and s_ptr < len(s):
        # if the characters match
        if s[s_ptr] == t[t_ptr]:
            # go to the next character in the subsequence string
            s_ptr +=1
        # regardless, go to the next character in the total string
        t_ptr +=1
        
        # after the loop, check if we have a match
        return s_ptr == len(s)
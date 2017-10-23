def is_anagram(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    return(s1 == s2)

def question1(s,t):
    for i in range(len(s) - len(t) + 1):
    	# helper function which checks for t in s
        if is_anagram(s[i: i + len(t)], t):
            return True
    return False
                   

# test Cases

print question1('university','tn') # False
print question1('Udacity', 'da') # True
print question1('programming', 'gram') # True
    

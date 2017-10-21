# takes a string input and returns true if string is a palindrome
def is_palindrome(s):
    return s == s[::-1]


#print is_palindrome('abba')


def next_substring(s):
    length = len(s)
    for i in range(length, 0, -1):
        for j in range(length - i + 1):
            yield s[j:j+i]

#print next_substring('abba')
#print next_substring('abba')

def question2(s):
    for string in next_substring(s):
        if is_palindrome(string):
            return string

print question2("aracecarbc")
print question2("abba")
print question2("coffee")
        

import re

def reverse_words(s):
    s = s.strip()                 		
    s = re.sub(' +', ' ', s)   		 
    words = s.split(' ')		
    reversed_words = reverse(words)		
    outstr = " ".join([str(elem) for elem in reversed_words])
    return outstr

def reverse(s):
    out = []
    for i in range(len(s)-1, -1, -1):
        out.append(s[i])
    return out
print(reverse_words("i am good"))
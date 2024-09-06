s = "iloveleetcode"
words = ["apples","i","love","leetcode"]
x="".join(word for word in words)
if s[0] == x[0] and s in x and len(x)<len(s):
    print(True)
else:
    print(False)
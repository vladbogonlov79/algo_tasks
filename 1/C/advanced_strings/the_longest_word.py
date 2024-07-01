word = input()
s = word.split()
mxs = s[0]
for i in range(1, len(s)):
    if len(s[i]) > len(mxs):
        mxs = s[i]
print(mxs, len(mxs), sep='\n')

s1 = input()
s2 = input()

alphabet = [0]*26
for s in s1:
    alphabet[ord(s)-97] += 1

for s in s2:
    alphabet[ord(s)-97] -= 1

res = 0 #제거해야할 문자
for i in alphabet:
    res += abs(i)
print(res)
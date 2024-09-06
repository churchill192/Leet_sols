words= ["Hello","Alaska","Dad","Peace"]
r1 = set('qwertyuiop')
r2 = set('asdfghjkl')
r3 = set('zxcvbnm')
R1 = []
R2 = []
R3 = []
for i in words:
    word_set = set(i.lower())

    if word_set.issubset(r1) and not (word_set.issubset(r2) and word_set.issubset(r3)):
        R1.append(i)
    elif word_set.issubset(r2) and not (word_set.issubset(r1) and word_set.issubset(r3)):
        R2.append(i)
    elif word_set.issubset(r3) and not (word_set.issubset(r2) and word_set.issubset(r1)):
        R3.append(i)


R=R1+R2+R3
print(R)

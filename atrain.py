order = "cba"
s = "abcd"
x = ""
list1 = list(order)

list2 = list(s)


for i in order:
    if i in s:
        x += i


        
for i in list1:
    if i in list2:
        list2.remove(i)
res = []
for i in list2:
            z = []
            if i in x:
                  l = list(x)
                  a = l.index(i)+1
                  l.insert(a,i)
                  result = "".join(l)
                  z.append(result)
            
            
            res.append(z)

print(res)
            





        



#print(result)
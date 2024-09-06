x={}


#string="a, a, a, a, b,b,b,c, c"
string="a, a, a, a, b,b,b,c, c"



string=string.replace(","," ")
string=string.replace("."," ")
banned=["a"]

y=string.lower()
para=list(y.split(" "))





for i in para:
    x[i]=para.count(i)
if "" in x:
    x.pop("")
print(x)
for i in banned:
            if i in x:
                x.pop(i)
count=[]



count=list(x.values())
maxx=max(count)
for key,value in x.items():
    if value == maxx:
        ans=key
# print(ans)
print(str(ans))
#print(x)


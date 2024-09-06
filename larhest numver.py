import functools
nums=[3,30,34,5,9,8]
for i,n in enumerate(nums):
    nums[i]=str(n)

def mycmp(n1,n2):
    if n1+n2>n2+n1:
        return -1
    else:
        return 1



nums=sorted(nums,key=functools.cmp_to_key(mycmp))
print(str(int("".join(nums))))

x="Abc"
a=x[0].lower()
print(a)
R1=["dad",'dad','dad']
R2=['mom','mom','mom']

R1=list(set(R1))
R2=list(set(R2))
R=R1+R2
print(R)
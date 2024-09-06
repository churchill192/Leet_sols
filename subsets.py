nums = [1,2,3]
result=[[]]

length = len(nums)


for start in range(length):
    for end in range(start+1,length+1):
        result.append(nums[start:end])
print(result)

"""
for i in nums:
    x=[]
    x.append(i)
    result.append(x)
length = len(nums)
for i in range(length):
    y=[]
    
print(result)
"""
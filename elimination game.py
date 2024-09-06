n=int(input())
arr=[]
for i in range(1,n+1):
    arr.append(i)

# while len(arr)>1:
#     del arr[0::2]
#     arr = arr[::-1]
a = 1
while len(arr)>1:
    if a%2!=0:
        for i in range(0,len(arr)+1,2):
            arr.pop(i)
        a+=1
    else:
        for i in range(len(arr),0,-2):
            arr.pop(i)
        a+=1



print(arr)
# arr=[1,2,3,4,5,6,7,8]
# for i in range(0,9,2):
#     arr.pop(i)
#     print(i,end="")
# print(" ")
# for i in range(3,0,-2):
#     print(i,end="")
#     arr.




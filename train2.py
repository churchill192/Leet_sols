
arr = "2[abc]3[cd]ef"
arr=(arr.split("]"))
for i in range(len(arr)):
    arr[i] = arr[i].replace("[","")

print(arr)

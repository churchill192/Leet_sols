# counter = 0
# def inception():
#     global counter
#     if counter>3:
#         return "done"
#     counter +=1
#     return inception()
#
# inception()
x = 1
def findFactorialRecursive(n):
    global x
    if n==1:
        return x
    x = n * findFactorialRecursive(n - 1)
    return x

print(findFactorialRecursive(3))

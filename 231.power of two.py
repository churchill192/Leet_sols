x = 0

def pow(n):
    global x
    if (2**x) == n:
        return True
    else:
        x+=1
        if (2**x)>n:
            return False
        else:
            return pow(n)

print(pow(16))
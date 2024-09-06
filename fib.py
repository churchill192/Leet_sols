
def fibno(n):
    if n<2:
        return n
    else:
        return fibno(n-1) + fibno(n-2)

print(fibno(6))
dividend = 7
divisor = -3
x=0
y=0


if (dividend > 0) and divisor>0:
    while x + divisor < dividend:
        x = x + divisor
        y=y+1
    print(y)
else:
    divisor=abs(divisor)
    dividend=abs(dividend)
    while x + divisor < dividend:
        x = x + divisor
        y=y+1

    print(-(y))





#4.6 Add definition
# Promptthe user for hours and rate per hour using input.

def computepay(h,r):
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("Enter Rate:")
    r = float(rate)
    if h<= 40:
        i = h*r
        return i
    else:
        x=h-40
        s=h-x
        i2 =s*r+x*r*1.5
        return i2

p = computepay(10,20)

print("Pay",p)

#Add Sick Leave Hours
#4.6 Add definition
# Promptthe user for hours and rate per hour using input.

def computepay(h,r,sl):
    hrs = input("Enter Work Hours:")
    h = float(hrs)
    shrs = input("Enter Sick Leave Hours:")
    sh = float(shrs)
    sl=sh*0.8
    rate = input("Enter Rate:")
    r = float(rate)
    if h<= 40:
        i = h*r+sl
        return i
    else:
        x=h-40
        s=h-x
        i2 =s*r+x*r*1.5+sl
        return i2

p = computepay(10,20,30)

print("Pay me ",p)

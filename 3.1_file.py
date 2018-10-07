#3.1 Promptthe user for hours and rate per hour using input.



hrs = input("Enter Hours:")

h = float(hrs)

rate = input("Enter Rate:")

r = float(rate)

if h<= 40:
    print("Pay ",h*r)
else:
    x=h-40
    s=h-x
    print(s*r+x*r*1.5)

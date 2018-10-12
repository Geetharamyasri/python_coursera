#problem był z inaczej dzialajaca funkcja input w python2 - raw_input
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num=int(num)
    except:
        print("Podaj liczbe")
        continue
    print(num)
    if largest is None and smallest is None:
        largest=num
        smallest=num
    elif num >largest:
        largest=num
        continue
    elif num<smallest:
        smallest=num

print("Maximum", str(largest))
print("Minimum", str(smallest))

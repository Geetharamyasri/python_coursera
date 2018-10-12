#pierwsza wersja nieskonczona
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 0: #nie dziala ze stringiem
        break
    try:
        num=int(num) #mimo wszystko wyrzuca blad
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

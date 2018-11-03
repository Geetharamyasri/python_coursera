#program categorizes each mail by which day of the week the commit was doneself.
#day of the week and number of appears as a key-value pair

ofile = raw_input("Enter a file: ")
try:
    file = open(ofile)
except:
    exit()

emails = list()
days = list()
dane = dict()

for line in file:
    if len(line) < 3:
        continue
    elif line.startswith("From") and not line.startswith("From:"):
        emails = line.split()
        day = emails[2]
        days.append(day)

for s in days:
    dane[s] = dane.get(s, 0)+1

print dane

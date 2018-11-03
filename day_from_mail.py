#program categorizes each mail by which day of the week the commit was doneself.
#day of the week and number of appears as a key-value pair

def get_dane():
    ofile = raw_input("Enter a file: ")
    try:
        file = open(ofile)
    except:
        exit()
    return file

def main():
    file2 = get_dane()
    
    emails = list()
    days = list()
    dane = dict()

    for line in file2:
        if len(line) < 3:
            continue
        elif line.startswith("From") and not line.startswith("From:"):
            emails = line.split()
            day = emails[2]
            days.append(day)

    for s in days:
        dane[s] = dane.get(s, 0)+1

    print dane

if __name__ == "__main__":
    main()

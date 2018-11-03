#Exc. 3,4 Chapet 9. Read throw a mail log and count how many messages have come from each email address
#print the dictionary
#print the email address that appears most times

def get_dane():
    ofile = raw_input("Enter a file name: ")
    try:
        file = open(ofile)
    except:
        exit()
    return file

def main():
    file2 = get_dane()

    lines = list()
    addresses = list()
    dane = dict()
    bigaddress = 0
    bigcount = 0

    for line in file2:
        if line.startswith("From") and not line.startswith("From:"):
            lines = line.split()
            x = lines[1]
            addresses.append(x)

            #create dictionary
    for s in addresses:
        dane[s] = dane.get(s, 0) + 1
    print dane

    for key, value in dane.items():
        if value > bigcount:
            bigcount = value
            bigaddress = key

    print bigaddress, bigcount

if __name__ == "__main__":
    main()

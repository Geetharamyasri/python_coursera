#Chapter8, Exc1
#Read a file and put raws to the list,
#a function takes a list and returns a new list
#that contains all but firts and last elements, print them.

def middle():
    ofile = raw_input("Enter file name: ")
    try:
        file = open(ofile)
    except:
        print("Wrong file name, try again ;)")
        exit()

    list = []

    for i in file:      #from file to the list
        i = i.rstrip()
        list.append(i)

    newlist = list[1:-1]    #only the middle
    for s in newlist:
        print s

middle()

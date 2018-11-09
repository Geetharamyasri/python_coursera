#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

abc = list()
time = list()
onlyhour = list()
pair = dict()
newlist = list()

for line in handle:
    if len(line)<1: continue
    elif line.startswith("From "):
            abc = line.split()
            time.append(abc[5])
for i in time:
    onlyhour.append(i[0:2])

for s in onlyhour:
    pair[s] = pair.get(s, 0)+1

for k,v in pair.items():
    newpair = (k,v)
    newlist.append(newpair)
newlist = sorted(newlist)

for w,z in newlist:
    print w,z

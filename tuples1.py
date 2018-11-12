#10.11 Tuples Ex.1
#print person who has the most commits

ofile = raw_input("Add a file name: ")
if len(ofile)<1: ofile = "mbox-short.txt"
file = open(ofile)

list1 = list()
emails = list()
ecount = dict()
tlist = list()

for l in file:
    if l.startswith("From "):
        list1 = l.split()
        emails.append(list1[1])

for s in emails:
    ecount[s] = ecount.get(s, 0)+1

for k,v in ecount.items():
    newpair = (v,k)
    tlist.append(newpair)
tlist = sorted(tlist, reverse=True)
print tlist[0]

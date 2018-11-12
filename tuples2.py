#10.11 Tuples Ex.2
#print sorted counts of the hours

ofile = raw_input("Add a file name: ")
if len(ofile)<1: ofile = "mbox-short.txt"
handle = open(ofile)

lines = list()
thours = list()
hours = list()
hcount = dict()
final = list()

for line in handle:
    if line.startswith("From "):
        lines  = line.split()
        thours.append(lines[5])

for s in thours:
    hours.append(s[:2])
print hours

for i in hours:
    hcount[i] = hcount.get(i, 0)+1
print hcount

for k,v in hcount.items():
    x = (k,v)
    final.append(x)

for q,w in sorted(final):
    print q,w

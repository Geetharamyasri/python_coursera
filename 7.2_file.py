#7.2 Write a program that prompts for a file name,
#then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines
#and compute the average of those values and produce an output as shown below.

ofile = raw_input("Enter file name: ")
rfile = open(ofile)
count = 0
s = 0
av = 0
l = 0

for line in rfile:
    if line.startswith("X-DSPAM-Confidence:"):
        print line
        x = (line.find(":"))
        y = float(line[x+1:])
        s = s + y
        l = l + 1
    else:
        continue
print ("Average: " + str(s/l))

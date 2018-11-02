#9.4 Write a program to read through the mbox-short.txt
#and figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear
#in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop
#to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lista = list()
dane = dict()
y = list()

#create list with emails
for line in handle:
    if len(line)<2: continue
    elif line.startswith("From") and not line.startswith("From:"):
        lista = line.split()
        x = lista[1]
        y.append(x)

#create dictionary:emails and numbers of times they appear
for i in y:
    dane[i] = dane.get(i, 0)+1

#maximum loop
bigemail = 0
bigcount = 0

for word, count in dane.items():
    if count > bigcount:
        bigcount = count
        bigemail = word
print bigemail, bigcount

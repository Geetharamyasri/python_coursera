#8.5 Open the file mbox-short.txt and read it line by line.
#When you find a line that starts with 'From ' like the following line:
#You will parse the From line using split() and print out the second word in the line
#(i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.


fname = open("mbox-short.txt")
count = 0
list = []

for i in fname:
    if i.startswith("From"):
        i = i.strip()
        list = i.split()

        #guardian in statement
        if len(list) < 2 or list[0]=="From:": continue

        print list[1]
        count = count+1
    else: continue

print("There were "+ str(count) +" lines in the file with From as the first word")

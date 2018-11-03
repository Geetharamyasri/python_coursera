#program reads words from a file and stores them in a dictionary,
#program check whether the string is in the dictionary

ofile = raw_input("Enter name of the file: ")

try:
    file = open(ofile)
except:
    exit()
lista = list()
dane = dict()

#add words to the dictionary as keys
for line in file:
    lista = line.split()
    for s in lista:
        dane[s] =''
print dane

#finding a word
while True:
    search = raw_input("Enter a word to find: ")
    if search in dane:
        print "YES"
    else:
        print "NO"

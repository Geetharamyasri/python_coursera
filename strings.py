#Chapter 6 Exc.1 Print letters of the string backwords

x = 0
word = 'abrakadabra'
y = len(word)

while x <len(word):
    print word[y-1]
    x = x+1
    y = y-1

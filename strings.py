#Chapter 6 Exc.1 Print letters of the string backwords
x = 0
word = 'abrakadabra'
y = len(word)

while x <len(word):
    print word[y-1]
    x = x+1
    y = y-1

#Chapter 6 Exc.2
fruit = 'banana'
print fruit[:]

#Chapter 6 Exc.3 Write a function with finds letter in a string
def find_letters(str,letter):
    count = 0
    for i in str:
        if i == letter:
            count = count +1
    print count

find_letters("abrakadabra", "a")

#Chapter 6 Exc.4 Method count
word = 'banana'
print (word.count('a'))

#Format operator
number = 567
text ='best'
float = 4.5
print "So %d is the %s %g"%(number, text, float)
